from pyrogram import Client, filters
from pyrogram.types import Message
from config import BOT_NAME as bn
from config import SUDO_USERS
import os



downloads = os.path.realpath("downloads")
raw_files = os.path.realpath("raw_files")

@Client.on_message(filters.command(["temizle", "clean"]) & ~filters.edited & filters.user(SUDO_USERS))
async def clear_downloads(_, message: Message):
    await message.delete()
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("**✅ {} Botunun Daxilindəki bütün Yüklənən Dosyalar Silindi.**".format(bn) )
    else:
        await message.reply_text("✅ **🗂 Yüklənən Dosya Yox.**")
    ls_dir = os.listdir(raw_files)
    if ls_dir:
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("**✅ {} Botundakı Bütün RAW Dosyaları Silindi.**".format(bn) )
    else:
        await message.reply_text("❌ **🗂 RAW Dosyaları Tapılmadı.**")
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("✅ **🗂 Lazımsız Dosyalar Silindi.**")
    else:
        await message.reply_text("❌ **🗂 Lazımsız Dosyalar Tapılmadı.**")

        


