"""
Jarvis AI - Logo ve Görseller Oluşturucu
PIL (Pillow) ile profesyonel görseller oluştur
"""

import os
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

def create_logo():
    """Jarvis AI Logo oluştur"""
    print("[*] Logo oluşturuluyor...")
    
    # 512x512 Logo
    img = Image.new('RGBA', (512, 512), (10, 25, 47, 255))  # Koyu mavi
    draw = ImageDraw.Draw(img)
    
    # Daire
    draw.ellipse([50, 50, 462, 462], outline=(100, 200, 255, 255), width=8)
    draw.ellipse([100, 100, 412, 412], outline=(100, 200, 255, 255), width=4)
    
    # J harfi (Jarvis)
    draw.text((180, 180), "J", fill=(100, 200, 255, 255), font=None)
    
    # Yapay Zeka Simgesi (Beyin)
    draw.arc([150, 150, 362, 362], 0, 360, fill=(100, 200, 255, 255), width=6)
    draw.ellipse([220, 200, 292, 272], fill=(100, 200, 255, 100))
    
    img.save('jarvis_logo.png')
    print("✓ Logo kaydedildi: jarvis_logo.png")
    
    # 256x256 Sürüm
    img_small = img.resize((256, 256), Image.Resampling.LANCZOS)
    img_small.save('jarvis_logo_256.png')
    print("✓ Küçük Logo: jarvis_logo_256.png")
    
    # 128x128 Icon
    img_icon = img.resize((128, 128), Image.Resampling.LANCZOS)
    img_icon.save('jarvis_icon.png')
    print("✓ Icon: jarvis_icon.png")
    
    # ICO Dosyası (Windows)
    img_ico = img.resize((256, 256), Image.Resampling.LANCZOS)
    img_ico.save('jarvis.ico')
    print("✓ Windows Icon: jarvis.ico")

def create_banner():
    """Proje Banner oluştur"""
    print("\n[*] Banner oluşturuluyor...")
    
    # 1200x400 Banner
    img = Image.new('RGB', (1200, 400), (10, 25, 47))  # Koyu mavi
    draw = ImageDraw.Draw(img)
    
    # Gradient benzeri dikdörtgenler
    for i in range(0, 400, 50):
        color = (int(10 + i*0.1), int(25 + i*0.15), int(47 + i*0.2))
        draw.rectangle([0, i, 1200, i+50], fill=color)
    
    # Başlık
    draw.text((100, 80), "JARVIS AI", fill=(100, 200, 255), font=None)
    draw.text((100, 180), "Turkish AI Assistant", fill=(200, 200, 200), font=None)
    
    img.save('jarvis_banner.png')
    print("✓ Banner kaydedildi: jarvis_banner.png")

def create_features_image():
    """Özellikler Görseli oluştur"""
    print("\n[*] Özellikler görseli oluşturuluyor...")
    
    # 800x600 Özellikler
    img = Image.new('RGB', (800, 600), (15, 30, 50))
    draw = ImageDraw.Draw(img)
    
    # Başlık
    draw.text((50, 30), "JARVIS AI - FEATURES", fill=(100, 200, 255), font=None)
    
    # Özellikler Listesi
    features = [
        "🤖 4 AI Models (Claude, OpenAI, Gemini)",
        "🎤 Turkish Voice Recognition",
        "🔊 Text to Speech (TTS)",
        "🖥️ Hardware Control",
        "📊 System Monitoring",
        "🎯 Command Automation",
        "⚡ 300-500 MB Portable EXE",
        "💻 Windows 7+, Linux, Mac",
    ]
    
    y = 100
    for feature in features:
        draw.text((70, y), feature, fill=(200, 200, 200), font=None)
        y += 50
    
    img.save('jarvis_features.png')
    print("✓ Özellikler: jarvis_features.png")

def create_flowchart():
    """Akış Diyagramı oluştur"""
    print("\n[*] Akış diyagramı oluşturuluyor...")
    
    # 1000x700 Akış Diyagramı
    img = Image.new('RGB', (1000, 700), (20, 35, 60))
    draw = ImageDraw.Draw(img)
    
    # Başlık
    draw.text((300, 20), "JARVIS AI - WORKFLOW", fill=(100, 200, 255), font=None)
    
    # Kutular ve Oklar
    boxes = [
        (150, 100, 350, 150, "INPUT\nVoice/Text"),
        (400, 100, 600, 150, "RECOGNITION\nSpeech-to-Text"),
        (650, 100, 850, 150, "PROCESSING\nCommand Identify"),
        (150, 300, 350, 350, "AI ENGINE\n4 Models"),
        (400, 300, 600, 350, "RESPONSE\nGeneration"),
        (650, 300, 850, 350, "OUTPUT\nText-to-Speech"),
        (150, 500, 850, 550, "HARDWARE/SYSTEM CONTROL"),
    ]
    
    for x1, y1, x2, y2, text in boxes:
        draw.rectangle([x1, y1, x2, y2], outline=(100, 200, 255), width=2)
        draw.text((x1+20, y1+15), text, fill=(200, 200, 200), font=None)
    
    img.save('jarvis_flowchart.png')
    print("✓ Akış Diyagramı: jarvis_flowchart.png")

def create_architecture():
    """Mimari Diyagram oluştur"""
    print("\n[*] Mimari diyagram oluşturuluyor...")
    
    # 1000x800 Mimari
    img = Image.new('RGB', (1000, 800), (20, 35, 60))
    draw = ImageDraw.Draw(img)
    
    # Başlık
    draw.text((250, 20), "JARVIS AI - ARCHITECTURE", fill=(100, 200, 255), font=None)
    
    # Katmanlar
    layers = [
        (100, 100, 900, 150, "USER INTERFACE (Voice/Text)", (100, 200, 255)),
        (100, 180, 900, 230, "SPEECH RECOGNITION LAYER", (150, 200, 255)),
        (100, 260, 450, 380, "AI MODELS\nClaude | OpenAI", (100, 200, 255)),
        (500, 260, 900, 380, "AI MODELS\nGemini | Transformers", (100, 200, 255)),
        (100, 410, 900, 460, "COMMAND PROCESSOR & ROUTER", (150, 200, 255)),
        (100, 490, 450, 620, "SYSTEM MODULE\nHardware Control", (100, 200, 255)),
        (500, 490, 900, 620, "AUTOMATION MODULE\nSchedules & Tasks", (100, 200, 255)),
        (100, 650, 900, 700, "OUTPUT (TTS & Display)", (100, 200, 255)),
    ]
    
    for x1, y1, x2, y2, text, color in layers:
        draw.rectangle([x1, y1, x2, y2], outline=color, width=2)
        draw.text((x1+20, y1+15), text, fill=(200, 200, 200), font=None)
    
    img.save('jarvis_architecture.png')
    print("✓ Mimari Diyagram: jarvis_architecture.png")

def create_readme_header():
    """README için Header oluştur"""
    print("\n[*] README Header oluşturuluyor...")
    
    # 1200x300 Header
    img = Image.new('RGB', (1200, 300), (10, 25, 47))
    draw = ImageDraw.Draw(img)
    
    # Başlık
    draw.text((150, 50), "JARVIS AI", fill=(100, 200, 255), font=None)
    draw.text((150, 130), "Turkish AI Assistant with Voice Recognition", fill=(200, 200, 200), font=None)
    draw.text((150, 180), "🎤 Voice | 🤖 AI | 🖥️ Hardware | 💻 Python", fill=(100, 200, 255), font=None)
    draw.text((150, 230), "⭐ GitHub | 🚀 Production Ready | 📜 MIT License", fill=(200, 200, 200), font=None)
    
    img.save('jarvis_readme_header.png')
    print("✓ README Header: jarvis_readme_header.png")

def create_comparison_table():
    """Karşılaştırma Tablosu Görseli"""
    print("\n[*] Karşılaştırma tablosu oluşturuluyor...")
    
    # 1000x600 Tablo
    img = Image.new('RGB', (1000, 600), (20, 35, 60))
    draw = ImageDraw.Draw(img)
    
    # Başlık
    draw.text((250, 20), "AI MODELS COMPARISON", fill=(100, 200, 255), font=None)
    
    # Tablo Başlığı
    headers = ["Model", "Cost", "Speed", "Quality", "Offline"]
    col_widths = [150, 150, 150, 200, 150]
    x = 50
    y = 80
    
    for i, header in enumerate(headers):
        draw.rectangle([x, y, x+col_widths[i], y+50], outline=(100, 200, 255), width=2)
        draw.text((x+20, y+15), header, fill=(100, 200, 255), font=None)
        x += col_widths[i]
    
    # Satırlar
    models = [
        ("Claude", "$", "Medium", "Excellent", "No"),
        ("OpenAI", "$$", "Fast", "Good", "No"),
        ("Gemini", "Free", "Very Fast", "Good", "No"),
        ("Transformers", "Free", "Slow", "Fair", "Yes"),
    ]
    
    y = 130
    for model_data in models:
        x = 50
        for i, cell in enumerate(model_data):
            draw.rectangle([x, y, x+col_widths[i], y+50], outline=(100, 200, 255), width=1)
            draw.text((x+20, y+15), cell, fill=(200, 200, 200), font=None)
            x += col_widths[i]
        y += 50
    
    img.save('jarvis_comparison.png')
    print("✓ Karşılaştırma: jarvis_comparison.png")

def main():
    print()
    print("╔" + "═"*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + "Jarvis AI - Görseller Oluşturucu".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "═"*68 + "╝")
    print()
    
    try:
        create_logo()
        create_banner()
        create_features_image()
        create_flowchart()
        create_architecture()
        create_readme_header()
        create_comparison_table()
        
        print()
        print("╔" + "═"*68 + "╗")
        print("║" + " "*68 + "║")
        print("║" + "✅ Tüm Görseller Başarıyla Oluşturuldu!".center(68) + "║")
        print("║" + " "*68 + "║")
        print("║" + "Dosyalar:".center(68) + "║")
        print("║" + "- jarvis_logo.png (512x512)".center(68) + "║")
        print("║" + "- jarvis_logo_256.png (256x256)".center(68) + "║")
        print("║" + "- jarvis_icon.png (128x128)".center(68) + "║")
        print("║" + "- jarvis.ico (Windows)".center(68) + "║")
        print("║" + "- jarvis_banner.png".center(68) + "║")
        print("║" + "- jarvis_features.png".center(68) + "║")
        print("║" + "- jarvis_flowchart.png".center(68) + "║")
        print("║" + "- jarvis_architecture.png".center(68) + "║")
        print("║" + "- jarvis_readme_header.png".center(68) + "║")
        print("║" + "- jarvis_comparison.png".center(68) + "║")
        print("║" + " "*68 + "║")
        print("╚" + "═"*68 + "╝")
        print()
        
    except Exception as e:
        print(f"\n❌ Hata: {e}")
        print("\n💡 Pillow yüklemeyi dene: pip install Pillow")

if __name__ == "__main__":
    main()
