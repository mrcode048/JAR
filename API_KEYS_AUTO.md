# Jarvis AI - API Keys Otomatik Yükleme

## 🔑 Desteklenen API Servisleri

### 1. Anthropic Claude
- **Kayıt**: https://console.anthropic.com
- **Ücretsiz Kredi**: $5
- **En İyi**: Türkçe destek, doğal konuşma

### 2. OpenAI GPT
- **Kayıt**: https://platform.openai.com/api/keys
- **Model**: gpt-3.5-turbo
- **Ödeme**: Pay-as-you-go

### 3. Google Gemini
- **Kayıt**: https://ai.google.dev
- **Ücretsiz**: Evet
- **Limit**: 60 requests/minute

---

## 🚀 Otomatik API Keys Ekleme

### Seçenek 1: Setup Scripti (Önerilen)

#### Windows (CMD - Yönetici)
```cmd
python setup_api_keys.py
```

#### Linux/Mac (Terminal)
```bash
python3 setup_api_keys.py
```

**Script şu işlemleri yapar:**
- API anahtarlarını sorar
- Doğrulama yapar
- .env dosyasına otomatik ekler
- Test bağlantısı yapar

---

### Seçenek 2: Environment Variables

#### Windows (PowerShell - Yönetici)
```powershell
# Sistem ortamına ekle
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "sk-ant-xxx...", "User")
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "sk-xxx...", "User")
[Environment]::SetEnvironmentVariable("GOOGLE_API_KEY", "xxx...", "User")

# Jarvis'i başlat
python jarvis.py
```

#### Linux/Mac (Bash)
```bash
export ANTHROPIC_API_KEY="sk-ant-xxx..."
export OPENAI_API_KEY="sk-xxx..."
export GOOGLE_API_KEY="xxx..."

python3 jarvis.py
```

---

### Seçenek 3: .env Dosyasına Elle Yazma

```bash
# 1. .env dosyasını aç
notepad .env          # Windows
nano .env             # Linux/Mac

# 2. Aşağıdakileri ekle
ANTHROPIC_API_KEY=sk-ant-xxx...
OPENAI_API_KEY=sk-xxx...
GOOGLE_API_KEY=xxx...
AI_MODE=claude

# 3. Kaydet ve Jarvis'i çalıştır
python jarvis.py
```

---

## 📋 API Keys Nasıl Alınır?

### Claude API Key (5 Dakika)
```
1. https://console.anthropic.com adresine git
2. "Sign In" veya "Sign Up" tıkla
3. Email doğrulaması yap
4. "API Keys" bölümüne git
5. "Create New Secret Key" tıkla
6. Kopyala: sk-ant-...
7. .env dosyasına yapıştır
```

### OpenAI API Key (10 Dakika)
```
1. https://platform.openai.com/api/keys adresine git
2. Hesap oluştur veya giriş yap
3. "Create new secret key" tıkla
4. Kopyala: sk-...
5. .env dosyasına yapıştır
6. Kredi kartı ekle (ödeme için)
```

### Google Gemini API Key (2 Dakika)
```
1. https://ai.google.dev adresine git
2. "Get API Key" tıkla
3. Google hesabıyla giriş yap
4. Kopyala
5. .env dosyasına yapıştır
```

---

## ✅ Doğrulama

```bash
# API Keys test et
python test_api_keys.py
```

**Çıktı:**
```
[+] Claude: ✓ Bağlandı
[+] OpenAI: ✓ Bağlandı
[+] Gemini: ✓ Bağlandı
[+] Transformers: ✓ Hazır (Yerel)

Seçilen AI: claude
```

---

## 🔒 Güvenlik Notları

⚠️ **API Keys'i Paylaşma!**
- Hiçbir zaman GitHub'a commit etme
- `.env` dosyasını `.gitignore`'a ekle (zaten eklendi)
- Hassas işlemler için API keys'ı rotate et
- Maksimum kullanım limitlerini belirle

✅ **Güvenli Yöntemler:**
- Sistem environment variables kullan
- Azure Key Vault / AWS Secrets Manager kullan
- Ayrı bir `.env.local` dosyası oluştur

---

## 🚨 Sorun Giderme

### "Invalid API Key"
```
1. API key'i doğru kopyaladığını kontrol et
2. Boş alanlara dikkat et (copy/paste)
3. API key'i yenile (console'dan)
4. Rate limit kontrol et
```

### "Connection Error"
```
1. İnternet bağlantısını kontrol et
2. Firewall ayarlarını kontrol et
3. VPN kullanıyorsan devre dışı bırak
4. API service'in durumunu kontrol et
```

### "Quota Exceeded"
```
1. API kullanım limitini kontrol et
2. İstek sayısını azalt
3. Başka bir AI modeline geç
4. Ödeme planını yükselt
```

---

## 💰 Fiyatlandırma

| AI | Ücretsiz | Başlangıç | Not |
|----|----|-------|---|
| **Claude** | $5 kredi | $1+ | Ay başında reset |
| **OpenAI** | Ödeme gerekli | $0.0005/req | Pay-as-you-go |
| **Gemini** | Evet | $0 | 60 req/min |
| **Transformers** | Evet | $0 | Yerel (sınırsız) |

---

## 🎯 Önerilen Setup

```bash
# En ekonomik (Ücretsiz)
AI_MODE=gemini    # + Transformers fallback

# En iyi Türkçe
AI_MODE=claude    # + OpenAI fallback

# Hibrirt (En Güvenli)
AI_MODE=claude
FALLBACK_API=openai
FALLBACK_API_2=gemini
```

---

## 📞 Hızlı Linkler

| Hizmet | Link |
|--------|------|
| **Claude** | https://console.anthropic.com |
| **OpenAI** | https://platform.openai.com |
| **Gemini** | https://ai.google.dev |
| **Status** | https://status.anthropic.com |

---

**Jarvis hazır! API Keys'i ekle ve sohbet etmeye başla! 🚀**
