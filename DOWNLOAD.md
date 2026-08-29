# Jarvis AI - İndir ve Kur

## 🚀 Hızlı İndirme

### Windows 7 İçin Paket
```
📦 Jarvis-AI-v1.0-Windows7.zip
Boyut: ~250MB
SHA256: (checksum burada)
```

**[📥 Direkt İndir (GitHub Releases)](https://github.com/mrcode048/JAR/releases/download/v1.0/Jarvis-AI-v1.0-Windows7.zip)**

---

## 📋 İndirme Seçenekleri

### 1. **GitHub Desktop Klonu** (Önerilen)
```bash
git clone https://github.com/mrcode048/JAR.git
cd JAR
```

### 2. **ZIP İndir**
- [Ana branch ZIP](https://github.com/mrcode048/JAR/archive/refs/heads/main.zip)
- Paketi çıkart: `JAR-main.zip`

### 3. **GitHub CLI**
```bash
gh repo clone mrcode048/JAR
cd JAR
```

---

## 💾 Kurulum Sonrası

### Windows 7 Adımlar

```bash
# 1. Python 3.7+ yükle (Eğer yoksa)
# İndir: https://www.python.org/downloads/windows/

# 2. Klasöre git
cd C:\Users\YourName\Downloads\JAR

# 3. Bağımlılıkları yükle
pip install -r requirements.txt

# 4. .env dosyası oluştur
copy .env.example .env

# 5. API anahtarlarını ekle
# .env dosyasını metin editörü ile aç
# ANTHROPIC_API_KEY=sk-ant-xxx...
# OPENAI_API_KEY=sk-xxx...
# GOOGLE_API_KEY=xxx...

# 6. Çalıştır
python jarvis.py
```

---

## 📊 Paket İçeriği

```
JAR/
├── jarvis.py              # Ana uygulama
├── requirements.txt       # Python paketleri
├── .env.example          # API ayarları şablonu
├── SETUP.md              # Kurulum rehberi
├── README.md             # Proje açıklaması
├── config.yaml           # Konfigürasyon
│
├── core/
│   ├── ai_engine.py      # AI Motor (Claude, OpenAI, Gemini)
│   ├── speech.py         # Ses Tanıma & TTS
│   └── hardware.py       # Donanım Kontrolü
│
├── modules/
│   ├── commands.py       # Komut İşleyici
│   ├── automation.py     # Görev Otomasyonu
│   └── monitoring.py     # Sistem İzleme
│
└── docs/
    ├── INSTALL.md        # Yükleme rehberi
    ├── API_KEYS.md       # API anahtarları
    └── TROUBLESHOOT.md   # Sorun giderme
```

---

## 🔧 Sistem Gereksinimleri

| Gereklilik | Minimum | Önerilen |
|-----------|---------|----------|
| **OS** | Windows 7 SP1 | Windows 10+ |
| **Python** | 3.7 | 3.9+ |
| **RAM** | 2 GB | 4+ GB |
| **Disk** | 500 MB | 1+ GB |
| **Mikrofon** | Gerekli | USB Mikrofon |

---

## ⚠️ Sorun Yaşarsan

### Python Yüklü Değil Hatası
```
'python' is not recognized as an internal or external command
```
**Çözüm**: 
- Python yükle: https://www.python.org/downloads/
- Kurulumda "Add Python to PATH" seç

### Paket Yükleme Hatası
```
pip: command not found
```
**Çözüm**:
```bash
# Python kurulu mu kontrol et
python --version

# pip güncelle
python -m pip install --upgrade pip
```

### Ses Tanıma Çalışmıyor
```bash
# PyAudio Windows 7 için:
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
# Uygun .whl dosyasını indir ve yükle:
pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl
```

---

## 📞 Yardım & Destek

- **Issues**: https://github.com/mrcode048/JAR/issues
- **Discussions**: https://github.com/mrcode048/JAR/discussions
- **Wiki**: https://github.com/mrcode048/JAR/wiki

---

## 📜 Lisans

MIT License - Özgürce kullan ve paylaş

---

## ✨ Sürüm Geçmişi

### v1.0 (2026-08-29)
✅ Tüm AI modelleri entegre (Claude, OpenAI, Gemini)
✅ Windows 7 uyumlu
✅ Türkçe ses tanıma & metin okuma
✅ Donanım kontrolleri
✅ Sistem izleme

---

**Sorular? Issues'de sor: https://github.com/mrcode048/JAR/issues**