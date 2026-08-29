"""
Ses İşlemleri - Mikrofon Giriş ve Hoparlör Çıkışı (Windows 7 Uyumlu)
"""

import logging
from typing import Optional

logger = logging.getLogger(__name__)


class SpeechRecognition:
    """Ses Tanıma (Windows 7 Uyumlu)"""
    
    def __init__(self):
        logger.info("Ses Tanıma Engine başlatılıyor...")
        self.recognizer = None
        self.microphone = None
        
        try:
            import speech_recognition as sr
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
            logger.info("Ses Tanıma başarıyla yüklendi")
        except ImportError:
            logger.warning("speech_recognition kütüphanesi yüklü değil")
            logger.info("Yüklemek için: pip install SpeechRecognition")
        except Exception as e:
            logger.error(f"Ses Tanıma yüklenirken hata: {e}")
    
    def listen(self, timeout: int = 5) -> Optional[str]:
        """
        Mikrofonda dinle ve metne dönüştür
        
        Args:
            timeout: Dinleme zaman aşımı (saniye)
            
        Returns:
            Tanınan metin veya None
        """
        if not self.recognizer or not self.microphone:
            logger.error("Ses Tanıma başlatılmadı")
            return None
        
        try:
            with self.microphone as source:
                logger.info("Dinleniyor...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=timeout)
            
            logger.info("Metin dönüştürülüyor...")
            
            # Google Speech Recognition - Türkçe
            try:
                text = self.recognizer.recognize_google(audio, language='tr-TR')
                logger.info(f"Tanınan: {text}")
                return text
            except:
                # İngilizce fallback
                try:
                    text = self.recognizer.recognize_google(audio, language='en-EN')
                    logger.info(f"Tanınan (EN): {text}")
                    return text
                except Exception as e:
                    logger.error(f"Google Speech Recognition hatası: {e}")
                    return None
        
        except Exception as e:
            logger.error(f"Ses tanıma hatası: {e}")
            return None
    
    def close(self):
        """Kaynakları kapat"""
        logger.info("Ses Tanıma kapatılıyor...")


class TextToSpeech:
    """Metin Okuma (Windows 7 Uyumlu)"""
    
    def __init__(self):
        logger.info("Text-to-Speech Engine başlatılıyor...")
        self.engine = None
        
        try:
            import pyttsx3
            self.engine = pyttsx3.init()
            
            # Ses özelliklerini ayarla
            self.engine.setProperty('rate', 150)  # Konuşma hızı
            self.engine.setProperty('volume', 0.9)  # Ses seviyesi
            
            # Türkçe ses ayarla
            voices = self.engine.getProperty('voices')
            for voice in voices:
                if 'turkish' in voice.name.lower() or 'tr-TR' in voice.id:
                    self.engine.setProperty('voice', voice.id)
                    logger.info(f"Türkçe ses kullanılıyor: {voice.name}")
                    break
            
            logger.info("Text-to-Speech başarıyla yüklendi")
        except ImportError:
            logger.warning("pyttsx3 kütüphanesi yüklü değil")
            logger.info("Yüklemek için: pip install pyttsx3")
        except Exception as e:
            logger.error(f"TTS yüklenirken hata: {e}")
    
    def speak(self, text: str):
        """
        Metni sese dönüştür ve oynat
        
        Args:
            text: Okutulacak metin
        """
        if not text:
            return
        
        if not self.engine:
            logger.info(f"[TTS] {text}")
            return
        
        try:
            logger.info(f"Konuşuluyor: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            logger.error(f"Metin okuma hatası: {e}")
    
    def set_voice_rate(self, rate: int):
        """
        Konuşma hızını ayarla (50-300)
        
        Args:
            rate: Hız değeri
        """
        if self.engine:
            rate = max(50, min(300, rate))
            self.engine.setProperty('rate', rate)
            logger.info(f"Konuşma hızı {rate} olarak ayarlandı")
    
    def set_volume(self, volume: float):
        """
        Ses seviyesini ayarla (0.0-1.0)
        
        Args:
            volume: Ses seviyesi
        """
        if self.engine:
            volume = max(0.0, min(1.0, volume))
            self.engine.setProperty('volume', volume)
            logger.info(f"TTS ses seviyesi {volume} olarak ayarlandı")
