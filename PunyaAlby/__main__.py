# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram import idle

from config import *
from PunyaAlby import BOTLOG_CHATID, ALIVE_LOGO, LOGGER, LOOP, bots
from PunyaAlby.helpers.misc import git, heroku

MSG_ON = """
🔥 **ALBY-PYROBOT Berhasil Di Aktifkan**
   (\︵/) 
　⫺( •ᆺ•)⫹ 
┏━∪ ━━━━━━━━━━━
╏➠ **Userbot Version -** `{}`
╏➠ **Ketik** `{}alby` **untuk Mengecheck Bot**
┗━━━━━━━━━━━━━
"""
async def startupmessage(bot):
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG_CHATID:
            await bot.send_file(
                BOTLOG_CHATID,
                ALIVE_LOGO,
                caption=MSG_ON.format(BOT_VER, CMD_HANDLER),
                reply_to_message_id=ReplyCheck(message),
            )
    except Exception as e:
        LOGGER.error(e)
        return None


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("ruangdiskusikami")
            await bot.join_chat("ruangprojects")
            await bot.join_chat("ruang_gabutku")
            await startupmessage(bot)
        except Exception as a:
            LOGGER("main").warning(a)
    await idle()


if __name__ == "__main__":
    LOGGER("PunyaAlby").info("Starting ALBY-PYROBOT")
    git()
    heroku()
    LOGGER("PunyaAlby").info(f"ALBY-PYROBOT v{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")
    LOOP.run_until_complete(main())
