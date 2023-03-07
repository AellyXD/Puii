"""
• Same as `sysinfo`, get system informations with carbon image.

• **Available commands**:

  • `{i}osinfo`
"""

from . import *
from os import remove

@puii_cmd(
    pattern="osinfo$",
)
async def _(e):
    xx = await e.eor(get_string("com_1"))
    x, y = await bash("neofetch|sed 's/\x1B\\[[0-9;\\?]*[a-zA-Z]//g' >> neo.txt")
    if y and y.endswith("NOT_FOUND"):
        return await xx.edit(f"Error: `{y}`")
    with open("neo.txt", "r", encoding="utf-8") as neo:
        p = (neo.read()).replace("\n\n", "")
    haa = await async_searcher(
                    "https://carbonara.vercel.app/api/cook",
                    json={"code": p},
                    post=True,
                    re_content=True)
    if isinstance(haa, dict):
        await xx.edit(f"`{haa}`")
    else:
        await e.reply(file=haa)
        await xx.delete()
    remove("neo.txt")
