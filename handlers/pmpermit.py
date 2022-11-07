from pyrogram import Client
import asyncio
from config import SUDO_USERS
from config import PMPERMIT
from pyrogram import filters
from pyrogram.types import Message
from callsmusic.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                "Salam 👋, Musiqi Asistanı Xirmətinizdədir.\n\n ❗️ ƏMRLƏR:\n - Şəxsi Söhbətdə İcazə Yoxdur.\n - Məlumat Və Əmrlər Üçün Qrupunuzun Söhbətində**/məlumat** Yazın . (Asistanın Şəxsi Sphbətinə Məlumat Yazmayın.) Musiqi Əmirlırini Öyrənə Bilərsiz.\n - İsdənmiyən Posta İcazə Verilməz.\n\n 🚨 **Userbot Grupunuza Qatılmırsa >> DAVƏT QATILMA ÖZƏLLİYİ VƏ SƏS YÖNƏTİMİ ÖZƏLLİKLƏRİ VER ADMİN EDİN. <<**\n\n ⚠️ DİQQƏT: Burda bir mesaj göndərirsəniz, Adminim göndərdiyinizi görəcəkdir.\n - Şəxsi məlumatlarıburda paylaşmayın. (Musiqi Botunu Zəhmıt Olmasa Gizli Qrublara Almayın) 📚 Məlumat Üçün [OWNER 👨‍💻](https://t.me/sesizKOLGE) 🇹🇷\n",
            )
            return
 
    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("✅  PM İcazəsi Açıq")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("⚡ PM İcazəsi Qapalı")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("**Userbot Yazışması Artıq Uğurlu.**")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Təxmin Olaraq PM")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Bu Şəkildə PM")
        return
    message.continue_propagation()
