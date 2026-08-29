"""
Jarvis AI Assistant - Ana Uygulama
Konuşan, dinleyen ve bilgisayarı kontrol edebilen AI asistanı
"""

import os
import sys
from pathlib import Path
import logging
from dotenv import load_dotenv

# Bağımlılıkları yükle
from core.ai_engine import AIEngine
from core.speech import SpeechRecognition, TextToSpeech
from core.hardware import HardwareController
from modules.commands import CommandProcessor
from modules.automation import TaskAutomation
from modules.monitoring import SystemMonitor

# Logging yapılandırma
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()


class Jarvis:
    """Jarvis AI Assistant Ana Sınıfı"""
    
    def __init__(self):
        logger.info("Jarvis başlatılıyor...")
        
        # Bileşenleri başlat
        self.ai_engine = AIEngine()
        self.speech_recognition = SpeechRecognition()
        self.text_to_speech = TextToSpeech()
        self.hardware = HardwareController()
        self.command_processor = CommandProcessor(self)
        self.task_automation = TaskAutomation()
        self.system_monitor = SystemMonitor()
        
        self.running = False
        logger.info("Jarvis hazır!")
    
    def greet(self):
        """Karşılama mesajı"""
        greeting = "Merhaba, ben Jarvis. Size nasıl yardımcı olabilirim?"
        self.text_to_speech.speak(greeting)
        logger.info(greeting)
    
    def listen(self):
        """Kullanıcının sesini dinle"""
        try:
            text = self.speech_recognition.listen()
            if text:
                logger.info(f"Kullanıcı: {text}")
                return text
        except Exception as e:
            logger.error(f"Dinleme hatası: {e}")
        return None
    
    def process_command(self, text):
        """Komutu işle ve cevap ver"""
        try:
            # AI motoru ile metin işle
            response = self.ai_engine.process(text)
            
            # Komutu işle
            self.command_processor.execute(text, response)
            
            # Cevabı söyle
            if response:
                self.text_to_speech.speak(response)
                logger.info(f"Jarvis: {response}")
            
            return response
        except Exception as e:
            logger.error(f"Komut işleme hatası: {e}")
            error_msg = "Maalesef bir hata oluştu. Lütfen tekrar deneyin."
            self.text_to_speech.speak(error_msg)
    
    def run(self):
        """Ana döngü"""
        self.running = True
        self.greet()
        
        logger.info("Dinleme modu başladı...")
        
        try:
            while self.running:
                # Ses dinle
                text = self.listen()
                
                if text:
                    # Çıkış komutu kontrolü
                    if text.lower() in ['çıkış', 'kapat', 'bye', 'exit']:
                        self.text_to_speech.speak("Hoşça kalın!")
                        break
                    
                    # Komutu işle
                    self.process_command(text)
        
        except KeyboardInterrupt:
            logger.info("Kullanıcı tarafından durduruldu")
            self.text_to_speech.speak("Kapatılıyor...")
        except Exception as e:
            logger.error(f"Beklenmeyen hata: {e}")
        finally:
            self.shutdown()
    
    def shutdown(self):
        """Uygulamayı kapat"""
        logger.info("Jarvis kapatılıyor...")
        self.running = False
        self.speech_recognition.close()
        self.hardware.cleanup()


def main():
    """Ana giriş noktası"""
    jarvis = Jarvis()
    jarvis.run()


if __name__ == "__main__":
    main()