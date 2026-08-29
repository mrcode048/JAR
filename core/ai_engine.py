"""
AI Motor - Tüm AI Modelleri Entegrasyonu
OpenAI, Google Gemini, Anthropic Claude, Transformers
"""

import logging
from typing import Dict, Any, Optional
import os

logger = logging.getLogger(__name__)


class AIEngine:
    """Yapay Zeka Motor - Çoklu Model Desteği"""
    
    def __init__(self):
        logger.info("AI Engine başlatılıyor...")
        
        # Komut anahtar kelimeleri
        self.commands = {
            'time': ['saat', 'zaman', 'saati'],
            'weather': ['hava', 'yağmur', 'güneş', 'sıcaklık'],
            'system': ['sistem', 'bilgisayar', 'bilgiler', 'ram', 'cpu'],
            'open_app': ['aç', 'başlat', 'çalıştır'],
            'close_app': ['kapat', 'sonlandır'],
            'search': ['ara', 'bing', 'google'],
            'volume': ['ses', 'sesini', 'volume'],
            'brightness': ['parlaklık', 'ekran', 'brightness'],
            'shutdown': ['kapat', 'kapatılsın', 'shutdown'],
        }
        
        # AI Modelleri başlat
        self.openai_client = self._init_openai()
        self.gemini_client = self._init_gemini()
        self.claude_client = self._init_claude()
        self.transformer_model = self._init_transformer()
        
        self.ai_mode = self._detect_available_ai()
        logger.info(f"Aktif AI Modu: {self.ai_mode}")
    
    def _init_openai(self) -> Optional[Any]:
        """OpenAI GPT başlat"""
        try:
            import openai
            api_key = os.getenv('OPENAI_API_KEY')
            if api_key:
                openai.api_key = api_key
                logger.info("✓ OpenAI GPT yüklendi")
                return openai
            else:
                logger.warning("⚠ OPENAI_API_KEY bulunmadı")
                return None
        except Exception as e:
            logger.warning(f"OpenAI yüklenirken hata: {e}")
            return None
    
    def _init_gemini(self) -> Optional[Any]:
        """Google Gemini başlat"""
        try:
            import google.generativeai as genai
            api_key = os.getenv('GOOGLE_API_KEY')
            if api_key:
                genai.configure(api_key=api_key)
                logger.info("✓ Google Gemini yüklendi")
                return genai
            else:
                logger.warning("⚠ GOOGLE_API_KEY bulunmadı")
                return None
        except Exception as e:
            logger.warning(f"Google Gemini yüklenirken hata: {e}")
            return None
    
    def _init_claude(self) -> Optional[Any]:
        """Anthropic Claude başlat"""
        try:
            from anthropic import Anthropic
            api_key = os.getenv('ANTHROPIC_API_KEY')
            if api_key:
                client = Anthropic(api_key=api_key)
                logger.info("✓ Anthropic Claude yüklendi")
                return client
            else:
                logger.warning("⚠ ANTHROPIC_API_KEY bulunmadı")
                return None
        except Exception as e:
            logger.warning(f"Anthropic Claude yüklenirken hata: {e}")
            return None
    
    def _init_transformer(self) -> Optional[Any]:
        """Hugging Face Transformers başlat (Yerel)"""
        try:
            from transformers import pipeline
            logger.info("✓ Hugging Face Transformers yüklendi (Yerel AI)")
            return pipeline
        except Exception as e:
            logger.warning(f"Transformers yüklenirken hata: {e}")
            return None
    
    def _detect_available_ai(self) -> str:
        """Mevcut AI'yi tespit et"""
        if self.claude_client:
            return "claude"
        elif self.openai_client:
            return "openai"
        elif self.gemini_client:
            return "gemini"
        elif self.transformer_model:
            return "transformer"
        else:
            return "local"
    
    def process(self, text: str) -> str:
        """
        Metni işle ve cevap üret
        
        Args:
            text: Kullanıcı metni
            
        Returns:
            Cevap metni
        """
        text_lower = text.lower().strip()
        
        # Komut türünü belirle
        command_type = self._identify_command(text_lower)
        
        if command_type in ['time', 'weather', 'system', 'search']:
            return self._handle_system_command(command_type, text_lower)
        
        # AI modeline gönder
        return self._call_ai_model(text)
    
    def _identify_command(self, text: str) -> str:
        """Komut türünü belirle"""
        for cmd_type, keywords in self.commands.items():
            for keyword in keywords:
                if keyword in text:
                    return cmd_type
        return 'general'
    
    def _handle_system_command(self, cmd_type: str, text: str) -> str:
        """Sistem komutlarını işle"""
        if cmd_type == 'time':
            from datetime import datetime
            now = datetime.now()
            return f"Şu anda saat {now.strftime('%H:%M')}"
        elif cmd_type == 'weather':
            return "Hava durumu için internet bağlantısı gereklidir."
        elif cmd_type == 'system':
            return "Sistem bilgileri alınıyor..."
        elif cmd_type == 'search':
            return f"'{text}' için arama yapılıyor..."
        return ""
    
    def _call_ai_model(self, text: str) -> str:
        """AI modeline çağrı yap"""
        if self.ai_mode == "claude":
            return self._claude_response(text)
        elif self.ai_mode == "openai":
            return self._openai_response(text)
        elif self.ai_mode == "gemini":
            return self._gemini_response(text)
        elif self.ai_mode == "transformer":
            return self._transformer_response(text)
        else:
            return self._local_response(text)
    
    def _claude_response(self, text: str) -> str:
        """Claude API çağrısı"""
        try:
            message = self.claude_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": text}
                ]
            )
            return message.content[0].text
        except Exception as e:
            logger.error(f"Claude hata: {e}")
            return "Claude cevap veremedi, özür dilerim."
    
    def _openai_response(self, text: str) -> str:
        """OpenAI GPT çağrısı"""
        try:
            response = self.openai_client.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": text}
                ],
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"OpenAI hata: {e}")
            return "GPT cevap veremedi, özür dilerim."
    
    def _gemini_response(self, text: str) -> str:
        """Google Gemini çağrısı"""
        try:
            model = self.gemini_client.GenerativeModel('gemini-pro')
            response = model.generate_content(text)
            return response.text
        except Exception as e:
            logger.error(f"Gemini hata: {e}")
            return "Gemini cevap veremedi, özür dilerim."
    
    def _transformer_response(self, text: str) -> str:
        """Hugging Face Transformer çağrısı (Yerel)"""
        try:
            qa_pipeline = self.transformer_model(
                "question-answering",
                model="mrm8488/bert-multi-cased-finetuned-xquad"
            )
            response = qa_pipeline(text)
            return response.get('answer', 'Cevap üreti lemedi.')
        except Exception as e:
            logger.error(f"Transformer hata: {e}")
            return "Yerel AI cevap veremedi, özür dilerim."
    
    def _local_response(self, text: str) -> str:
        """Yerel basit cevap"""
        responses = [
            "Anlaşıldı, yardımcı olmaya çalışıyorum.",
            "Komutu işliyorum...",
            "Tamam, yapıyorum.",
            "Başlamışım bile.",
        ]
        import random
        return random.choice(responses)
    
    def get_ai_info(self) -> Dict[str, Any]:
        """AI durumunu göster"""
        return {
            'active_mode': self.ai_mode,
            'claude': bool(self.claude_client),
            'openai': bool(self.openai_client),
            'gemini': bool(self.gemini_client),
            'transformer': bool(self.transformer_model),
            'requires_api_keys': self.ai_mode in ['claude', 'openai', 'gemini']
        }
