# Jarvis AI - Hazır EXE Dosyası İndirme

## 🎯 EXE Nerede?

### Seçenek 1: GitHub Releases (Hazır - Önerilen)
```
📥 https://github.com/mrcode048/JAR/releases
```

**Dosyalar:**
- `JarvisAI-Standalone.exe` (300-500 MB) - Direkt çalıştırabilirsin
- `JarvisAI-Installer.exe` (250 MB) - Kurulum programı
- `JarvisAI.zip` (50 MB) - Kaynak kodu

---

### Seçenek 2: Kendi EXE'nizi Oluşturun (5-10 dakika)

#### Windows (Yönetici CMD)
```cmd
# 1. Depoyu klonla
git clone https://github.com/mrcode048/JAR.git
cd JAR

# 2. Bağımlılıkları yükle
pip install -r requirements.txt
pip install pyinstaller

# 3. EXE oluştur
python build_exe.py
```

**Çıktı:**
```
dist/
└── JarvisAI.exe  ✅ (300-500 MB)
```

#### Windows (Otomatik Script)
```cmd
# Direkt çalıştır
build_exe.bat
```

#### Linux/Mac
```bash
chmod +x build_exe.sh
./build_exe.sh
```

**Çıktı:**
```
dist/
└── JarvisAI  ✅ (Executable)
```

---

## 📥 EXE'yi Kullan

### Windows
```
1. dist/JarvisAI.exe'ye çift tıkla
2. API Keys'i gir (ilk kez)
3. Sohbet etmeye başla!
```

### Linux/Mac
```bash
chmod +x dist/JarvisAI
./dist/JarvisAI
```

---

## 📦 EXE Özellikleri

| Özellik | Durum |
|---------|-------|
| **Boyut** | 300-500 MB |
| **Platform** | Windows 7+ / Linux / Mac |
| **Python Gerekli** | ❌ Hayır |
| **Kurulum Gerekli** | ❌ Hayır (Portable) |
| **AI Modelleri** | ✅ Tümü (Claude, OpenAI, Gemini) |
| **Ses Tanıma** | ✅ Türkçe |
| **Donanım Kontrol** | ✅ Evet |
| **İnternet** | ✅ Sadece API calls |

---

## 🚀 HIZLI BAŞLANGIZ

### 1️⃣ GitHub'dan İndir
```
https://github.com/mrcode048/JAR/releases
JarvisAI-Standalone.exe dosyasını indir
```

### 2️⃣ Çalıştır
```
JarvisAI.exe → Çift tıkla
```

### 3️⃣ API Keys Ekle (İlk Kez)
```
Claude: https://console.anthropic.com
OpenAI: https://platform.openai.com/api/keys
Gemini: https://ai.google.dev
```

### 4️⃣ Sohbet Et!
```
"Merhaba, nasılsın?"
"Saat kaç?"
"Bilgisayarı kapat"
```

---

## 🔧 EXE Sorun Giderme

### EXE çalışmıyor
```
1. Windows Defender'ı kontrol et (SmartScreen)
   - Daha fazla bilgi → Yine de çalıştır
2. Antivirus'u devre dışı bırak (geçici)
3. Administrator olarak çalıştır (Sağ tıkla)
```

### "Python not found" hatası
```
Normal! EXE içerisinde Python vardır.
Bu hata görülmezse direkt çalışacak.
```

### EXE çok büyük (500+ MB)
```
Normal! Tüm AI modelleri + Python runtime + dependencies
İçeriyor. Boyutu azaltmak için:
- Transformers modelini kaldır
- Yalnızca Claude kullan
```

---

## 📊 EXE Oluşturma Zamanı

| İşlem | Zaman |
|-------|-------|
| İlk Derleme | 10-15 dakika |
| Sonraki Derleme | 5-10 dakika |
| İndirme | 5-30 dakika (hız'a bağlı) |

---

## 🎁 Bonus: Windows Installer

NSIS kullanarak kurulum programı oluştur:

```bash
# 1. NSIS yükle
https://nsis.sourceforge.io/

# 2. jarvis_installer.nsi çalıştır
makensis jarvis_installer.nsi

# 3. Çıktı
JarvisAI-Installer.exe ✅
```

---

## 📞 Linkler

| Kaynak | Link |
|--------|------|
| **GitHub Releases** | https://github.com/mrcode048/JAR/releases |
| **Source Code** | https://github.com/mrcode048/JAR |
| **Issues** | https://github.com/mrcode048/JAR/issues |

---

**EXE'yi indir ve Jarvis'i kullanmaya başla! 🚀**
