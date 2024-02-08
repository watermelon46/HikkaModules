
# meta developer: @zonerkin & @holinimmeta
import logging
import asyncio
from urllib.parse import quote_plus
from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class Ducko(loader.Module):
    
    __version__ = (1, 1)

    """Ducko"""

    strings = {
        "name":  "Ducko",
        "error": "<b>⚠ Ошибка. Вероятно, ты не указал текст запроса</b>",
        "success": "<b>👇 Нажмите ниже для открытия результатов в браузере</b>"
    }

    async def duckocmd(self, message):
        """
        [запрос] - искать в DuckDuckGo
        """
        query = utils.get_args_raw(message)
        if query:
            await message.edit("Ищу ответы в DuckDuckGo...")
            encoded_query = quote_plus(query)
            url = f"https://duckduckgo.com/html/?q={encoded_query}"
            
            await message.edit(f'<b><a href="{url}"><emoji document_id=5188217332748527444>🔍</emoji> Результаты запроса {query} в DuckDuckGo</a></b>')
        else:
            await message.edit(self.strings["error"])