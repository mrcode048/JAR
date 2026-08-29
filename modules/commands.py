"""
Komut İşleyicisi - Kullanıcı Komutlarını İşleme
"""

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from jarvis import Jarvis

logger = logging.getLogger(__name__)


class CommandProcessor:
    """Komut İşleyicisi"""
    
    def __init__(self, jarvis: 'Jarvis'):
        self.jarvis = jarvis
        logger.info("Komut İşleyicisi başlatıldı")
    
    def execute(self, text: str, response: str):
        """
        Komutu çalıştır
        
        Args:
            text: Orijinal komut metni
            response: AI tarafından üretilen cevap
        """
        text_lower = text.lower()
        
        # Saati söyle
        if any(word in text_lower for word in ['saat', 'zaman', 'saati']):
            self._handle_time()
        
        # Sistem bilgilerini göster
        elif any(word in text_lower for word in ['sistem', 'bilgisayar', 'bilgi', 'ram', 'cpu']):
            self._handle_system_info()
        
        # Ses kontrolü
        elif 'ses' in text_lower:
            self._handle_volume(text_lower)
        
        # Uygulama aç
        elif 'aç' in text_lower or 'başlat' in text_lower:
            self._handle_open_app(text_lower)
        
        # Kapatma komutu
        elif 'kapat' in text_lower and 'bilgisayar' in text_lower:
            self._handle_shutdown()
    
    def _handle_time(self):
        """Saati işle"""
        from datetime import datetime
        now = datetime.now()
        time_str = now.strftime('%H:%M')
        logger.info(f"Şu anda saat {time_str}")
    
    def _handle_system_info(self):
        """Sistem bilgilerini işle"""
        info = self.jarvis.hardware.get_system_info()
        if 'error' not in info:
            cpu = info.get('cpu_percent', 0)
            memory = info.get('memory', {}).get('percent', 0)
            logger.info(f"CPU: {cpu}%, Bellek: {memory}%")
    
    def _handle_volume(self, text: str):
        """Ses kontrolü işle"""
        if 'artır' in text or 'yukarı' in text:
            self.jarvis.hardware.set_volume(75)
        elif 'azalt' in text or 'aşağı' in text:
            self.jarvis.hardware.set_volume(25)
        elif 'kapat' in text or 'sesiz' in text:
            self.jarvis.hardware.set_volume(0)
    
    def _handle_open_app(self, text: str):
        """Uygulama açma işle"""
        logger.info("Uygulama açılıyor...")
        # Uygulama adını çıkart ve aç
    
    def _handle_shutdown(self):
        """Kapatma işle"""
        logger.info("Bilgisayar kapatılıyor...")
        self.jarvis.hardware.execute_command('shutdown /s /t 30')
