# Jarvis AI - Kurulum Rehberi

## 🚀 Hızlı Başlangıç

### 1. Bağımlılıkları Yükle
```bash
pip install -r requirements.txt
```

### 2. API Anahtar larını Ekle
`.env.example` dosyasını `.env` olarak kopyala ve API anahtar larını ekle:

```bash
cp .env.example .env
```

Ardından `.env` dosyasını düzenle:
```
OPENAI_API_KEY=sk-xxx...
ANTHROPIC_API_KEY=sk-ant-xxx...
GOOGLE_API_KEY=xxx...
```

### 3. Jarvis'i Çalıştır
```bash
python jarvis.py
```

---

## 🤖 AI Modelleri ve API Anahtar ları

### 1. **Claude (Anthropic)** ⭐ Önerilen
- **Kayıt**: https://console.anthropic.com
- **En İyi**: Doğal konuşma, bağlam anlama
- **Fiyat**: Ücretsiz (ilk 5$ kredisi ücretsiz)

### 2. **OpenAI GPT**
- **Kayıt**: https://platform.openai.com
- **Model**: gpt-3.5-turbo
- **Fiyat**: Ücretsiz (ödeme-olarak-kazan)

### 3. **Google Gemini**
- **Kayıt**: https://ai.google.dev
- **Özellik**: Ücretsiz başlangıç
- **En İyi**: Hızlı cevaplar

### 4. **Hugging Face Transformers** ✅ Ücretsiz
- **Özellik**: Yerel çalışma, internet gerekmiyor
- **En İyi**: Gizlilik, hız
- **Model**: BERT, DistilBERT

---

## 📋 Desteklenen Komutlar

| Komut | Örnek | Sonuç |
|-------|--------|-------|
| Sohbet | "Merhaba, nasılsın?" | AI cevap verir |
| Saat | "Saat kaç?" | Saati söyler |
| Sistem | "RAM kullanımı nedir?" | Sistem bilgileri gösterir |
| Uygulama Açma | "Tarayıcı aç" | Uygulama açılır |
| Ses Kontrolü | "Sesi artır" | Ses seviyesi değişir |
| Kapatma | "Bilgisayarı kapat" | 30 saniye sonra kapatılır |

---

## 🔧 Ayarlar

`config.yaml` dosyasından:
- Ses hızı
- AI modeli seçimi
- Sistem izleme
- Görev otomasyonu

---

## ⚠️ Sorun Giderme

### API Anahtarı Hatası
```
OPENAI_API_KEY bulunmadı
→ .env dosyasını kontrol et ve API anahtarını ekle
```

### Ses Tanıma Çalışmıyor
```
pip install PyAudio
# Windows 7'de sorun yaşarsan:
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
```

### İnternet Bağlantısı Yok
→ Transformer modelini kullan (yerel)

---

## 📞 Destek

- GitHub: https://github.com/mrcode048/JAR
- Issues: Hataları rapor et
- Wiki: Detaylı dokümantasyon

---

## 📋 Lisans

MIT License - Özgürce kullan ve dağıt
