# 🧠 Saç Ekimi Chatbot - Akbank GenAI Bootcamp

Bu repo, **Akbank Generative AI Bootcamp** için hazırlanmış bir **RAG (Retrieval Augmented Generation)** tabanlı chatbot projesidir. Bot, saç ekimiyle ilgili sık sorulan sorulara **Gemini API** kullanarak doğal dilde yanıt verir.

---

## 📁 Proje Yapısı
```
chat_bot/
├── data/
│   └── sac_ekimi_veri_seti.py    # Soru-cevap veri seti (86 doküman)
├── src/
│   ├── __init__.py
│   ├── app.py                     # FastAPI REST API
│   └── rag.py                     # RAG pipeline (LangChain + Gemini)
├── app_streamlit.py               # Streamlit web arayüzü
├── .env.example                   # API key şablonu
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🎯 Projenin Amacı
Saç ekimi hakkında sık sorulan sorulara (FUE/DHI yöntemleri, operasyon süreci, bakım, yan etkiler vb.) **RAG teknolojisi** ile doğru ve hızlı yanıtlar veren bir chatbot geliştirmek.

---

## 📊 Veri Seti Hakkında
- **Kaynak:** `data/sac_ekimi_veri_seti.py`
- **Format:** Haystack `Document` nesneleri (soru-cevap çiftleri)
- **Kaynaklar:** estefavor.com, vitasacekim.com, ankarainternational.com, smilehairclinic.com
- **Kapsam:** 50+ soru-cevap; kategoriler (temel bilgi, yöntemler, operasyon, bakım, yan etkiler, fiyat, vb.)

---

## 🛠️ Kullanılan Teknolojiler

### RAG Pipeline
- **Framework:** LangChain + LCEL (LangChain Expression Language)
- **Embedding:** GoogleGenerativeAIEmbeddings (`text-embedding-004`)
- **Vector DB:** Chroma
- **LLM:** ChatGoogleGenerativeAI (`gemini-2.5-flash`)

### Web Arayüzü
- **Streamlit:** Interactive chat interface

---

## 🎓 Eğitim Materyalleri ile Uyum

Bu proje, Akbank GenAI Bootcamp eğitim materyallerinde anlatılan **RAG (Retrieval Augmented Generation)** prensiplerini **LangChain framework** ile uygular:

✅ **Retrieval (R):** LangChain Chroma retriever ile semantic search  
✅ **Augmentation (A):** Context injection ile LLM'e bilgi sağlama  
✅ **Generation (G):** ChatGoogleGenerativeAI ile doğal dil üretimi  
✅ **LCEL:** LangChain Expression Language ile chain oluşturma

### LangChain LCEL Chain Yapısı
```python
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
```

---

## 🚀 Kurulum ve Çalıştırma

### 1️⃣ Gereksinimler
- Python 3.9+
- Gemini API Key ([buradan alın](https://ai.google.dev/))

### 2️⃣ Sanal Ortam Oluştur
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# veya
.venv\Scripts\activate     # Windows
```

### 3️⃣ Bağımlılıkları Kur
```bash
pip install -r requirements.txt
```

### 4️⃣ API Key Ayarla
`.env.example` dosyasını `.env` olarak kopyalayın ve Gemini API key'inizi ekleyin:
```bash
cp .env.example .env
# .env dosyasını düzenleyin:
GEMINI_API_KEY=your_actual_api_key_here
```

### 5️⃣ Uygulamayı Başlat

**Web Arayüzü:**
```bash
streamlit run app_streamlit.py
```
Tarayıcınızda otomatik olarak `http://localhost:8501` açılacaktır.

**Not:** İlk soru sorulduğunda embedding oluşturulacağı için ~30-40 saniye sürebilir. Sonraki sorular 2-3 saniyede yanıtlanır.

---

## 💻 Web Arayüzü Özellikleri

- ✅ **Gerçek zamanlı chat** interface
- ✅ **Chat history** (oturum bazlı)
- ✅ **Örnek sorular** sidebar'da
- ✅ **Responsive design** (mobil uyumlu)

---

## � Demo

**Lokal:** `http://localhost:8501`

**Online:** *(Deploy tamamlandığında buraya eklenecek)*

---

## 👨‍💻 Geliştirici
Akbank GenAI Bootcamp Projesi - 2025
