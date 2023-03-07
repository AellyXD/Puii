from secrets import choice

from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice

from . import puii_cmd


@puii_cmd(pattern="asupan$")
async def _(event):
    xx = await event.eor("`Wait a moment...`")
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@tedeasupancache",
                filter=InputMessagesFilterVideo,
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=choice(asupannya),
            reply_to=event.reply_to_msg_id,
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Could not find intake video.**")


@puii_cmd(pattern="desahcewe$")
async def _(event):
    xx = await event.eor("`Wait a moment...`")
    try:
        desahcewe = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancewesangesange",
                filter=InputMessagesFilterVoice,
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=choice(desahcewe),
            reply_to=event.reply_to_msg_id,
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Can't find a girl's sigh Wait a moment.**")


@puii_cmd(pattern="desahcowo$")
async def _(event):
    xx = await event.eor("`Wait a moment...`")
    try:
        desahcowo = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancowokkkk",
                filter=InputMessagesFilterVoice,
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=choice(desahcowo),
            reply_to=event.reply_to_msg_id,
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Couldn't find a cowboy sigh.**")
