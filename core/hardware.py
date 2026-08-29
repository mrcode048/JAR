"""
Donanım Kontrolü - Sistem Komutları (Windows 7 Uyumlu)
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
        
        # Windows 7 kontrolü
        if self.system == 'Windows':
            self.is_windows_7 = self._check_windows_7()
            logger.info(f"Windows 7 Uyumlu: {self.is_windows_7}")
    
    def _check_windows_7(self) -> bool:
        """Windows 7 kontrolü"""
        try:
            version = platform.release()
            return version == '7'
        except:
            return False
    
    def execute_command(self, command: str) -> str:
        """
        Sistem komutu çalıştır
        
        Args:
            command: Çalıştırılacak komut
            
        Returns:
            Komut çıktısı
        """
        try:
            result = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE
            )
            stdout, stderr = result.communicate(timeout=10)
            return stdout.decode('utf-8', errors='ignore')
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
                'disk': psutil.disk_usage('C:' if self.system == 'Windows' else '/')._asdict(),
                'platform': self.system,
                'processor': platform.processor(),
                'python_version': platform.python_version()
            }
        except ImportError:
            logger.warning("psutil kütüphanesi yüklü değil")
            return {'error': 'psutil yüklü değil'}
        except Exception as e:
            logger.error(f"Sistem bilgisi alma hatası: {e}")
            return {'error': str(e)}
    
    def open_application(self, app_name: str):
        """
        Uygulama aç (Windows 7 Uyumlu)
        
        Args:
            app_name: Uygulama adı veya yolu
        """
        try:
            if self.system == 'Windows':
                # Windows 7'de os.startfile kullan
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
        Windows 7 Uyumlu
        
        Args:
            level: Ses seviyesi
        """
        level = max(0, min(100, level))  # 0-100 arasında sınırla
        
        try:
            if self.system == 'Windows':
                # Windows 7 için nircmd kullan
                try:
                    self.execute_command(f'nircmd.exe changesysvolume {level * 655}')
                except:
                    # nircmd yoksa VB script kullan
                    vbs_code = f'''
Set objAudio = CreateObject("WMPlayer.OCX.7")
objAudio.settings.volume = {level}
'''
                    with open('temp_volume.vbs', 'w') as f:
                        f.write(vbs_code)
                    self.execute_command('temp_volume.vbs')
                    os.remove('temp_volume.vbs')
            
            logger.info(f"Ses seviyesi {level}% olarak ayarlandı")
        except Exception as e:
            logger.error(f"Ses ayarı hatası: {e}")
    
    def get_processes(self) -> list:
        """
        Çalışan işlemleri listele
        
        Returns:
            İşlem listesi
        """
        try:
            import psutil
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'status']):
                processes.append({
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'status': proc.info['status']
                })
            return processes
        except Exception as e:
            logger.error(f"İşlem listesi hatası: {e}")
            return []
    
    def kill_process(self, process_name: str):
        """
        İşlemi sonlandır
        
        Args:
            process_name: İşlem adı
        """
        try:
            if self.system == 'Windows':
                self.execute_command(f'taskkill /IM {process_name} /F')
            else:
                self.execute_command(f'killall {process_name}')
            
            logger.info(f"{process_name} sonlandırıldı")
        except Exception as e:
            logger.error(f"İşlem sonlandırma hatası: {e}")
    
    def shutdown_system(self, delay: int = 30):
        """
        Bilgisayarı kapat
        
        Args:
            delay: Kapatma gecikmesi (saniye)
        """
        try:
            if self.system == 'Windows':
                self.execute_command(f'shutdown /s /t {delay}')
            elif self.system == 'Darwin':
                self.execute_command('osascript -e "tell app \"System Events\" to shut down"')
            elif self.system == 'Linux':
                self.execute_command(f'sudo shutdown -h +{delay // 60}')
            
            logger.info(f"Bilgisayar {delay} saniye sonra kapatılacak")
        except Exception as e:
            logger.error(f"Kapatma hatası: {e}")
    
    def restart_system(self, delay: int = 30):
        """
        Bilgisayarı yeniden başlat
        
        Args:
            delay: Yeniden başlama gecikmesi (saniye)
        """
        try:
            if self.system == 'Windows':
                self.execute_command(f'shutdown /r /t {delay}')
            elif self.system == 'Darwin':
                self.execute_command('osascript -e "tell app \"System Events\" to restart"')
            elif self.system == 'Linux':
                self.execute_command(f'sudo shutdown -r +{delay // 60}')
            
            logger.info(f"Bilgisayar {delay} saniye sonra yeniden başlatılacak")
        except Exception as e:
            logger.error(f"Yeniden başlatma hatası: {e}")
    
    def cleanup(self):
        """Kaynakları kapat"""
        logger.info("Donanım kaynakları temizleniyor...")
