"""
RAG Pipeline - Saç Ekimi Chatbot

LangChain framework kullanarak RAG implementasyonu.
Gemini API ile embedding ve text generation.
"""
from typing import List, Optional
from haystack import Document as HaystackDocument
import os
from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_core.documents import Document as LCDocument
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

# Cache
_haystack_docs_cache: Optional[List[HaystackDocument]] = None
_vectorstore_cache: Optional[Chroma] = None
_rag_chain_cache = None


def load_documents_from_data() -> List[HaystackDocument]:
    """Veri setini yükle"""
    global _haystack_docs_cache
    if _haystack_docs_cache is not None:
        return _haystack_docs_cache
    
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "sac_ekimi_veri_seti.py")
    import importlib.util

    spec = importlib.util.spec_from_file_location("sac_data", data_path)
    sac_data = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sac_data)
    _haystack_docs_cache = sac_data.create_hair_transplant_dataset()
    return _haystack_docs_cache


def convert_to_langchain_documents(haystack_docs: List[HaystackDocument]) -> List[LCDocument]:
    """Haystack dokümanlarını LangChain formatına çevir"""
    lc_documents = []
    for doc in haystack_docs:
        metadata = {
            "kategori": doc.meta.get("kategori", ""),
            "source": doc.meta.get("source", ""),
            "tags": ", ".join(doc.meta.get("tags", []))
        }
        lc_documents.append(
            LCDocument(
                page_content=doc.content,
                metadata=metadata
            )
        )
    return lc_documents


def get_embeddings():
    """Get Gemini embeddings via LangChain wrapper with timeout settings."""
    import time
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not found in .env")
    
    # Add task_type for better embedding quality
    return GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=api_key,
        task_type="retrieval_document"
    )


def build_or_get_vectorstore() -> Chroma:
    """Build or retrieve cached Chroma vectorstore (LangChain style)."""
    import time
    global _vectorstore_cache
    
    if _vectorstore_cache is not None:
        print("✅ Mevcut vectorstore kullanılıyor (cached)")
        return _vectorstore_cache
    
    print("📦 Vectorstore oluşturuluyor...")
    
    # Load and convert documents
    haystack_docs = load_documents_from_data()
    lc_documents = convert_to_langchain_documents(haystack_docs)
    print(f"📄 {len(lc_documents)} doküman yüklendi")
    
    # Get embeddings
    embeddings = get_embeddings()
    
    # Create Chroma vectorstore with retry logic
    max_retries = 3
    for attempt in range(max_retries):
        try:
            print(f"🔄 Embedding oluşturuluyor (deneme {attempt + 1}/{max_retries})...")
            
            # Process in smaller batches to avoid timeout
            batch_size = 20
            if len(lc_documents) > batch_size:
                print(f"📦 Büyük veri seti: {batch_size}'lik batch'ler halinde işlenecek")
                vectorstore = None
                for i in range(0, len(lc_documents), batch_size):
                    batch = lc_documents[i:i+batch_size]
                    print(f"   Batch {i//batch_size + 1}: {len(batch)} doküman")
                    
                    if vectorstore is None:
                        vectorstore = Chroma.from_documents(
                            documents=batch,
                            embedding=embeddings,
                            collection_name="sac_ekimi_langchain"
                        )
                    else:
                        vectorstore.add_documents(batch)
                    
                    time.sleep(1)  # Rate limiting
            else:
                vectorstore = Chroma.from_documents(
                    documents=lc_documents,
                    embedding=embeddings,
                    collection_name="sac_ekimi_langchain"
                )
            
            _vectorstore_cache = vectorstore
            print(f"✅ Chroma vectorstore oluşturuldu: {len(lc_documents)} doküman eklendi")
            return vectorstore
            
        except Exception as e:
            print(f"⚠️ Hata (deneme {attempt + 1}): {str(e)}")
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 5
                print(f"🔄 {wait_time} saniye bekleniyor...")
                time.sleep(wait_time)
            else:
                raise RuntimeError(f"Vectorstore oluşturulamadı: {str(e)}")


def get_retriever(k: int = 5):
    """Get retriever from vectorstore with similarity search."""
    vectorstore = build_or_get_vectorstore()
    # Similarity search with score threshold
    return vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )


def format_docs(docs: List[LCDocument]) -> str:
    """Format retrieved documents for context."""
    return "\n\n---\n\n".join(doc.page_content for doc in docs)


def get_llm():
    """Get Gemini LLM via LangChain wrapper."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not found in .env")
    
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.3
    )


def get_prompt_template():
    """Get RAG prompt template."""
    template = """Sen saç ekimi konusunda uzman bir asistansın. 
Kullanıcının sorusunu Türkçe olarak yanıtla.

BAĞLAM (Saç Ekimi Bilgi Bankası):
{context}

KULLANICI SORUSU:
{question}

YANIT:
Yukarıdaki bağlamdaki bilgileri kullanarak soruya detaylı ve profesyonel bir cevap ver.
Mümkünse bağlamdaki bilgileri referans al ve kullanıcıya yardımcı ol.
"""
    return ChatPromptTemplate.from_template(template)


def build_or_get_rag_chain():
    """Build or retrieve cached RAG chain using LCEL."""
    global _rag_chain_cache
    
    if _rag_chain_cache is not None:
        return _rag_chain_cache
    
    print("🔗 RAG Chain oluşturuluyor (LCEL)...")
    
    # Components
    retriever = get_retriever(k=3)
    prompt = get_prompt_template()
    llm = get_llm()
    
    # Build chain using LCEL
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    _rag_chain_cache = rag_chain
    print("✅ RAG Chain hazır")
    return rag_chain


def retrieve_and_answer(question: str) -> str:
    """
    Main RAG pipeline function: retrieve relevant docs and generate answer.
    
    This function uses LangChain's LCEL (LangChain Expression Language) to:
    1. Retrieve relevant documents from Chroma vectorstore
    2. Format them as context
    3. Pass to Gemini LLM with prompt
    4. Return generated answer
    
    Args:
        question: User's question in Turkish
        
    Returns:
        Generated answer from Gemini based on retrieved context
    """
    try:
        rag_chain = build_or_get_rag_chain()
        answer = rag_chain.invoke(question)
        return answer
    except Exception as e:
        return f"❌ Hata oluştu: {str(e)}\n\nLütfen .env dosyanızda GEMINI_API_KEY'in doğru ayarlandığından emin olun."


def retrieve_relevant_docs(question: str, k: int = 3) -> List[str]:
    """
    Retrieve top-k relevant documents for debugging/inspection.
    
    Args:
        question: User's question
        k: Number of documents to retrieve
        
    Returns:
        List of retrieved document contents
    """
    try:
        retriever = get_retriever(k=k)
        docs = retriever.invoke(question)
        return [doc.page_content for doc in docs]
    except Exception as e:
        print(f"❌ Retrieval hatası: {e}")
        return []


if __name__ == "__main__":
    print("🚀 LangChain RAG Pipeline Test\n")
    print("="*60)
    
    # Test document loading
    docs = load_documents_from_data()
    print(f"✅ Yüklendi: {len(docs)} Haystack doküman")
    
    # Test vectorstore
    vectorstore = build_or_get_vectorstore()
    print("\n✅ Chroma vectorstore hazır")
    
    # Test RAG chain
    print("\n" + "="*60)
    test_questions = [
        "Saç ekimi nedir?",
        "FUE yöntemi nedir?",
        "DHI ve FUE arasındaki fark nedir?"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n🧪 Test {i}: {question}")
        print("-"*60)
        answer = retrieve_and_answer(question)
        print(f"💬 Cevap:\n{answer[:300]}...")
        print("="*60)
