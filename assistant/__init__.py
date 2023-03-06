# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from telethon import Button, custom

from plugins import ATRA_COL, InlinePlugin
from pyPuii import *
from pyPuii import _ult_cache
from pyPuii._misc import owner_and_sudos
from pyPuii._misc._assistant import asst_cmd, callback, in_pattern
from pyPuii.fns.helper import *
from pyPuii.fns.tools import get_stored_file
from strings import get_languages, get_string

OWNER_NAME = puii_bot.full_name
OWNER_ID = puii_bot.uid

AST_PLUGINS = {}


async def setit(event, name, value):
    try:
        udB.set_key(name, value)
    except BaseException as er:
        LOGS.exception(er)
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    return [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
