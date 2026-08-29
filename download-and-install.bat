@echo off
REM Jarvis AI - Otomatik İndirme ve Kurulum Scripti
REM Windows 7+ Uyumlu
REM Kullanım: download-and-install.bat

setlocal enabledelayedexpansion
chcp 65001 >nul

echo.
echo ╔══════════════════════════════════════════════════════════════║
echo ║         Jarvis AI - Otomatik İndirme ve Kurulum               ║
echo ║              Yapay Zeka Asistan Sistemi                        ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

REM Klasör kontrol et
if exist "JAR" (
    echo [!] JAR klasörü zaten mevcut
    set /p override="Üzerine yazmak ister misiniz? (E/H): "
    if /i not "!override!"=="E" (
        echo [X] İşlem iptal edildi
        pause
        exit /b 0
    )
    echo [*] Mevcut JAR klasörü siliniyor...
    rmdir /s /q JAR >nul 2>&1
)

REM Git kontrol et
echo [*] Git kontrol ediliyor...
git --version >nul 2>&1
if errorlevel 1 (
    echo [!] Git yüklü değil
    echo [*] Git indiriliyor: https://git-scm.com/download/win
    start https://git-scm.com/download/win
    echo [X] Git yükledikten sonra scripti tekrar çalıştırın
    pause
    exit /b 1
)
echo [+] Git bulundu

REM Repository klonla
echo [*] Jarvis AI repository klonlanıyor...
echo [*] GitHub'dan indiriliyor: https://github.com/mrcode048/JAR.git
git clone https://github.com/mrcode048/JAR.git JAR

if errorlevel 1 (
    echo [X] Klonlama başarısız
    echo [*] İnternet bağlantınızı kontrol edin
    pause
    exit /b 1
)
echo [+] Repository başarıyla klonlandı

REM JAR klasörüne gir
cd JAR

REM Python kontrol et
echo.
echo [*] Python kontrol ediliyor...
python --version >nul 2>&1
if errorlevel 1 (
    echo [!] Python 3.7+ yüklü değil
    echo [*] Python indiriliyor: https://www.python.org/downloads/
    start https://www.python.org/downloads/
    echo [X] Python yükledikten sonra scripti tekrar çalıştırın
    echo [!] Kurulumda "Add Python to PATH" seçeneğini işaretleyin!
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VER=%%i
echo [+] %PYTHON_VER% bulundu

REM pip güncelle
echo [*] pip güncelleniyorr...
python -m pip install --upgrade pip -q
echo [+] pip güncellendy

REM Bağımlılıkları yükle
echo.
echo [*] Paketler yükleniyor (Bu biraz zaman alabilir)...
echo [*] OpenAI, Anthropic Claude, Google Gemini, Transformers...
pip install -r requirements.txt

if errorlevel 1 (
    echo [X] Paket yüklemesi başarısız
    echo [*] Lütfen aşağıdaki komutları elle çalıştırın:
    echo     pip install --upgrade pip
    echo     pip install -r requirements.txt
    pause
    exit /b 1
)
echo [+] Tüm paketler başarıyla yüklendi

REM .env dosyası oluştur
echo.
echo [*] Konfigürasyon dosyası oluşturuluyor...
if not exist .env (
    copy .env.example .env >nul
    echo [+] .env dosyası oluşturuldu
) else (
    echo [!] .env dosyası zaten mevcut
)

REM .env'yi aç
echo [*] Lütfen .env dosyasını açıp API anahtar larını ekleyin
echo [*] Gerekli API anahtar ları:
echo     - ANTHROPIC_API_KEY (https://console.anthropic.com)
echo     - OPENAI_API_KEY (https://platform.openai.com/api/keys)
echo     - GOOGLE_API_KEY (https://ai.google.dev)
echo.
set /p edit="API anahtar larını şimdi eklemek ister misiniz? (E/H): "
if /i "!edit!"=="E" (
    start notepad .env
    echo [*] Notepad açılıyor, API anahtar larını ekleyin ve kaydedin
    pause
)

REM Kurulum tamamlandı
echo.
echo ╔══════════════════════════════════════════════════════════════║
echo ║              Kurulum Tamamlandı!                               ║
echo ║                                                                 ║
echo ║  Jarvis AI şu konumda:                                         ║
echo ║  %cd%                       ║
echo ║                                                                 ║
echo ║  Başlatmak için:                                               ║
echo ║  python jarvis.py                                              ║
echo ║                                                                 ║
echo ║  Veya şu komutu çalıştırın:                                    ║
echo ║  python -m jarvis.py                                           ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

set /p launch="Jarvis'i şimdi başlatmak ister misiniz? (E/H): "
if /i "!launch!"=="E" (
    echo [*] Jarvis başlatılıyor...
    python jarvis.py
) else (
    echo [+] Kurulum tamamlandı!
    echo [*] Daha sonra başlatmak için: python jarvis.py
    pause
)

endlocal
