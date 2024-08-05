# meta developer: @hlnmhikka
__version__ = (1, 0, 1)

from .. import loader
from telethon.tl.types import Message
import logging

logger = logging.getLogger(__name__)

logger.info("lnmCrawler service started")

@loader.tds
class lnmCrawler(loader.Module):
    """Модуль для сборки сообщений определенного человека."""
    strings = {
        "name": "lnmCrawler",
        "_cfg_doc_id": "ID человека, чьи сообщения будут логироваться.",
        "_cfg_doc_group": "ID группы, куда модуль будет направлять сообщения"
    }
    
    def __init__(self):
        self.config = loader.ModuleConfig(
        loader.ConfigValue(
               "id",
                0,
                lambda: self.strings("_cfg_doc_id"),
                validator=loader.validators.Integer(),
            ),
            loader.ConfigValue(
                "group",
                0,
                lambda: self.strings("_cfg_doc_group"),
                validator=loader.validators.Integer(),
            )
        )
    
    crawlerEnabled = True


    async def lnmcrawlercmd(self, message: Message):
        """включить или выключить сборщик"""
        if self.config["id"] == 0:
            await message.edit("<b><emoji document_id=5319156849650441567>😔</emoji> ID пользователя не задан. Задайте его в конфиге.</b>")
        elif self.config["group"] == 0:
            await message.edit("<b><emoji document_id=5319156849650441567>😔</emoji> ID группы не задан. Задайте его в конфиге или через .lnmsetgroup</b>")
        elif lnmCrawler.crawlerEnabled == True:
            action = "выключен"
            lnmCrawler.crawlerEnabled = False
        else:
            action = "включен"
            lnmCrawler.crawlerEnabled = True
        try:
            await message.edit(f"<b><emoji document_id=5318783359294382499>😎</emoji> Сборщик {action}.</b>")
        except UnboundLocalError:
            pass

    async def lnmsetgroupcmd(self, message: Message):
        """назначить группу местом сбора сообщений"""
        try:
            group = int("-100" + str(message.peer_id.channel_id))
            cntn = True
        except AttributeError:
            await message.edit('<b><emoji document_id=5319111726724030090>😡</emoji> Группа не является супергруппой. Читайте <a href="https://tginfo.me/groups_vs_supergroups/">эту статью</a> для информации о преобразовании группы в супергруппу, или задайте айди в конфиге самостоятельно.<b>')
            cntn = False
        if cntn == True:
            self.config["group"] = group
            await message.edit(f"<b><emoji document_id=5318783359294382499>😎</emoji> ID группы изменен на {group}</b>")



    async def watcher(self, message):
        if lnmCrawler.crawlerEnabled == True:
            if getattr(message, "from_id", None) == int(self.config["id"]):
                groupId = message.peer_id.channel_id
                msgId = message.id
                msgLink = f'https://t.me/c/{groupId}/{msgId}/'
                try:
                    msg = message.message
                except:
                    msg = 'сообщение не содержит текста'
                await message.client.send_message(
                        int(self.config["group"]),
                        f"<b><emoji document_id=5319310759803495101>🤔</emoji><a href = '{msgLink}'> Найдено новое сообщение</a></b>\n\n{msg}",
                )
