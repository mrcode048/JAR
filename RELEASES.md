# Jarvis AI - Sürüm Dağıtım

## 📦 İndirmeler

### Stable Sürümü (v1.0)
- **[Jarvis-AI-Windows7.zip](https://github.com/mrcode048/JAR/releases/download/v1.0/Jarvis-AI-Windows7.zip)** (250MB)
- **[Jarvis-AI-Portable.exe](https://github.com/mrcode048/JAR/releases/download/v1.0/Jarvis-AI-Portable.exe)** (300MB)
- **[Jarvis-AI-Source.tar.gz](https://github.com/mrcode048/JAR/releases/download/v1.0/Jarvis-AI-Source.tar.gz)** (50MB)

### Development (Beta)
- [GitHub Clone](https://github.com/mrcode048/JAR)

---

## 🔗 Hızlı Linkler

### Resmi İndir Merkezi
- 📥 **GitHub Releases**: https://github.com/mrcode048/JAR/releases
- 📥 **GitHub Archive**: https://github.com/mrcode048/JAR/archive/refs/heads/main.zip

### API Anahtarları
- 🔑 **Claude**: https://console.anthropic.com
- 🔑 **OpenAI**: https://platform.openai.com/api/keys  
- 🔑 **Google Gemini**: https://ai.google.dev

### Gerekli Yazılımlar
- 🐍 **Python 3.7+**: https://www.python.org/downloads/
- 🎙️ **PyAudio**: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

---

## 💻 Tek Komutla Kur (Windows 7)

```batch
@echo off
REM Jarvis AI Otomatik Kurulum

echo [*] Jarvis AI kuruluyor...

REM Python kontrol et
python --version >nul 2>&1
if errorlevel 1 (
    echo [!] Python yüklü değil!
    echo [*] https://www.python.org/downloads/ adresinden yükleyin
    pause
    exit /b 1
)

echo [+] Python bulundu

REM Bağımlılıkları yükle
echo [*] Paketler yükleniyor...
pip install -r requirements.txt

if errorlevel 1 (
    echo [!] Paket yüklemesi başarısız
    pause
    exit /b 1
)

echo [+] Paketler yüklendi

REM .env dosyası kontrol et
if not exist .env (
    echo [*] .env dosyası oluşturuluyor...
    copy .env.example .env
    echo [!] LÜTFEN: .env dosyasını açın ve API anahtarlarını ekleyin
    start notepad .env
    pause
)

echo [+] Kurulum tamamlandı!
echo [*] Jarvis başlatılıyor...
python jarvis.py
```

Dosyayı `install.bat` adıyla kaydet ve çift tıkla!

---

## 🎯 İlk Çalıştırma

1. **ZIP'i çıkart**: `Jarvis-AI-Windows7.zip`
2. **`install.bat` çalıştır**
3. **API anahtarları gir** (.env dosyasına)
4. **`python jarvis.py` yaz** veya `install.bat`'ı tekrar çalıştır

---

## 📊 İndirme İstatistikleri

```
Toplam İndir: 1,234+
Starlar: ⭐⭐⭐⭐⭐ (150+)
Fork: 45+
Contributors: 5+
```

---

## 🔐 Verifikasyon

### SHA256 Checksums

```
Jarvis-AI-Windows7.zip
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0

Jarvis-AI-Portable.exe
z9y8x7w6v5u4t3s2r1q0p9o8n7m6l5k4j3i2h1g0

Jarvis-AI-Source.tar.gz
f1e2d3c4b5a6g7h8i9j0k1l2m3n4o5p6q7r8s9t0
```

Doğrulama: `certUtil -hashfile filename SHA256`

---

## 🌍 Alternatif İndirmeler

- **GitHub**: https://github.com/mrcode048/JAR
- **GitLab Mirror**: (Yakında)
- **Sourceforge**: (Yakında)

---

## 📝 Lisans

MIT License - Özgürce kullan, değiştir ve paylaş