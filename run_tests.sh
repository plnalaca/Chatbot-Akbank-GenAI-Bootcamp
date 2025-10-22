#!/bin/bash

# Saç Ekimi Chatbot - Otomatik Test Script
# Akbank GenAI Bootcamp Projesi

echo "🧪 Saç Ekimi Chatbot Test Script"
echo "=================================="
echo ""

# Renk kodları
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test sayacı
PASSED=0
FAILED=0

# Yardımcı fonksiyon: Test sonucunu göster
test_result() {
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓${NC} $1"
        ((PASSED++))
    else
        echo -e "${RED}✗${NC} $1"
        ((FAILED++))
    fi
}

echo "1️⃣  Python Environment Kontrolü"
echo "--------------------------------"
python3 --version
test_result "Python versiyonu"

if [ -d ".venv" ]; then
    echo -e "${GREEN}✓${NC} Virtual environment bulundu"
    source .venv/bin/activate
    ((PASSED++))
else
    echo -e "${RED}✗${NC} Virtual environment bulunamadı"
    echo -e "${YELLOW}ℹ${NC}  Lütfen 'python3 -m venv .venv' komutunu çalıştırın"
    ((FAILED++))
    exit 1
fi

echo ""
echo "2️⃣  Environment Variables Kontrolü"
echo "--------------------------------"
if [ -f ".env" ]; then
    echo -e "${GREEN}✓${NC} .env dosyası bulundu"
    ((PASSED++))
    
    if grep -q "GEMINI_API_KEY=" .env; then
        echo -e "${GREEN}✓${NC} GEMINI_API_KEY tanımlı"
        ((PASSED++))
    else
        echo -e "${RED}✗${NC} GEMINI_API_KEY bulunamadı"
        ((FAILED++))
    fi
else
    echo -e "${RED}✗${NC} .env dosyası bulunamadı"
    echo -e "${YELLOW}ℹ${NC}  Lütfen '.env.example' dosyasını '.env' olarak kopyalayın"
    ((FAILED++))
fi

echo ""
echo "3️⃣  Dependencies Kontrolü"
echo "--------------------------------"
pip list | grep -q "langchain"
test_result "langchain"

pip list | grep -q "langchain-google-genai"
test_result "langchain-google-genai"

pip list | grep -q "langchain-chroma"
test_result "langchain-chroma"

pip list | grep -q "fastapi"
test_result "fastapi"

pip list | grep -q "streamlit"
test_result "streamlit"

echo ""
echo "4️⃣  Veri Seti Kontrolü"
echo "--------------------------------"
python3 -c "from data.sac_ekimi_veri_seti import documents; print(f'Doküman sayısı: {len(documents)}')" 2>/dev/null
test_result "Veri seti yükleme"

echo ""
echo "5️⃣  RAG Pipeline Testi"
echo "--------------------------------"
python3 -c "
from src.rag import load_documents_from_data, convert_to_langchain_documents
docs = load_documents_from_data()
lc_docs = convert_to_langchain_documents(docs)
print(f'LangChain dönüşümü: {len(lc_docs)} doküman')
" 2>/dev/null
test_result "LangChain document dönüşümü"

echo ""
echo "6️⃣  Embedding ve Vector Store Testi"
echo "--------------------------------"
echo -e "${YELLOW}⚠${NC}  Bu test 30-40 saniye sürebilir (batch processing)..."
python3 -c "
from src.rag import build_or_get_vectorstore
try:
    vectorstore = build_or_get_vectorstore()
    print('Vector store başarıyla oluşturuldu/yüklendi')
except Exception as e:
    print(f'Hata: {e}')
    exit(1)
" 2>/dev/null
test_result "Vector Store (Chroma)"

echo ""
echo "7️⃣  RAG Chain Testi"
echo "--------------------------------"
python3 -c "
from src.rag import build_or_get_rag_chain
try:
    chain = build_or_get_rag_chain()
    print('RAG chain başarıyla oluşturuldu')
except Exception as e:
    print(f'Hata: {e}')
    exit(1)
" 2>/dev/null
test_result "RAG Chain (LCEL)"

echo ""
echo "8️⃣  End-to-End Query Testi"
echo "--------------------------------"
echo -e "${YELLOW}⚠${NC}  Gerçek bir soru soruyorum (2-3 saniye sürebilir)..."
python3 -c "
from src.rag import retrieve_and_answer
try:
    answer = retrieve_and_answer('FUE yöntemi nedir?')
    print('Soru: FUE yöntemi nedir?')
    print(f'Yanıt uzunluğu: {len(answer)} karakter')
    print('İlk 200 karakter:', answer[:200])
except Exception as e:
    print(f'Hata: {e}')
    exit(1)
" 2>/dev/null
test_result "End-to-End Query"

echo ""
echo "9️⃣  FastAPI Health Check"
echo "--------------------------------"
echo -e "${YELLOW}ℹ${NC}  FastAPI'nin çalıştığından emin olun (uvicorn src.app:app)"
echo -e "${YELLOW}ℹ${NC}  Test ediliyor: http://127.0.0.1:8000/health"

# FastAPI'nin çalışıp çalışmadığını kontrol et
HEALTH_CHECK=$(curl -s http://127.0.0.1:8000/health 2>/dev/null)
if echo "$HEALTH_CHECK" | grep -q "ok"; then
    echo -e "${GREEN}✓${NC} FastAPI health check başarılı"
    echo "Yanıt: $HEALTH_CHECK"
    ((PASSED++))
else
    echo -e "${YELLOW}⚠${NC}  FastAPI çalışmıyor (manuel test gerekebilir)"
    echo -e "${YELLOW}ℹ${NC}  Başlatmak için: uvicorn src.app:app --reload"
    # Burası fail sayılmasın
fi

echo ""
echo "🔟  Streamlit Kontrolü"
echo "--------------------------------"
echo -e "${YELLOW}ℹ${NC}  Streamlit'in çalıştığından emin olun (streamlit run app_streamlit.py)"
echo -e "${YELLOW}ℹ${NC}  Test ediliyor: http://localhost:8501"

STREAMLIT_CHECK=$(curl -s -I http://localhost:8501 2>/dev/null | head -1)
if echo "$STREAMLIT_CHECK" | grep -q "200"; then
    echo -e "${GREEN}✓${NC} Streamlit erişilebilir"
    echo "Yanıt: $STREAMLIT_CHECK"
    ((PASSED++))
else
    echo -e "${YELLOW}⚠${NC}  Streamlit çalışmıyor (manuel test gerekebilir)"
    echo -e "${YELLOW}ℹ${NC}  Başlatmak için: streamlit run app_streamlit.py"
    # Burası fail sayılmasın
fi

echo ""
echo "=================================="
echo "📊 TEST SONUÇLARI"
echo "=================================="
echo -e "Başarılı: ${GREEN}$PASSED${NC}"
echo -e "Başarısız: ${RED}$FAILED${NC}"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✅ TÜM TESTLER BAŞARILI!${NC}"
    echo ""
    echo "Sistem production-ready durumda."
    echo ""
    echo "📝 Sonraki Adımlar:"
    echo "  1. FastAPI başlat: uvicorn src.app:app --reload"
    echo "  2. Streamlit başlat: streamlit run app_streamlit.py"
    echo "  3. Tarayıcıda aç: http://localhost:8501"
    exit 0
else
    echo -e "${RED}❌ BAZI TESTLER BAŞARISIZ${NC}"
    echo ""
    echo "Lütfen yukarıdaki hataları gözden geçirin."
    exit 1
fi
