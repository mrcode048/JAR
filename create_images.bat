@echo off
REM Jarvis AI - Görseller Oluşturucu
REM Logo, Banner ve Diyagramları oluştur

setlocal enabledelayedexpansion
chcp 65001 >nul

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║         Jarvis AI - Görseller Oluşturucu                        ║
echo ║     Logo, Banner, Diyagramlar ve İkonlar                       ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

echo [*] Pillow (PIL) kontrol ediliyor...
pip show pillow >nul 2>&1
if errorlevel 1 (
    echo [!] Pillow yüklü değil, yükleniyor...
    pip install pillow -q
)
echo [+] Pillow hazır
echo.

echo [*] Görseller oluşturuluyor...
echo.
python create_images.py

if errorlevel 1 (
    echo.
    echo ❌ Görseller oluşturulamadı!
    pause
    exit /b 1
)

echo.
echo [+] Tamamlandı! Görseller klasörde hazır.
echo.
pause
endlocal
