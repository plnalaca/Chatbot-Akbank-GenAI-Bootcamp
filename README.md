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
│   └── rag.py                     # RAG pipeline (Gemini + Chroma)
├── notebooks/
│   ├── rag_demo.ipynb             # Jupyter notebook (RAG pipeline demo)
│   └── rag_comparison.ipynb       # Custom vs LangChain karşılaştırma
├── app_streamlit.py               # Streamlit web arayüzü
├── .env.example                   # API key şablonu
├── .env                           # API key (gitignore'da)
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

### RAG Pipeline (LangChain Implementation)
- **Framework:** LangChain + LCEL (LangChain Expression Language)
- **Embedding:** GoogleGenerativeAIEmbeddings (`text-embedding-004`)
- **Vector DB:** Chroma (via LangChain wrapper)
- **LLM:** ChatGoogleGenerativeAI (`gemini-2.5-flash`)
- **Chain:** LCEL-based RAG chain (retriever → format → prompt → LLM)

### Backend
- **FastAPI:** REST API
- **uvicorn:** ASGI server

### Frontend
- **Streamlit:** Web arayüzü

### Alternative Implementation
- **Custom RAG:** `src/rag_custom.py` (pure Python, no LangChain)
- Karşılaştırma için `notebooks/rag_comparison.ipynb` notebookuna bakın

---

## 🎓 Eğitim Materyalleri ile Uyum

Bu proje, Akbank GenAI Bootcamp eğitim materyallerinde anlatılan **RAG (Retrieval Augmented Generation)** prensiplerini **LangChain framework** ile uygular:

✅ **Retrieval (R):** LangChain Chroma retriever ile semantic search  
✅ **Augmentation (A):** Context injection ile LLM'e bilgi sağlama  
✅ **Generation (G):** ChatGoogleGenerativeAI ile doğal dil üretimi  
✅ **LCEL:** LangChain Expression Language ile chain oluşturma  
✅ **LangSmith Ready:** LangSmith entegrasyonu için hazır (API key eklenebilir)

### LangChain LCEL Chain Yapısı
```python
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
```

Bu yapı eğitim materyallerinde anlatılan iki aşamalı (two-step chain) yaklaşımını kullanır:
1. **Retrieval:** Her sorgu için otomatik olarak ilgili dokümanlar getirilir
2. **Generation:** Bulunan context ile tek bir LLM çağrısı yapılır

### Custom vs LangChain Yaklaşımı
Proje **LangChain implementation** kullanır. Eski custom implementation `src/rag_custom.py` dosyasında saklanmıştır.

| Özellik | Custom (Yedek) | LangChain (Aktif) |
|---------|-----------------|------------------------|
| Framework | Pure Python | LangChain + LCEL |
| Dependency | Az (5-6 lib) | Standart (10+ lib) |
| Kontrol | Tam kontrol | Framework abstraction |
| Monitoring | Manuel logging | LangSmith entegre |
| Bootcamp Uyumu | Fonksiyonel eşdeğer | **Tam uyumlu** ✅ |

**Sonuç:** LangChain implementation bootcamp eğitim materyalleriyle tam uyumlu ve production-ready.

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

**Seçenek A: Web Arayüzü (Önerilen)**
```bash
streamlit run app_streamlit.py
```
Tarayıcınızda otomatik olarak `http://localhost:8501` açılacaktır.

**Seçenek B: REST API**
```bash
uvicorn src.app:app --host 127.0.0.1 --port 8000 --reload
```
API dokümantasyonu: `http://127.0.0.1:8000/docs`

---

## 🧪 API Kullanımı

### Health Check
```bash
curl http://127.0.0.1:8000/health
# Response: {"status":"ok","service":"Saç Ekimi Chatbot"}
```

### Chat Endpoint
```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"Saç ekimi nedir?"}'
```

**Okunabilir Çıktı İçin:**
```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"FUE yöntemi nedir?"}' \
  | python3 -c "import sys, json; print(json.load(sys.stdin)['answer'])"
```

---

## 💻 Web Arayüzü Özellikleri

- ✅ **Gerçek zamanlı chat** interface
- ✅ **Chat history** (oturum bazlı)
- ✅ **Örnek sorular** sidebar'da
- ✅ **Markdown rendering** (zengin formatlı cevaplar)
- ✅ **Responsive design** (mobil uyumlu)
- ✅ **Hata yönetimi** ve kullanıcı bildirimleri

**Web Arayüzü Ekran Görüntüleri:**
- Sidebar: Örnek sorular, teknoloji bilgisi
- Ana ekran: Chat interface, mesaj geçmişi
- Input: Soru girişi, otomatik scroll

---

## 📈 Elde Edilen Sonuçlar

### ✅ Başarılı Test Sonuçları
- **86 doküman** üzerinde semantic search
- **Gemini 2.5-flash** ile Türkçe, profesyonel yanıtlar
- **Context-aware responses** (sadece bildiği bilgiyi söylüyor)
- **Hallucination-free** (bilmediği sorularda dürüst)

### 🎯 Test Örnekleri
| Soru | Sonuç |
|------|-------|
| "Saç ekimi nedir?" | ✅ Detaylı, doğru açıklama |
| "FUE yöntemi nedir?" | ✅ Teknik bilgi, avantajlar |
| "Operasyon sonrası spor?" | ✅ Zaman çizelgesi, tavsiyeler |
| "DHI vs FUE farkı?" | ✅ FUE bilgisi verdi, DHI eksik olduğunu belirtti |

### 📊 Performans
- **Embedding:** ~30-40 saniye (ilk yükleme, 86 doküman)
- **Query latency:** ~2-3 saniye (retrieval + generation)
- **Accuracy:** Yüksek (veri seti kalitesine bağlı)

---

## 📓 Jupyter Notebook Demo

Projeye dahil edilen notebook'lar RAG pipeline'ın detaylarını interaktif olarak gösterir:

### 1. `notebooks/rag_demo.ipynb` - RAG Pipeline Demo
**İçerik:**
1. 📊 Veri Seti Analizi ve Görselleştirme
2. 🔢 Embedding Oluşturma (Gemini API)
3. 📦 Vector Store (ChromaDB)
4. 🔍 Semantic Search (Retrieval)
5. 🤖 Cevap Üretimi (Gemini 2.5-flash)
6. ⚡ Performans Analizi ve Karşılaştırma

### 2. `notebooks/rag_comparison.ipynb` - Implementation Karşılaştırması
**İçerik:**
1. 🔧 Custom Implementation (Mevcut Proje)
2. 🦜 LangChain Implementation (Alternatif)
3. 🆚 Performans ve Kod Karşılaştırması
4. 📊 Benchmark Sonuçları

**Çalıştırma:**
```bash
jupyter notebook notebooks/rag_demo.ipynb
# veya VS Code'da direkt açın
```

**Not:** `rag_comparison.ipynb` için LangChain kütüphaneleri gerekir (requirements.txt'de opsiyonel olarak listelendi).

---

## 🌐 Web Arayüzü

**Lokal Erişim:** `http://localhost:8501`

**Kullanım:**
1. Tarayıcınızda `http://localhost:8501` adresini açın
2. Sol sidebar'dan örnek soruları tıklayın veya kendi sorunuzu yazın
3. Enter'a basın veya "Gönder" butonuna tıklayın
4. Chatbot size RAG pipeline ile yanıt verecek

**Not:** İlk soru sorulduğunda embedding ve Chroma koleksiyonu oluşturulacağı için ~30-40 saniye sürebilir. Sonraki sorular daha hızlı olacaktır.

---

## 🌐 Deploy Linki
*(Deploy tamamlandığında buraya eklenecek)*

---

## 📝 Geliştirme Notları

### RAG Pipeline Akışı
1. **Kullanıcı sorusu** → `/chat` endpoint'ine POST isteği
2. **Embedding:** Soru sentence-transformers ile vektörize edilir
3. **Retrieval:** Chroma'da semantic search (top-3 benzer doküman)
4. **Generation:** Gemini API'ye context + soru gönderilir
5. **Yanıt:** Türkçe, bağlama uygun cevap döner

### Geliştirme Önerileri
- [x] Streamlit web arayüzü ekle
- [x] Jupyter notebook demo
- [x] LangChain karşılaştırması
- [ ] LangSmith monitoring entegrasyonu
- [ ] Chat history/session yönetimi (database)
- [ ] Docker containerization
- [ ] Deploy (Render/Railway/HuggingFace Spaces)
- [ ] Text chunking strategy (uzun dokümanlar için)
- [ ] RAG Agents (multi-step reasoning)

---

## 👨‍💻 Geliştirici
Akbank GenAI Bootcamp Projesi - 2025
