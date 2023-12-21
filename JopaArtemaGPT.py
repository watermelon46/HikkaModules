# meta developer: @holinimmeta
__version__ = (1, 2,1)
import logging
import asyncio
import random
import time
from .. import loader, utils

logger = logging.getLogger(__name__)
symvolsbase = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхфывапролджэячсмитьбю1234567890  _-+():/ &#$%\@*;!?×÷^√∆-<>=α°•|{}[]πβγ⌀™©®"
emojibase = "😭😀🤣🤑🤔🤓😎😨😱😈🥸😐"
prompt = ""
answer = ""
def generate():
        """
        Генерация мешанины
        """
        global answer
        answer=""
        for i in range(1,random.randint(20,250)):
        	if random.randint(1,20)==5:
        		answer=answer+emojibase[random.randint(0,len(emojibase)-1)]
        	else:
        		answer=answer+symvolsbase[random.randint(0,len(symvolsbase)-1)]


@loader.tds
class JopaArtemaGPT(loader.Module):
    """Инновационная нейросеть основанная на жопе Артёма. Умнее, чем GPT-4!"""
    strings = {
        "name": "JopaArtemaGPT"
    }
    async def jagptcmd(self, message):
        """
        - спросить самую умную, быструю, и обученную нейросеть JopaArtemaGPT
        """
        
        prompt = utils.get_args_raw(message)
        if prompt=="":
        	await message.edit("<b>🤓 JopaArtemaGPT не знает, на что отвечать.</b> Использование команды:\n.jagpt [вопрос]")
        else:
            await message.edit(f"<b>👨‍💻 Вы:</b> {prompt}\n<b>🤖 JopaArtemaGPT:</b> Идет генерация, подождите")
            generate()
            time.sleep(random.randint(0, 4))
            await message.edit(f"<b>👨‍💻 Вы:</b> {prompt}\n<b>🤖 JopaArtemaGPT:</b> {answer}")