"""RAG pipeline for Saç Ekimi Chatbot with Gemini API

This module provides:
- Document loading from data/sac_ekimi_veri_seti.py
- Embedding creation using sentence-transformers
- Chroma vectorstore for similarity search
- Gemini API integration for answer generation
"""
from typing import List, Optional
from haystack import Document
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Global variables for caching
_documents_cache: Optional[List[Document]] = None
_collection_cache = None
_embedding_model_cache = None


def load_documents_from_data() -> List[Document]:
    """Import and return document list from the provided data module."""
    global _documents_cache
    if _documents_cache is not None:
        return _documents_cache
    
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "sac_ekimi_veri_seti.py")
    import importlib.util

    spec = importlib.util.spec_from_file_location("sac_data", data_path)
    sac_data = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sac_data)
    _documents_cache = sac_data.create_hair_transplant_dataset()
    return _documents_cache


def get_embedding_function():
    """Get Gemini embedding function (uses API, no local model download)."""
    import google.generativeai as genai
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not found in .env")
    genai.configure(api_key=api_key)
    
    def embed_texts(texts):
        """Embed a list of texts using Gemini API."""
        embeddings = []
        for text in texts:
            result = genai.embed_content(
                model="models/text-embedding-004",
                content=text,
                task_type="retrieval_document"
            )
            embeddings.append(result['embedding'])
        return embeddings
    
    return embed_texts


def build_or_get_collection():
    """Build or retrieve cached Chroma collection with embeddings."""
    global _collection_cache
    
    if _collection_cache is not None:
        return _collection_cache
    
    try:
        import chromadb
        from chromadb.config import Settings
    except ImportError:
        raise RuntimeError("chromadb not installed. Run: pip install chromadb")
    
    docs = load_documents_from_data()
    embed_fn = get_embedding_function()
    
    texts = [d.content for d in docs]
    print(f"Embedding oluşturuluyor: {len(texts)} doküman...")
    embeddings = embed_fn(texts)
    
    # Create in-memory Chroma client
    client = chromadb.Client(Settings(anonymized_telemetry=False))
    
    # Try to get existing collection or create new
    try:
        collection = client.get_collection(name="sac_ekimi_faq")
        print("Mevcut koleksiyon kullanılıyor.")
    except:
        collection = client.create_collection(name="sac_ekimi_faq")
        ids = [f"doc_{i}" for i in range(len(texts))]
        
        # Convert metadata tags (list) to string for Chroma compatibility
        metadatas = []
        for d in docs:
            meta = d.meta.copy() if d.meta else {}
            if "tags" in meta and isinstance(meta["tags"], list):
                meta["tags"] = ", ".join(meta["tags"])
            metadatas.append(meta)
        
        collection.add(
            ids=ids,
            documents=texts,
            metadatas=metadatas,
            embeddings=embeddings
        )
        print(f"✅ Chroma koleksiyonu oluşturuldu: {len(texts)} doküman eklendi.")
    
    _collection_cache = collection
    return collection


def retrieve_relevant_docs(question: str, k: int = 3) -> List[str]:
    """Retrieve top-k relevant documents for the question."""
    collection = build_or_get_collection()
    embed_fn = get_embedding_function()
    
    # Embed the question
    question_embedding = embed_fn([question])[0]
    
    # Query Chroma
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=k
    )
    
    # Extract documents
    if results and "documents" in results and len(results["documents"]) > 0:
        return results["documents"][0]
    return []


def generate_answer_with_gemini(question: str, context_docs: List[str]) -> str:
    """Generate answer using Gemini API with retrieved context."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "⚠️ GEMINI_API_KEY bulunamadı. Lütfen .env dosyasına ekleyin."
    
    genai.configure(api_key=api_key)
    # Use gemini-2.5-flash (newer model)
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    # Build context from retrieved docs
    context = "\n\n---\n\n".join(context_docs)
    
    # Create prompt
    prompt = f"""Sen saç ekimi konusunda uzman bir asistansın. Aşağıdaki bilgilere dayanarak kullanıcının sorusunu Türkçe olarak yanıtla.

BAĞLAM (Saç Ekimi Bilgi Bankası):
{context}

KULLANICI SORUSU: {question}

YANIT (Türkçe, profesyonel ve yardımcı):"""
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Gemini API hatası: {str(e)}"


def retrieve_and_answer(question: str, k: int = 3) -> str:
    """Main RAG pipeline: retrieve relevant docs and generate answer with Gemini."""
    # Retrieve relevant documents
    context_docs = retrieve_relevant_docs(question, k=k)
    
    if not context_docs:
        return "Üzgünüm, bu soruyla ilgili bilgi bulamadım. Lütfen farklı bir şekilde sorar mısınız?"
    
    # Generate answer with Gemini
    answer = generate_answer_with_gemini(question, context_docs)
    return answer


if __name__ == "__main__":
    # Test the pipeline
    docs = load_documents_from_data()
    print(f"✅ Yüklendi: {len(docs)} doküman")
    
    collection = build_or_get_collection()
    print("\n✅ Chroma koleksiyonu hazır")
    
    test_question = "Saç ekimi nedir?"
    print(f"\n🧪 Test sorusu: {test_question}")
    answer = retrieve_and_answer(test_question)
    print(f"\n💬 Cevap:\n{answer}")
