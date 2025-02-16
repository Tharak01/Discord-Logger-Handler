# discord_logger/logger.py
import requests
import json
import logging
from datetime import datetime, timezone
from typing import Optional, Dict, Any

class DiscordLogger:
    def __init__(self, webhook_url: str, app_name: str = "Application", min_level: str = "DEBUG"):
        self.webhook_url = webhook_url
        self.app_name = app_name
        
        self.logger = logging.getLogger(app_name)
        
        level_map = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        self.logger.setLevel(level_map.get(min_level.upper(), logging.DEBUG))
    
    def _create_embed(self, level: str, message: str, extra: Optional[Dict[str, Any]] = None) -> Dict:
        """Create a Discord embed for the log message."""
        colors = {
            'DEBUG': 7506394,    # Gray
            'INFO': 3447003,     # Blue
            'WARNING': 16776960, # Yellow
            'ERROR': 15158332,   # Red
            'CRITICAL': 10038562 # Dark red
        }
        
        embed = {
            'title': f'{self.app_name} - {level}',
            'description': message,
            'color': colors.get(level, 7506394),
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'fields': []
        }
        
        if extra:
            for key, value in extra.items():
                embed['fields'].append({
                    'name': key,
                    'value': str(value),
                    'inline': True
                })
                
        return embed
    
    def _send_to_discord(self, embed: Dict) -> bool:
        """Send the formatted embed to Discord."""
        payload = {'embeds': [embed]}
        
        try:
            response = requests.post(
                self.webhook_url,
                json=payload,
                headers={'Content-Type': 'application/json'}
            )
            return response.status_code == 204
        except Exception as e:
            print(f"Failed to send to Discord: {str(e)}")
            return False

    def debug(self, message: str, **kwargs) -> None:
        """Send a debug level log message."""
        embed = self._create_embed('DEBUG', message, kwargs)
        self._send_to_discord(embed)
        self.logger.debug(message)
    
    def info(self, message: str, **kwargs) -> None:
        """Send an info level log message."""
        embed = self._create_embed('INFO', message, kwargs)
        self._send_to_discord(embed)
        self.logger.info(message)
    
    def warning(self, message: str, **kwargs) -> None:
        """Send a warning level log message."""
        embed = self._create_embed('WARNING', message, kwargs)
        self._send_to_discord(embed)
        self.logger.warning(message)
    
    def error(self, message: str, **kwargs) -> None:
        """Send an error level log message."""
        embed = self._create_embed('ERROR', message, kwargs)
        self._send_to_discord(embed)
        self.logger.error(message)
    
    def critical(self, message: str, **kwargs) -> None:
        """Send a critical level log message."""
        embed = self._create_embed('CRITICAL', message, kwargs)
        self._send_to_discord(embed)
        self.logger.critical(message)