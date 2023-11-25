# meta developer: @holinimmeta

import logging
import asyncio
import random
import time
from .. import loader, utils

logger = logging.getLogger(__name__)
symvolsbase = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхфывапролджэячсмитьбю1234567890_-+()'/"
prompt = ""
answer = ""
def generate():
        """
        Генерация мешанины
        """
        global answer
        for i in range(1,random.randint(20,250)):
        	answer=answer+symvolsbase[random.randint(0,130)]

@loader.tds
class JopaArtemaGPT(loader.Module):
    """Инновационная нейросеть основанная на жопе Артёма. Умнее, чем GPT-4!"""

    strings = {
        "name": "JopaArtemaGPT"
    }

    async def jagptcmd(self, message):
        """
        Спросить самую умную, быструю, и обученную нейросеть JopaArtemaGPT
        """
        
        prompt = utils.get_args_raw(message)
        await message.edit(f"Вы: {prompt}\nJopaArtemaGPT: Идет генерация, подождите")
        generate()
        time.sleep(random.randint(0, 10))
        await message.edit(f"Вы: {prompt}\nJopaArtemaGPT: {answer}")
