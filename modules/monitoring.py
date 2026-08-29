"""
Sistem İzleme - CPU, RAM, Disk Kullanımı
"""

import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)


class SystemMonitor:
    """Sistem İzleyicisi"""
    
    def __init__(self):
        logger.info("Sistem İzleyicisi başlatılıyor...")
        try:
            import psutil
            self.psutil = psutil
        except ImportError:
            logger.warning("psutil kütüphanesi yüklü değil")
            self.psutil = None
    
    def get_cpu_usage(self) -> float:
        """
        CPU kullanımını al
        
        Returns:
            CPU kullanımı yüzdesi
        """
        if not self.psutil:
            return 0.0
        return self.psutil.cpu_percent(interval=1)
    
    def get_memory_usage(self) -> Dict[str, float]:
        """
        RAM kullanımını al
        
        Returns:
            RAM kullanımı bilgileri
        """
        if not self.psutil:
            return {}
        
        mem = self.psutil.virtual_memory()
        return {
            'total': mem.total / (1024 ** 3),  # GB
            'used': mem.used / (1024 ** 3),
            'percent': mem.percent
        }
    
    def get_disk_usage(self, path: str = '/') -> Dict[str, float]:
        """
        Disk kullanımını al
        
        Args:
            path: Disk yolu
            
        Returns:
            Disk kullanımı bilgileri
        """
        if not self.psutil:
            return {}
        
        disk = self.psutil.disk_usage(path)
        return {
            'total': disk.total / (1024 ** 3),  # GB
            'used': disk.used / (1024 ** 3),
            'free': disk.free / (1024 ** 3),
            'percent': disk.percent
        }
    
    def get_all_stats(self) -> Dict[str, Any]:
        """
        Tüm sistem istatistiklerini al
        
        Returns:
            Sistem istatistikleri
        """
        return {
            'cpu': self.get_cpu_usage(),
            'memory': self.get_memory_usage(),
            'disk': self.get_disk_usage()
        }
