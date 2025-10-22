# Saç Ekimi Chatbot

Akbank Generative AI Bootcamp kapsamında geliştirilen RAG (Retrieval Augmented Generation) tabanlı bir soru-cevap sistemi.

## Genel Bakış

Bu proje, saç ekimi konusunda bilgi arayan kullanıcılara yardımcı olmak amacıyla geliştirilmiştir. Sistem, vektör tabanlı arama ve büyük dil modelleri kullanarak kullanıcı sorularına doğru ve bağlama uygun yanıtlar üretir.

## Proje Yapısı

```
chat_bot/
├── data/
│   └── sac_ekimi_veri_seti.py    # Veri seti (86 doküman)
├── src/
│   ├── __init__.py
│   ├── app.py                     # FastAPI backend
│   └── rag.py                     # RAG pipeline
├── app_streamlit.py               # Web arayüzü
├── requirements.txt
└── README.md
```

## Teknik Detaylar

### Veri Seti
Proje, çeşitli güvenilir kaynaklardan derlenen 86 adet soru-cevap çiftini içermektedir. Veri seti şu kategorileri kapsar:
- Temel bilgiler ve tanımlar
- FUE ve DHI yöntemleri
- Operasyon süreci
- Post-operatif bakım
- Yan etkiler ve riskler
- Fiyatlandırma

### Teknoloji Stack
**RAG Pipeline:**
- LangChain framework ile LCEL (LangChain Expression Language) implementasyonu
- Google Generative AI Embeddings (text-embedding-004)
- Chroma vektör veritabanı
- Gemini 2.5-flash dil modeli

**Uygulama:**
- Streamlit ile geliştirilmiş interaktif web arayüzü
- FastAPI backend desteği (opsiyonel)

### Mimari

Sistem, üç temel aşamadan oluşur:

1. **Retrieval (Bilgi Getirme):** Kullanıcı sorusu vektör uzayında aranır ve en ilgili dokümanlar bulunur
2. **Augmentation (Zenginleştirme):** Bulunan dokümanlar bağlam olarak dil modeline iletilir
3. **Generation (Üretim):** Dil modeli, bağlamı kullanarak kullanıcı sorusuna uygun yanıt üretir

```python
# LCEL chain yapısı
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
```

## Kurulum

### Gereksinimler
- Python 3.9 veya üzeri
- Gemini API anahtarı ([buradan edinilebilir](https://ai.google.dev/))

### Adımlar

1. Depoyu klonlayın:
```bash
git clone https://github.com/plnalaca/Chatbot-Akbank-GenAI-Bootcamp.git
cd Chatbot-Akbank-GenAI-Bootcamp
```

2. Sanal ortam oluşturun ve aktifleştirin:
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# Windows için: .venv\Scripts\activate
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

4. Ortam değişkenlerini ayarlayın:
```bash
cp .env.example .env
# .env dosyasını düzenleyerek API anahtarınızı ekleyin
```

5. Uygulamayı başlatın:
```bash
streamlit run app_streamlit.py
```

Uygulama `http://localhost:8501` adresinde çalışmaya başlayacaktır.

> **Not:** İlk sorgu sırasında vektör veritabanı oluşturulacağı için işlem 30-40 saniye sürebilir. Sonraki sorgular 2-3 saniye içinde yanıtlanır.

## Özellikler

- Gerçek zamanlı soru-cevap sistemi
- Oturum tabanlı sohbet geçmişi
- Hazır örnek sorular
- Responsive tasarım
- Türkçe dil desteği

## Demo

**Canlı Demo:** https://sac-ekimi-soru-cevap-chatbot.streamlit.app/

**Yerel:** http://localhost:8501

## Lisans

Bu proje Akbank GenAI Bootcamp eğitim programı kapsamında geliştirilmiştir.

## İletişim

Proje hakkında sorularınız için GitHub Issues bölümünü kullanabilirsiniz.
