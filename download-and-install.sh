#!/bin/bash
# Jarvis AI - Otomatik İndirme ve Kurulum Scripti
# Linux/Mac Uyumlu
# Kullanım: bash download-and-install.sh

set -e

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║         Jarvis AI - Otomatik İndirme ve Kurulum               ║"
echo "║              Yapay Zeka Asistan Sistemi                        ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Klasör kontrol et
if [ -d "JAR" ]; then
    echo "[!] JAR klasörü zaten mevcut"
    read -p "Üzerine yazmak ister misiniz? (e/h): " override
    if [ "$override" != "e" ]; then
        echo "[X] İşlem iptal edildi"
        exit 0
    fi
    echo "[*] Mevcut JAR klasörü siliniyor..."
    rm -rf JAR
fi

# Git kontrol et
echo "[*] Git kontrol ediliyor..."
if ! command -v git &> /dev/null; then
    echo "[!] Git yüklü değil"
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "[*] Lütfen yükleyin: brew install git"
    else
        echo "[*] Lütfen yükleyin: sudo apt-get install git"
    fi
    exit 1
fi
echo "[+] Git bulundu"

# Repository klonla
echo "[*] Jarvis AI repository klonlanıyor..."
echo "[*] GitHub'dan indiriliyor: https://github.com/mrcode048/JAR.git"
git clone https://github.com/mrcode048/JAR.git JAR

if [ $? -ne 0 ]; then
    echo "[X] Klonlama başarısız"
    echo "[*] İnternet bağlantınızı kontrol edin"
    exit 1
fi
echo "[+] Repository başarıyla klonlandı"

# JAR klasörüne gir
cd JAR

# Python kontrol et
echo ""
echo "[*] Python kontrol ediliyor..."
if ! command -v python3 &> /dev/null; then
    echo "[!] Python 3.7+ yüklü değil"
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "[*] Lütfen yükleyin: brew install python3"
    else
        echo "[*] Lütfen yükleyin: sudo apt-get install python3 python3-pip"
    fi
    exit 1
fi

PYTHON_VER=$(python3 --version)
echo "[+] $PYTHON_VER bulundu"

# pip güncelle
echo "[*] pip güncelleniyor..."
python3 -m pip install --upgrade pip -q
echo "[+] pip güncellendi"

# Bağımlılıkları yükle
echo ""
echo "[*] Paketler yükleniyor (Bu biraz zaman alabilir)..."
echo "[*] OpenAI, Anthropic Claude, Google Gemini, Transformers..."

if ! pip3 install -r requirements.txt; then
    echo "[X] Paket yüklemesi başarısız"
    echo "[*] Lütfen aşağıdaki komutları elle çalıştırın:"
    echo "    python3 -m pip install --upgrade pip"
    echo "    pip3 install -r requirements.txt"
    exit 1
fi
echo "[+] Tüm paketler başarıyla yüklendi"

# .env dosyası oluştur
echo ""
echo "[*] Konfigürasyon dosyası oluşturuluyor..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "[+] .env dosyası oluşturuldu"
else
    echo "[!] .env dosyası zaten mevcut"
fi

# .env'yi düzenle
echo "[*] Lütfen .env dosyasını açıp API anahtarlarını ekleyin"
echo "[*] Gerekli API anahtarları:"
echo "    - ANTHROPIC_API_KEY (https://console.anthropic.com)"
echo "    - OPENAI_API_KEY (https://platform.openai.com/api/keys)"
echo "    - GOOGLE_API_KEY (https://ai.google.dev)"
echo ""
read -p "API anahtarlarını şimdi eklemek ister misiniz? (e/h): " edit
if [ "$edit" = "e" ]; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
        open -a TextEdit .env
    else
        nano .env || vi .env
    fi
fi

# Kurulum tamamlandı
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║              Kurulum Tamamlandı!                               ║"
echo "║                                                                 ║"
echo "║  Jarvis AI şu konumda:                                         ║"
echo "║  $(pwd)                                     ║"
echo "║                                                                 ║"
echo "║  Başlatmak için:                                               ║"
echo "║  python3 jarvis.py                                             ║"
echo "║                                                                 ║"
echo "║  Veya:                                                         ║"
echo "║  ./jarvis.py (eğer çalıştırılabilir ise)                       ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

read -p "Jarvis'i şimdi başlatmak ister misiniz? (e/h): " launch
if [ "$launch" = "e" ]; then
    echo "[*] Jarvis başlatılıyor..."
    python3 jarvis.py
else
    echo "[+] Kurulum tamamlandı!"
    echo "[*] Daha sonra başlatmak için: python3 jarvis.py"
fi
