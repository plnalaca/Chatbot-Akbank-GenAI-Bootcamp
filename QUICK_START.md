# 🚀 Saç Ekimi Chatbot - Hızlı Başlangıç

## ✅ Servisler Aktif

### 1. FastAPI Backend
- **URL:** http://127.0.0.1:8000
- **Docs:** http://127.0.0.1:8000/docs
- **Health:** http://127.0.0.1:8000/health
- **Status:** ✅ Çalışıyor

### 2. Streamlit Web UI
- **Local URL:** http://localhost:8501
- **Network URL:** http://192.168.236.236:8501
- **Status:** ✅ Çalışıyor

---

## 🎯 Kullanım

### Web UI (Önerilen)
1. Tarayıcınızda **http://localhost:8501** adresini açın
2. Sol taraftaki örnek sorulardan birini seçin veya kendi sorunuzu yazın
3. Enter'a basın ve cevabı bekleyin

**⏱️ İlk Soru:** 30-40 saniye sürebilir (vectorstore ilk kez oluşturuluyor)  
**⏱️ Sonraki Sorular:** 2-3 saniye (cache'den çalışır)

### API Kullanımı
```bash
# Health check
curl http://127.0.0.1:8000/health

# Soru sorma
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"FUE yöntemi nedir?"}'
```

---

## 🧪 Test Soruları

Şu soruları deneyebilirsiniz:

### Temel Bilgiler
- "Saç ekimi nedir?"
- "Saç ekimi kimler için uygundur?"
- "Greft nedir?"

### Yöntemler
- "FUE yöntemi nedir?"
- "FUE yöntemi nasıl uygulanır?"

### Süreç
- "Saç ekiminden sonra ne zaman spor yapabilirim?"
- "Saç ekiminden sonra ne kadar dinlenmeliyim?"
- "Şok dökülme nedir?"

### Bakım
- "Saç ekiminden sonra jöle kullanılabilir mi?"
- "Ekilen saçlar kalıcı mı?"

---

## 🛠️ Servis Yönetimi

### Servisleri Durdurma
```bash
# Tüm servisleri durdur
pkill -f "uvicorn|streamlit"
```

### Servisleri Başlatma
```bash
# FastAPI
cd /Users/pelin/Desktop/chat_bot
.venv/bin/uvicorn src.app:app --host 127.0.0.1 --port 8000 &

# Streamlit
.venv/bin/streamlit run app_streamlit.py --server.headless=true --server.port=8501 &
```

### Logları İzleme
```bash
# Streamlit logları
tail -f /tmp/streamlit.log

# FastAPI logları
tail -f /tmp/uvicorn.log
```

---

## ⚠️ Bilinen Uyarılar

### LibreSSL Warning
```
NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+
```
**Etki:** Yok - Gemini API cloud-based olduğu için sorun yok  
**Çözüm:** Gerekli değil

### İlk Sorgu Yavaş
**Sebep:** Vectorstore ilk kez oluşturuluyor (86 doküman, batch processing)  
**Süre:** 30-40 saniye  
**Sonraki Sorgular:** 2-3 saniye (cached)

---

## 📊 Sistem Durumu

| Bileşen | Durum | URL |
|---------|-------|-----|
| FastAPI | ✅ Çalışıyor | http://127.0.0.1:8000 |
| Streamlit | ✅ Çalışıyor | http://localhost:8501 |
| LangChain RAG | ✅ Hazır | - |
| Chroma DB | ✅ Cache'de | - |
| Gemini API | ✅ Aktif | - |

---

## 🎉 Başlamak İçin

1. **Tarayıcınızı açın:** http://localhost:8501
2. **İlk soruyu sorun** (30-40 saniye bekleyin)
3. **Sonraki sorular** çok daha hızlı olacak
4. **Keyifle kullanın!** 💇

---

## 🆘 Sorun Giderme

### "Siteye ulaşılamıyor" hatası:
```bash
# Streamlit sürecini kontrol et
ps aux | grep streamlit

# Çalışmıyorsa yeniden başlat
.venv/bin/streamlit run app_streamlit.py --server.headless=true --server.port=8501 &
```

### "504 Deadline Exceeded" hatası:
- İlk sorguda normaldir (batch processing)
- 30-40 saniye bekleyin
- Retry mekanizması otomatik çalışacak

### "API çalışmıyor" hatası:
```bash
# Health check yap
curl http://127.0.0.1:8000/health

# Çalışmıyorsa yeniden başlat
.venv/bin/uvicorn src.app:app --host 127.0.0.1 --port 8000 &
```

---

**Hazırlayan:** Pelin Alaca 
**Proje:** Akbank GenAI Bootcamp 2025  
**Tarih:** 19 Ekim 2025
