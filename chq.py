# meta developer: @hlnmhikka
__version__ = (1, 3, 3, 7)
import logging
import asyncio
from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class ChequesNoArab(loader.Module):
    """Убери арабов из чата! Специально для Cheques"""
    strings = {
        "name": "ChequesNoArab"
    }
    async def switchlangcmd(self, message):
        """
        - отправить человека в другой языковой чат
        """
        await message.edit('<b>🤓 Switch to chat with your language</b>\n\n<a href="https://t.me/chequeschatique/91128/91129">RU Chat</a>\n<a href="https://t.me/chequeschatique/91113">FA Chat</a>\n<a href="https://t.me/chequeschatique/91172">EN Chat</a>')