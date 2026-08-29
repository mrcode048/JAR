"""
Ses İşlemleri - Mikrofon Girişi ve Hoparlör Çıkışı
"""

import logging
from typing import Optional

logger = logging.getLogger(__name__)


class SpeechRecognition:
    """Ses Tanıma"""
    
    def __init__(self):
        logger.info("Ses Tanıma Engine başlatılıyor...")
        try:
            import speech_recognition as sr
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
        except ImportError:
            logger.warning("speech_recognition kütüphanesi yüklü değil")
            self.recognizer = None
            self.microphone = None
    
    def listen(self) -> Optional[str]:
        """
        Mikrofonda dinle ve metne dönüştür
        
        Returns:
            Tanınan metin veya None
        """
        if not self.recognizer:
            return None
        
        try:
            with self.microphone as source:
                logger.info("Dinleniyor...")
                audio = self.recognizer.listen(source, timeout=5)
            
            # Google Speech Recognition kullan
            text = self.recognizer.recognize_google(audio, language='tr-TR')
            return text
        
        except Exception as e:
            logger.error(f"Ses tanıma hatası: {e}")
            return None
    
    def close(self):
        """Kaynakları kapat"""
        pass


class TextToSpeech:
    """Metin Okuma"""
    
    def __init__(self):
        logger.info("Text-to-Speech Engine başlatılıyor...")
        try:
            import pyttsx3
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('volume', 0.9)
            
            # Türkçe sesini ayarla
            voices = self.engine.getProperty('voices')
            for voice in voices:
                if 'turkish' in voice.name.lower() or 'tr' in voice.languages:
                    self.engine.setProperty('voice', voice.id)
                    break
        except ImportError:
            logger.warning("pyttsx3 kütüphanesi yüklü değil")
            self.engine = None
    
    def speak(self, text: str):
        """
        Metni sese dönüştür ve oynat
        
        Args:
            text: Okutulacak metin
        """
        if not self.engine:
            logger.info(f"[TTS] {text}")
            return
        
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            logger.error(f"Metin okuma hatası: {e}")
