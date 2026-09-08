#!/bin/bash
# Jarvis AI - Görseller Oluşturucu
# Logo, Banner ve Diyagramları oluştur

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║         Jarvis AI - Görseller Oluşturucu                        ║"
echo "║     Logo, Banner, Diyagramlar ve İkonlar                       ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

echo "[*] Pillow (PIL) kontrol ediliyor..."
if ! pip3 show pillow &> /dev/null; then
    echo "[!] Pillow yüklü değil, yükleniyor..."
    pip3 install pillow -q
fi
echo "[+] Pillow hazır"
echo ""

echo "[*] Görseller oluşturuluyor..."
echo ""
python3 create_images.py

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Görseller oluşturulamadı!"
    exit 1
fi

echo ""
echo "[+] Tamamlandı! Görseller klasörde hazır."
echo ""
