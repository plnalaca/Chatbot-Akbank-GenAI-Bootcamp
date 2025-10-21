from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.rag import retrieve_and_answer, build_or_get_vectorstore
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Saç Ekimi Chatbot API - LangChain Edition",
    description="RAG-based chatbot for hair transplant Q&A using LangChain + Gemini API",
    version="2.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Query(BaseModel):
    question: str


class ChatResponse(BaseModel):
    question: str
    answer: str


@app.on_event("startup")
async def startup_event():
    """Initialize RAG pipeline on startup (LangChain vectorstore)."""
    logger.info("🚀 Initializing LangChain RAG pipeline...")
    try:
        build_or_get_vectorstore()
        logger.info("✅ LangChain RAG pipeline ready!")
    except Exception as e:
        logger.error(f"❌ Failed to initialize RAG: {e}")


@app.get("/health")
def health():
    """Health check endpoint."""
    return {"status": "ok", "service": "Saç Ekimi Chatbot"}


@app.post("/chat", response_model=ChatResponse)
def chat(q: Query):
    """
    Chat endpoint - answers hair transplant questions using RAG pipeline (LangChain).
    
    Requires GEMINI_API_KEY in .env file.
    """
    if not q.question or len(q.question.strip()) == 0:
        raise HTTPException(status_code=400, detail="Soru boş olamaz.")
    
    try:
        logger.info(f"📝 Soru alındı: {q.question}")
        answer = retrieve_and_answer(q.question)
        logger.info(f"✅ Cevap üretildi (uzunluk: {len(answer)} karakter)")
        return ChatResponse(question=q.question, answer=answer)
    except Exception as e:
        logger.error(f"❌ Chat error: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Bir hata oluştu: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.app:app", host="127.0.0.1", port=8000, reload=True)
