"""
Donanım Kontrolü - Sistem Komutları
"""

import logging
import os
import subprocess
import platform
from typing import Dict, Any

logger = logging.getLogger(__name__)


class HardwareController:
    """Donanım Kontrolcüsü"""
    
    def __init__(self):
        logger.info("Donanım Kontrolcüsü başlatılıyor...")
        self.system = platform.system()
    
    def execute_command(self, command: str) -> str:
        """
        Sistem komutu çalıştır
        
        Args:
            command: Çalıştırılacak komut
            
        Returns:
            Komut çıktısı
        """
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.stdout
        except Exception as e:
            logger.error(f"Komut çalıştırma hatası: {e}")
            return str(e)
    
    def get_system_info(self) -> Dict[str, Any]:
        """
        Sistem bilgilerini al
        
        Returns:
            Sistem bilgileri sözlüğü
        """
        try:
            import psutil
            return {
                'cpu_percent': psutil.cpu_percent(interval=1),
                'memory': psutil.virtual_memory()._asdict(),
                'disk': psutil.disk_usage('/')._asdict(),
                'platform': self.system
            }
        except ImportError:
            logger.warning("psutil kütüphanesi yüklü değil")
            return {'error': 'psutil yüklü değil'}
    
    def open_application(self, app_name: str):
        """
        Uygulama aç
        
        Args:
            app_name: Uygulama adı
        """
        try:
            if self.system == 'Windows':
                os.startfile(app_name)
            elif self.system == 'Darwin':  # macOS
                subprocess.run(['open', '-a', app_name])
            elif self.system == 'Linux':
                subprocess.Popen([app_name])
            
            logger.info(f"{app_name} açıldı")
        except Exception as e:
            logger.error(f"Uygulama açılamadı: {e}")
    
    def set_volume(self, level: int):
        """
        Ses seviyesini ayarla (0-100)
        
        Args:
            level: Ses seviyesi
        """
        level = max(0, min(100, level))  # 0-100 arasında sınırla
        
        try:
            if self.system == 'Windows':
                self.execute_command(f'nircmd.exe changesysvolume {level * 655}')
            elif self.system == 'Darwin':
                self.execute_command(f'osascript -e "set volume output volume {level}"')
            elif self.system == 'Linux':
                self.execute_command(f'amixer set Master {level}%')
            
            logger.info(f"Ses seviyesi {level}% olarak ayarlandı")
        except Exception as e:
            logger.error(f"Ses ayarı hatası: {e}")
    
    def cleanup(self):
        """Kaynakları kapat"""
        logger.info("Donanım kaynakları temizleniyor...")
