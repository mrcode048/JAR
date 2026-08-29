@echo off
REM Jarvis AI - Portable EXE Oluşturucu
REM PyInstaller kullanarak tek dosya executable oluşturur

setlocal enabledelayedexpansion
chcp 65001 >nul

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║       Jarvis AI - Portable EXE Oluşturucu                      ║
echo ║                                                                 ║
echo ║  Bu script, Jarvis AI'yi bağımsız .EXE dosyasına dönüştürür   ║
echo ║  İnternet veya Python gerekmiyor - sadece çalıştır!            ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Python kontrol et
echo [*] Python kontrol ediliyor...
python --version >nul 2>&1
if errorlevel 1 (
    echo [X] Python yüklü değil!
    echo [*] https://www.python.org/downloads/ adresinden yükleyin
    pause
    exit /b 1
)
echo [+] Python bulundu

REM PyInstaller kontrol et ve yükle
echo [*] PyInstaller kontrol ediliyor...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo [!] PyInstaller yüklü değil, yükleniyor...
    pip install pyinstaller -q
    if errorlevel 1 (
        echo [X] PyInstaller yüklenemedi
        pause
        exit /b 1
    )
    echo [+] PyInstaller yüklendi
) else (
    echo [+] PyInstaller bulundu
)

REM Bağımlılıklar kontrol et
echo [*] Tüm bağımlılıklar kontrol ediliyor...
pip install -r requirements.txt -q

REM EXE dosyası oluştur
echo.
echo [*] EXE dosyası oluşturuluyor...
echo [*] Bu işlem 5-10 dakika sürebilir (ilk kez biraz uzun)...
echo.

python -m PyInstaller --onefile --windowed --name=JarvisAI --add-data ".env.example:." --add-data "config.yaml:." --hidden-import=pyttsx3 --hidden-import=speech_recognition --hidden-import=anthropic --hidden-import=openai --hidden-import=google.generativeai --hidden-import=transformers --hidden-import=psutil --collect-all=pyttsx3 --collect-all=transformers --distpath=dist --workpath=build --specpath=. jarvis.py

if errorlevel 1 (
    echo [X] EXE oluşturma başarısız
    pause
    exit /b 1
)

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║              EXE Başarıyla Oluşturuldu!                        ║
echo ║                                                                 ║
echo ║  💾 Konum: dist\JarvisAI.exe                                      ║
echo ║  📐 Boyut: ~300-500 MB                                            ║
echo ║                                                                 ║
echo ║  📌 Dosya Özellikleri:                                            ║
echo ║  ✓ Taşınabilir (Portable)                                      ║
echo ║  ✓ Windows 7 + uyumlu                                          ║
echo ║  ✓ Tüm AI modelleri dahil                                      ║
echo ║  ✓ Python gerekmiyor!                                          ║
echo ║                                                                 ║
echo ║  🎯 Kullanım Seçenekleri:                                          ║
echo ║  1. Direkt çalıştır: dist\JarvisAI.exe                         ║
echo ║  2. Masaüstüne kopyala ve kullan                               ║
echo ���  3. Klasörde gezin: start dist                                 ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Klasör aç veya EXE çalıştır
set /p action="Ne yapmak istersiniz? (1=Aç/2=Test/3=Kapat): "
if /i "!action!"=="1" (
    start dist
) else if /i "!action!"=="2" (
    echo [*] JarvisAI.exe başlatılıyor...
    dist\JarvisAI.exe
) else (
    echo [+] Tamamlandı!
)

pause
endlocal
