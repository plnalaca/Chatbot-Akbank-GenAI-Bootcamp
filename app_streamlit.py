"""
Saç Ekimi Chatbot - Streamlit Web Arayüzü
Akbank GenAI Bootcamp Projesi
"""
import streamlit as st
import os
from src.rag import retrieve_and_answer

# Page config
st.set_page_config(
    page_title="Saç Ekimi Soru-Cevap",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1rem;
        color: #7f8c8d;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">Saç Ekimi Bilgi Sistemi</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Saç ekimi ile ilgili merak ettiklerinizi sorabilirsiniz</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("Bilgi")
    st.write("""
    Bu sistem RAG (Retrieval Augmented Generation) teknolojisi kullanarak 
    saç ekimi hakkındaki sorularınıza yanıt verir.
    
    **Teknik Detaylar:**
    - Gemini AI dil modeli
    - Vektör tabanlı arama
    - 86 doküman veri seti
    
    **Kapsadığı Konular:**
    - FUE ve DHI yöntemleri
    - Operasyon süreci
    - İyileşme süreci
    - Olası yan etkiler
    - Genel bilgiler
    """)
    
    st.divider()
    
    st.header("Örnek Sorular")
    example_questions = [
        "Saç ekimi nedir?",
        "FUE yöntemi nasıl uygulanır?",
        "Ameliyat sonrası ne kadar dinlenmeliyim?",
        "Şok dökülme ne demek?",
        "Fiyatları etkileyen faktörler neler?",
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
    st.error("API anahtarı bulunamadı. Lütfen .env dosyasını kontrol edin.")
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
        with st.spinner("Yanıt hazırlanıyor..."):
            try:
                response = retrieve_and_answer(question)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"Hata: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

# Chat input
if prompt := st.chat_input("Sorunuzu yazın..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Yanıt hazırlanıyor..."):
            try:
                response = retrieve_and_answer(prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"Hata: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

# Clear chat button (in sidebar)
with st.sidebar:
    if st.button("Sohbeti Temizle", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
