"""
Jarvis AI - Standalone EXE Oluşturucu (Hızlı)
PyInstaller ile tek tıkla executable oluştur
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def main():
    print("\n" + "="*70)
    print("JARVIS AI - STANDALONE EXE OLUŞTURUCU")
    print("="*70 + "\n")
    
    # Adım 1: PyInstaller Yükle
    print("[1/4] PyInstaller yükleniyor...")
    subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller", "-q"], check=False)
    print("✓ PyInstaller hazır\n")
    
    # Adım 2: Bağımlılıkları Yükle
    print("[2/4] Bağımlılıklar yükleniyor...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "-q"], check=False)
    print("✓ Bağımlılıklar hazır\n")
    
    # Adım 3: Eski dosyaları temizle
    print("[3/4] Eski dosyalar temizleniyor...")
    shutil.rmtree("dist", ignore_errors=True)
    shutil.rmtree("build", ignore_errors=True)
    if Path("jarvis.spec").exists():
        Path("jarvis.spec").unlink()
    print("✓ Temizleme tamamlandı\n")
    
    # Adım 4: EXE Oluştur
    print("[4/4] EXE oluşturuluyor (5-10 dakika)...\n")
    
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--windowed",
        "--name=JarvisAI",
        "--icon=jarvis.ico" if Path("jarvis.ico").exists() else "",
        "--add-data=.env.example:.",
        "--add-data=config.yaml:.",
        "--hidden-import=pyttsx3",
        "--hidden-import=speech_recognition",
        "--hidden-import=anthropic",
        "--hidden-import=openai",
        "--hidden-import=google.generativeai",
        "--hidden-import=transformers",
        "--hidden-import=psutil",
        "--collect-all=pyttsx3",
        "--collect-all=transformers",
        "--distpath=dist",
        "--workpath=build",
        "jarvis.py"
    ]
    
    # Boş stringleri kaldır
    cmd = [c for c in cmd if c]
    
    result = subprocess.run(cmd)
    
    if result.returncode == 0:
        exe_path = Path("dist/JarvisAI.exe")
        if exe_path.exists():
            size_mb = exe_path.stat().st_size / (1024*1024)
            print("\n" + "="*70)
            print("✅ EXE BAŞARIYLA OLUŞTURULDU!")
            print("="*70)
            print(f"\n📁 Konum: {exe_path.absolute()}")
            print(f"📦 Boyut: {size_mb:.1f} MB")
            print(f"\n🚀 Kullanım: dist/JarvisAI.exe dosyasını çalıştır")
            print(f"\n💡 İpucu: Masaüstüne kopyala ve shortcut oluştur")
            print("="*70 + "\n")
            
            # EXE'yi çalıştır
            start = input("EXE'yi şimdi test etmek ister misiniz? (E/H): ").strip().lower()
            if start == "e":
                print("\n🚀 Jarvis başlatılıyor...\n")
                os.startfile(str(exe_path))
        else:
            print("\n❌ EXE dosyası oluşturulamadı!")
    else:
        print("\n❌ EXE oluşturma başarısız!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Hata: {e}")
        input("\nDevam etmek için Enter tuşuna basın...")
