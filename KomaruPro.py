__version__ = (1, 3)
# meta developer: @hlnmhikka
print('KomaruPro 1.3 тоже может содержать много всяких багов... Репортите их в @hlnmhikka!')


from random import choice, randint

from telethon.tl.types import (
    InputMessagesFilterGif,
    InputMessagesFilterPhotos,
    InputMessagesFilterVideo,
    Message,
)

from .. import loader, utils

def selectchannel(confeg):
    if confeg == 'random':
        return choice(['komarueveryday', 'komaru_gif', 'komaru'])
    elif confeg != 'random':
        return confeg

class KomaruPro(loader.Module):
    """Отправить случайное медиа с Комару, Кокоа или Комуги из @komarueveryday, @komaru_gif и @komaru. Настройки модуля в .config"""

    strings = {
        "name": "KomaruPro",
        "choosing": "<b><emoji document_id=5188311512791393083>🔎</emoji> Выбираем {}...</b>",
        "gif": "GIF'ку",
        "video": "видео",
        "photo": "картинку",
        "_cfg_doc_media_source": "Канал, откуда модуль будет брать медиа, значение ОБЯЗАТЕЛЬНО БЕЗ @. Если у вас вместо медиа из канала кидаются случайные пикчи из всех ваших чатов - убедитесь что вы ввели правильный юзернейм",
        "_cfg_doc_contain_text": "Нужно ли добавлять в сообщение оригинальную подпись?"
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "media_source",
                'random',
                lambda: self.strings("_cfg_doc_media_source"),
                validator=loader.validators.String(),
            ),
            loader.ConfigValue(
                "contain_text",
                False,
                lambda: self.strings("_cfg_doc_contain_text"),
                validator=loader.validators.Boolean()
            )
        )

    
    SEARCH_TYPES = {
        InputMessagesFilterGif: "gif",
        InputMessagesFilterPhotos: "photo",
        InputMessagesFilterVideo: "video",
    }

    @loader.command(ru_doc="- отправить случайную медиа с ККК")
    async def komarucmd(self, message: Message):
        """- отправить случайное медиа с ККК из @komarueveryday, @komaru_gif или @komaru"""
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
                    selectchannel(self.config["media_source"]), limit=200, filter=search_type
                )
            ]
        )

        reply = await message.get_reply_message()
        if reply:
            reply = reply.id
        else:
            reply = None
        if self.config["contain_text"]==False:
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

    async def kmrgifcmd(self, message: Message):
        """- отправить случайную гиф с ККК"""
        search_type = InputMessagesFilterGif
        search_type_str = self.strings(self.SEARCH_TYPES[search_type])

        msg = await utils.answer(
            message, self.strings("choosing").format(search_type_str)
        )

        chosed_msg = choice(
            [
                message_in_channel
                async for message_in_channel in self.client.iter_messages(
                    selectchannel(self.config["media_source"]), limit=200, filter=search_type
                )
            ]
        )

        reply = await message.get_reply_message()
        if reply:
            reply = reply.id
        else:
            reply = None
        if self.config["contain_text"]==False:
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

    async def kmrvidcmd(self, message: Message):
        """- отправить случайное видео с ККК"""
        search_type = InputMessagesFilterVideo
        search_type_str = self.strings(self.SEARCH_TYPES[search_type])

        msg = await utils.answer(
            message, self.strings("choosing").format(search_type_str)
        )

        chosed_msg = choice(
            [
                message_in_channel
                async for message_in_channel in self.client.iter_messages(
                    selectchannel(self.config["media_source"]), limit=200, filter=search_type
                )
            ]
        )

        reply = await message.get_reply_message()
        if reply:
            reply = reply.id
        else:
            reply = None
        if self.config["contain_text"]==False:
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

    async def kmrpiccmd(self, message: Message):
        """- отправить случайную картинку с ККК"""
        search_type = InputMessagesFilterPhotos
        search_type_str = self.strings(self.SEARCH_TYPES[search_type])

        msg = await utils.answer(
            message, self.strings("choosing").format(search_type_str)
        )

        chosed_msg = choice(
            [
                message_in_channel
                async for message_in_channel in self.client.iter_messages(
                    selectchannel(self.config["media_source"]), limit=200, filter=search_type
                )
            ]
        )

        reply = await message.get_reply_message()
        if reply:
            reply = reply.id
        else:
            reply = None
        if self.config["contain_text"]==False:
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
