import os
import sys

from .version import __version__

run_as_module = __package__ in sys.argv or sys.argv[0] == "-m"


class ULTConfig:
    lang = "en"
    thumb = "resources/extras/puii.jpg"


if run_as_module:
    import time

    from .configs import Var
    from .startup import *
    from .startup._database import PuiiDB
    from .startup.BaseClient import PuiiClient
    from .startup.connections import validate_session, vc_connection
    from .startup.funcs import _version_changes, autobot, enable_inline, update_envs
    from .version import puii_version

    if not os.path.exists("./plugins"):
        LOGS.error(
            "'plugins' folder not found!\nMake sure that, you are on correct path."
        )
        exit()

    start_time = time.time()
    _ult_cache = {}
    _ignore_eval = []

    udB = PuiiDB()
    update_envs()

    LOGS.info(f"Connecting to {udB.name}...")
    if udB.ping():
        LOGS.info(f"Connected to {udB.name} Successfully!")

    BOT_MODE = udB.get_key("BOTMODE")
    DUAL_MODE = udB.get_key("DUAL_MODE")

    USER_MODE = udB.get_key("USER_MODE")
    if USER_MODE:
        DUAL_MODE = False

    if BOT_MODE:
        if DUAL_MODE:
            udB.del_key("DUAL_MODE")
            DUAL_MODE = False
        puii_bot = None

        if not udB.get_key("BOT_TOKEN"):
            LOGS.critical(
                '"BOT_TOKEN" not Found! Please add it, in order to use "BOTMODE"'
            )

            sys.exit()
    else:
        puii_bot = PuiiClient(
            validate_session(Var.SESSION, LOGS),
            udB=udB,
            app_version=puii_version,
            device_model="Puii",
        )
        puii_bot.run_in_loop(autobot())

    if USER_MODE:
        asst = puii_bot
    else:
        asst = PuiiClient(None, bot_token=udB.get_key("BOT_TOKEN"), udB=udB)

    if BOT_MODE:
        puii_bot = asst
        if udB.get_key("OWNER_ID"):
            try:
                puii_bot.me = puii_bot.run_in_loop(
                    puii_bot.get_entity(udB.get_key("OWNER_ID"))
                )
            except Exception as er:
                LOGS.exception(er)
    elif not asst.me.bot_inline_placeholder and asst._bot:
        puii_bot.run_in_loop(enable_inline(puii_bot, asst.me.username))

    vcClient = vc_connection(udB, puii_bot)

    _version_changes(udB)

    HNDLR = udB.get_key("HNDLR") or "."
    DUAL_HNDLR = udB.get_key("DUAL_HNDLR") or "/"
    SUDO_HNDLR = udB.get_key("SUDO_HNDLR") or HNDLR
else:
    print("pyPuii 2023 © AellyXD")

    from logging import getLogger

    LOGS = getLogger("pyPuii")

    puii_bot = asst = udB = vcClient = None
