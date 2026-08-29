# Jarvis AI Assistant

Jarvis, donanım entegrasyonu ile bilgisayarı kontrol edebilen, konuşan ve dinleyen, tam özellikli bir yapay zeka asistanıdır.

## Özellikler

- 🎤 **Ses Tanıma**: Konuşmayı metne dönüştürme
- 🔊 **Ses Sentezi**: Metin okuma (TTS)
- 🖥️ **Donanım Kontrolü**: Sistem komutları, uygulama yönetimi
- 🧠 **AI Motor**: Doğal dil işleme
- 🎯 **Görev Otomasyonu**: Zamanlanmış görevler
- 📊 **Sistem İzleme**: CPU, RAM, Disk kullanımı

## Gereksinimler

- Python 3.10+
- Windows 10+ / macOS 10.15+ / Linux
- Mikrofon ve Hoparlör

## Kurulum

```bash
pip install -r requirements.txt
```

## Hızlı Başlangıç

```bash
python jarvis.py
```

## Proje Yapısı

```
├── jarvis.py              # Ana uygulama
├── core/
│   ├── ai_engine.py       # NLP ve AI motor
│   ├── speech.py          # Ses işlemleri
│   └── hardware.py        # Donanım kontrolü
├── modules/
│   ├── commands.py        # Komut işleyicisi
│   ├── automation.py      # Görev otomasyonu
│   └── monitoring.py      # Sistem izleme
├── config.yaml            # Konfigürasyon
└── requirements.txt       # Bağımlılıklar
```

## Lisans

MIT License