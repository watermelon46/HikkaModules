#  ___  ___  ___       ________   _____ ______      
# |\  \|\  \|\  \     |\   ___  \|\   _ \  _   \    
# \ \  \\\  \ \  \    \ \  \\ \  \ \  \\\__\ \  \   
#  \ \   __  \ \  \    \ \  \\ \  \ \  \\|__| \  \  
#   \ \  \ \  \ \  \____\ \  \\ \  \ \  \    \ \  \ 
#    \ \__\ \__\ \_______\ \__\\ \__\ \__\    \ \__\
#     \|__|\|__|\|_______|\|__| \|__|\|__|     \|__|
#                         
# Ducko by holinim
# Official GitHub repo of Holinim's modules: https://github.com/watermelon46/HikkaModules
# Official Telegram channel of Holinim's modules: https://t.me/hlnmhikka     
                                                                                         
# meta developer: @hlnmhikka & @zonerkin
import logging
import asyncio
from urllib.parse import quote_plus
from .. import loader, utils

def getSearchUrls(query):
    global duckurl, yaurl, googleurl, wikiruurl, wikienurl, yahoourl, bingurl
    encoded_query = quote_plus(query)
    duckurl = f"https://duckduckgo.com/html/?q={encoded_query}"
    yaurl = f"https://yandex.ru/search/?text={encoded_query}"
    googleurl = f"https://google.com/search?q={encoded_query}"
    wikiruurl = f"https://ru.wikipedia.org/w/index.php?search={encoded_query}&title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F%3A%D0%9F%D0%BE%D0%B8%D1%81%D0%BA&profile=advanced&fulltext=1"
    wikienurl = f"https://en.wikipedia.org/w/index.php?title=Special:Search&search={encoded_query}&fulltext=Search"
    yahoourl = f"https://search.yahoo.com/search?p={encoded_query}"
    bingurl = f"https://www.bing.com/search?q={encoded_query}"


logger = logging.getLogger(__name__)

@loader.tds
class Ducko(loader.Module):
    
    __version__ = (2, 0)
    """Ducko"""

    strings = {
        "name":  "Ducko",
        "error": "<b>⚠ Ошибка. Вероятно, ты не указал текст запроса</b>",
        "searching": "<b><emoji document_id=5188311512791393083>🔎</emoji> Ищем ответы на просторах поисковиков...</b>"
    }

    async def duckocmd(self, message):
        """
        [запрос] - искать в DuckDuckGo, Яндекс, Google, Bing, Yahoo, Wikipedia
        """
        query = utils.get_args_raw(message)
        if query:
            await message.edit("<b><emoji document_id=5188311512791393083>🔎</emoji> Ищем ответы на просторах поисковиков...</b>")
            getSearchUrls(query)
            await message.edit(f'<b><emoji document_id=5325652987685642265>🔎</emoji> Результаты поиска по запросу "{query}":</b>\n\n\n<a href="{duckurl}">🦆 DuckDuckGo</a>\n\n<a href="{yaurl}">🇷🇺 Яндекс</a>\n\n<a href="{googleurl}">🇺🇸 Google</a>\n\n<a href="{bingurl}">🇺🇸 Bing</a>\n\n<a href="{yahoourl}">🇺🇸 Yahoo</a>\n\n<a href="{wikiruurl}">📖🇷🇺 Wikipedia на русском</a>\n\n<a href="{wikienurl}">📖🇺🇸 Wikipedia на английском</a>')
        else:
            await message.edit(self.strings["error"])
    
    async def dduckcmd(self, message):
        """
        [запрос] - искать в DuckDuckGo
        """
        query = utils.get_args_raw(message)
        if query:
            await message.edit("<b><emoji document_id=5188311512791393083>🔎</emoji> Ищем ответы на просторах DuckDuckGo...</b>")
            getSearchUrls(query)
            await message.edit(f'<a href="{yaurl}"><b><emoji document_id=5325652987685642265>🔎</emoji> Результаты поиска по запросу "{query}" в DuckDuckGo</a></b>')
        else:
            await message.edit(self.strings["error"])

    async def dyandexcmd(self, message):
        """
        [запрос] - искать в Яндекс
        """
        query = utils.get_args_raw(message)
        if query:
            await message.edit("<b><emoji document_id=5188311512791393083>🔎</emoji> Ищем ответы на просторах Яндекса...</b>")
            getSearchUrls(query)
            await message.edit(f'<a href="{yaurl}"><b><emoji document_id=5325652987685642265>🔎</emoji> Результаты поиска по запросу "{query}" в Яндекс</a></b>')
        else:
            await message.edit(self.strings["error"])

    async def dgooglecmd(self, message):
        """
        [запрос] - искать в Google
        """
        query = utils.get_args_raw(message)
        if query:
            await message.edit("<b><emoji document_id=5188311512791393083>🔎</emoji> Ищем ответы на просторах Google...</b>")
            getSearchUrls(query)
            await message.edit(f'<a href="{googleurl}"><b><emoji document_id=5325652987685642265>🔎</emoji> Результаты поиска по запросу "{query}" в Google</a></b>')
        else:
            await message.edit(self.strings["error"])
    
    async def dbingcmd(self, message):
        """
        [запрос] - искать в Bing
        """
        query = utils.get_args_raw(message)
        if query:
            await message.edit("<b><emoji document_id=5188311512791393083>🔎</emoji> Ищем ответы на просторах Bing...</b>")
            getSearchUrls(query)
            await message.edit(f'<a href="{bingurl}"><b><emoji document_id=5325652987685642265>🔎</emoji> Результаты поиска по запросу "{query}" в Bing</a></b>')
        else:
            await message.edit(self.strings["error"])

    async def dyahoocmd(self, message):
        """
        [запрос] - искать в Yahoo
        """
        query = utils.get_args_raw(message)
        if query:
            await message.edit("<b><emoji document_id=5188311512791393083>🔎</emoji> Ищем ответы на просторах Yahoo...</b>")
            getSearchUrls(query)
            await message.edit(f'<a href="{yahoourl}"><b><emoji document_id=5325652987685642265>🔎</emoji> Результаты поиска по запросу "{query}" в Yahoo</a></b>')
        else:
            await message.edit(self.strings["error"])
    
    async def dwikicmd(self, message):
        """
        [запрос] - искать в Wikipedia
        """
        query = utils.get_args_raw(message)
        if query:
            await message.edit("<b><emoji document_id=5188311512791393083>🔎</emoji> Ищем ответы на просторах Wikipedia...</b>")
            getSearchUrls(query)
            await message.edit(f'<b><emoji document_id=5325652987685642265>🔎</emoji> Результаты поиска по запросу "{query}" в:</b>\n\n<a href="{wikiruurl}">🇷🇺 Wikipedia на русском</a>\n<a href="{wikienurl}">🇺🇸 Wikipedia на английском</a>')
        else:
            await message.edit(self.strings["error"])

# смешнявочная, но правдивая переписка создателей модуля:
#
# Холиним: а че там столько говнокода в модуле?
# Зонер: его чатгпт писал
            
# ну, все версии начиная с 2.0 написаны на 95% не чатгпт. от чатгпт только самая база, по типу 21 строки.
