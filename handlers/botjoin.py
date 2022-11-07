from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only
from config import SUDO_USERS 
import asyncio

@Client.on_message(filters.group & filters.command(["qatıl", "asistan"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>ℹ Mənə İlk Olaraq Yetki Verməlisən\n\n✅ Mesaj Silmə\n✅ Bağlantı İlə Dəvət Etmə\n✅ Səsli Söhbəti Yönətmə</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "AsistanUserbot"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"😀 Sen İsdəyin Üçün Gəldim")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>✅ Asistan Onsuzda Bu Qrupda Var</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🔵 Zaman Aşımı Xətası 🔵\n User {user.first_name} Userbot Üçün Böyük Qatılma İsdəkləri Üçün Qrupa Qatılamadı! Asistanın qrupda Əngənlənmədiyindən əmin olun."
            "\n\n Yada Asistan Hesabını Qruba Özün Ekle </b>",
        )
        return
    await message.reply_text(
            "<b>✅ Asistan Onsuzda Bu Qrupda Var</b>",
        )
    
@USER.on_message(filters.group & filters.command(["ayrıl", "asistanat"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>❌ Asistan Qrubunuzdan Ayrılamadı!."
            "\n\n✅ Yada Özün Çıxarda Bilərsən</b>",
        )
        return
 
@USER.on_message(filters.group & filters.command(["userbotat", "userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>❌ Userbot Qrubunuzdan Ayrılamadı!."
            "\n\n✅ Vəya Məni Qrubunuzdan manuel Olaraq Atin</b>",
        )
        return


@Client.on_message(filters.command(["tamayrıl", "maho"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left = 0
        failed = 0
        lol = await message.reply("✅ Bütün Qruplardan Ayrılıram...")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left + 1
                await lol.edit(
                    f"Ayrılıram... Left: {left} chats. Failed: {failed} chats."
                )
            except:
                failed = failed + 1
                await lol.edit(
                    f"Ayrılıram... Left: {left} chats. Failed: {failed} chats."
                )
            await asyncio.sleep(0.7)
        await client.send_message(
            message.chat.id, f"Left {left} chats. Failed {failed} chats."
        )
 
 
