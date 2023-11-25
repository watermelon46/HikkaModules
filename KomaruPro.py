__version__ = (1, 1, 1)
# meta developer: @holinimmeta
channel = 0
# Значения не сохраняется при перезагрузке
# 0 - случайный канал
# 1 - komarueveryday
# 2 - komaru_gif
containtext = False
# True - добавлять подпись с оригинального медиа
# False - не добавлять подпись
from random import choice, randint
def selectchannel():
    if channel == 1:
        ch = "komarueveryday"
    elif channel == 2:
        ch = "komaru_gif"
    else:
        if randint(0, 1) == 0:
            ch = "komaru_gif"
        else:
            ch = "komarueveryday"
    return ch
from telethon.tl.types import (
    InputMessagesFilterGif,
    InputMessagesFilterPhotos,
    InputMessagesFilterVideo,
    Message,
)

from .. import loader, utils


class KomaruPro(loader.Module):
    """Отправить случайное медиа с Комару из @komarueveryday и @komaru_gif"""

    strings = {
        "name": "KomaruPro",
        "choosing": "<emoji document_id=5328311576736833844>🔎</emoji> Выбираем {}...",
        "gif": "GIF'ку",
        "video": "видео",
        "photo": "картинку",
    }

    SEARCH_TYPES = {
        InputMessagesFilterGif: "gif",
        InputMessagesFilterPhotos: "photo",
        InputMessagesFilterVideo: "video",
    }

    @loader.command(ru_doc="- отправить случайную медиа с Комару")
    async def komarucmd(self, message: Message):
        """- отправить случайное медиа с Комару из @komarueveryday и @komaru_gif"""
        search_type = choice(
            [
                InputMessagesFilterGif,
                InputMessagesFilterPhotos,
                InputMessagesFilterVideo,
            ]
        )
        search_type_str = self.strings(self.SEARCH_TYPES[search_type])

        msg = await utils.answer(
            message, self.strings("choosing").format(search_type_str)
        )

        chosed_msg = choice(
            [
                message_in_channel
                async for message_in_channel in self.client.iter_messages(
                    selectchannel(), limit=200, filter=search_type
                )
            ]
        )

        reply = await message.get_reply_message()
        if reply:
            reply = reply.id
        else:
            reply = None
        if containtext==False:
            return await utils.answer_file(
                msg,
                chosed_msg,
                reply_to=reply,
            )
        else:
            return await utils.answer_file(
                msg,
                chosed_msg,
                chosed_msg.text or "",
                reply_to=reply,
            )
    async def usekomarugifcmd(self, message: Message):
        """- изменить источник медиа на @komaru_gif"""
        channel = 2
        await message.edit("Источник медиа был сменен на @komaru_gif :3")

    async def usekomarueverydaycmd(self, message: Message):
        """- изменить источник медиа на @komarueveryday"""
        global channel
        channel = 1
        await message.edit("Источник медиа был сменен на @komaru_everyday :3")

    async def userandomcmd(self, message: Message):
        """- выбирать источник медиа случайно"""
        global channel
        channel = 0
        await message.edit("Источник медиа теперь выбирается случайно :3")
    async def addsigncmd(self, message: Message):
        """- добавлять к медиа оригинальную подпись (вкл/выкл)"""
        global containtext
        if containtext==True:
            containtext=False
            await message.edit("Теперь к медиа не будет добавляться оригинальная подпись :3")
        else:
            containtext=True
            await message.edit("Теперь к медиа будет добавляться оригинальная подпись :3")
            
    