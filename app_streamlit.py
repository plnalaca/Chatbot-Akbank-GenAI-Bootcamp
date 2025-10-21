"""
Saç Ekimi Chatbot - Streamlit Web Arayüzü
Akbank GenAI Bootcamp Projesi
"""
import streamlit as st
import os
from src.rag import retrieve_and_answer

# Page config
st.set_page_config(
    page_title="Saç Ekimi Chatbot",
    page_icon="💇",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
    }
    .assistant-message {
        background-color: #f5f5f5;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">💇 Saç Ekimi Asistanı</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Saç ekimi hakkındaki sorularınızı sorun!</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("ℹ️ Hakkında")
    st.write("""
    Bu chatbot, **RAG (Retrieval Augmented Generation)** teknolojisi ile çalışır:
    
    **Teknoloji:**
    - 🧠 Gemini 2.5-flash
    - 🔍 Gemini Embedding API
    - 📚 ChromaDB (86 doküman)
    - ⚡ FastAPI Backend
    
    **Kapsam:**
    - FUE/DHI yöntemleri
    - Operasyon süreci
    - Bakım ve iyileşme
    - Yan etkiler & riskler
    - Fiyat bilgileri
    """)
    
    st.divider()
    
    st.header("🎯 Örnek Sorular")
    example_questions = [
        "Saç ekimi nedir?",
        "FUE yöntemi nasıl uygulanır?",
        "Saç ekiminden sonra ne kadar süre dinlenmeliyim?",
        "Şok dökülme nedir?",
        "Saç ekimi fiyatlarını ne etkiler?",
        "Ekilen saçlar kalıcı mı?"
    ]
    
    for q in example_questions:
        if st.button(q, key=f"example_{q}", use_container_width=True):
            st.session_state.current_question = q
    
    st.divider()
    st.caption("Akbank GenAI Bootcamp - 2025")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Check API key
if not os.getenv("GEMINI_API_KEY"):
    st.error("⚠️ GEMINI_API_KEY bulunamadı! Lütfen .env dosyasını kontrol edin.")
    st.stop()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle example question click
if "current_question" in st.session_state:
    question = st.session_state.current_question
    del st.session_state.current_question
    
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Düşünüyorum..."):
            try:
                response = retrieve_and_answer(question)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"❌ Bir hata oluştu: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

# Chat input
if prompt := st.chat_input("Sorunuzu buraya yazın..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Düşünüyorum..."):
            try:
                response = retrieve_and_answer(prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"❌ Bir hata oluştu: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

# Clear chat button (in sidebar)
with st.sidebar:
    if st.button("🗑️ Sohbeti Temizle", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
