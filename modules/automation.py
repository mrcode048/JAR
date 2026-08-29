"""
Görev Otomasyonu - Zamanlanmış Görevler
"""

import logging
import schedule
import threading
from typing import Callable, Dict, List
from datetime import datetime, time

logger = logging.getLogger(__name__)


class TaskAutomation:
    """Görev Otomasyonu"""
    
    def __init__(self):
        logger.info("Görev Otomasyonu başlatılıyor...")
        self.tasks: Dict[str, Dict] = {}
        self.scheduler_thread = None
        self.running = False
    
    def schedule_task(self, name: str, func: Callable, time_str: str):
        """
        Zamanlanmış görev oluştur
        
        Args:
            name: Görev adı
            func: Çalıştırılacak fonksiyon
            time_str: Zaman (HH:MM formatında)
        """
        self.tasks[name] = {
            'function': func,
            'time': time_str,
            'created': datetime.now()
        }
        logger.info(f"Görev '{name}' zamanlandı: {time_str}")
    
    def start_scheduler(self):
        """Planlayıcıyı başlat"""
        if self.running:
            return
        
        self.running = True
        self.scheduler_thread = threading.Thread(target=self._run_scheduler, daemon=True)
        self.scheduler_thread.start()
        logger.info("Planlayıcı başlatıldı")
    
    def _run_scheduler(self):
        """Planlayıcı döngüsü"""
        while self.running:
            schedule.run_pending()
    
    def stop_scheduler(self):
        """Planlayıcıyı durdur"""
        self.running = False
        logger.info("Planlayıcı durduruldu")
    
    def list_tasks(self) -> List[str]:
        """Zamanlanmış görevleri listele"""
        return list(self.tasks.keys())
