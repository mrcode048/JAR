"""
Jarvis AI - Portable EXE Oluşturucu
PyInstaller ile tek dosya executable'ı oluşturur
"""

import os
import subprocess
import sys
import shutil
from pathlib import Path

def create_portable_exe():
    """Portable EXE dosyası oluştur"""
    
    print("=" * 70)
    print("Jarvis AI - Portable EXE Oluşturucu")
    print("=" * 70)
    print()
    
    # PyInstaller yüklü mü kontrol et
    print("[*] PyInstaller kontrol ediliyor...")
    try:
        import PyInstaller
        print("[+] PyInstaller bulundu")
    except ImportError:
        print("[!] PyInstaller yüklü değil, yükleniyor...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("[+] PyInstaller yüklendi")
    
    # Output dizini temizle
    output_dir = Path("dist")
    if output_dir.exists():
        print("[*] Eski derleme dosyaları siliniyor...")
        shutil.rmtree(output_dir)
        shutil.rmtree(Path("build"), ignore_errors=True)
        if Path("jarvis.spec").exists():
            Path("jarvis.spec").unlink()
    
    # PyInstaller komutu
    print()
    print("[*] EXE dosyası oluşturuluyor...")
    print("    Bu işlem 5-10 dakika sürebilir...")
    print()
    
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",                          # Tek dosya
        "--windowed",                         # GUI modu (konsol penceresi yok)
        "--icon=jarvis.ico",                  # Icon (varsa)
        "--name=JarvisAI",                    # Çıktı adı
        "--add-data=.env.example:.",          # .env dosyasını ekle
        "--add-data=config.yaml:.",           # config dosyasını ekle
        "--hidden-import=pyttsx3",            # Hidden imports
        "--hidden-import=speech_recognition",
        "--hidden-import=anthropic",
        "--hidden-import=openai",
        "--hidden-import=google.generativeai",
        "--hidden-import=transformers",
        "--hidden-import=psutil",
        "--collect-all=pyttsx3",              # Tüm pyttsx3 dosyalarını topla
        "--collect-all=transformers",         # Tüm transformers dosyalarını topla
        "--distpath=dist",                    # Çıktı dizini
        "--workpath=build",
        "--specpath=.",
        "jarvis.py"
    ]
    
    try:
        subprocess.check_call(cmd)
        print()
        print("[+] EXE başarıyla oluşturuldu!")
        print()
        print("=" * 70)
        print("Konum: dist/JarvisAI.exe")
        print("Boyut: ~300-500MB")
        print("=" * 70)
        print()
        
        # Kurulum scriptini oluştur
        create_installer()
        
    except subprocess.CalledProcessError as e:
        print(f"[X] EXE oluşturma başarısız: {e}")
        sys.exit(1)


def create_installer():
    """NSIS kurulum programı oluştur"""
    
    print("[*] Windows kurulum programı (Installer) oluşturuluyor...")
    
    nsis_script = r"""
; Jarvis AI - NSIS Installer Scripti
!include "MUI2.nsh"
!include "x64.nsh"

; Tanımlar
!define PRODUCT_NAME "Jarvis AI"
!define PRODUCT_VERSION "1.0"
!define PRODUCT_PUBLISHER "mrcode048"
!define PRODUCT_WEB_SITE "https://github.com/mrcode048/JAR"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\JarvisAI.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"

; Kurulum klasörü
InstallDir "$PROGRAMFILES\JarvisAI"

; Tema
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_LANGUAGE "Turkish"

; Installer bilgileri
Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "JarvisAI-Installer.exe"
ShowInstDetails show
ShowUnInstDetails show

Section "Jarvis AI" SEC01
  SetOutPath "$INSTDIR"
  File "dist\JarvisAI.exe"
  File ".env.example"
  File "README.md"
  File "SETUP.md"
  
  ; Başlat menüsüne kısa yol ekle
  CreateDirectory "$SMPROGRAMS\JarvisAI"
  CreateShortCut "$SMPROGRAMS\JarvisAI\JarvisAI.lnk" "$INSTDIR\JarvisAI.exe"
  CreateShortCut "$SMPROGRAMS\JarvisAI\Kaldır.lnk" "$INSTDIR\uninst.exe"
  
  ; Masaüstüne kısa yol ekle
  CreateShortCut "$DESKTOP\JarvisAI.lnk" "$INSTDIR\JarvisAI.exe"
SectionEnd

Section "Uninstall"
  RMDir /r "$INSTDIR"
  RMDir /r "$SMPROGRAMS\JarvisAI"
  Delete "$DESKTOP\JarvisAI.lnk"
SectionEnd
"""
    
    nsis_path = Path("jarvis_installer.nsi")
    with open(nsis_path, "w", encoding="utf-8") as f:
        f.write(nsis_script)
    
    print("[+] NSIS scripti oluşturuldu: jarvis_installer.nsi")
    print()
    print("NOT: NSIS Installer'ı oluşturmak için:")
    print("1. NSIS yükleyin: https://nsis.sourceforge.io/")
    print("2. Şu komutu çalıştırın: makensis jarvis_installer.nsi")
    print()


if __name__ == "__main__":
    create_portable_exe()
