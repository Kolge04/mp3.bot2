from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://images.app.goo.gl/in11Pj1tHNhVo4DY9",
                caption=(f"""**Salam 👋 {message.from_user.mention} 🎵\nMən {bot}!\nSəsli Söhbətlırdə Musiqi Oxuya Bilən Musiqi Botuyam. Ban Yetkisi Olmadan, Səsli Söhbəti İdarə Etmə Yetkisi Verib, Asistanı Qrupa Qatın.\n\nMəlumat Üçün [𝐊 𝐎 𝐋 𝐆 Ə _ 𝐌 𝐏 3 🎧 ](https://t.me/sesizKOLGE).**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Qrubuna Ekle ❱ ➕", url=f"https://t.me/Kolgempbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 ASİSTAN", url="https://t.me/KolgeMp3Asistan"
                    ),
                    InlineKeyboardButton(
                        "DİGƏR BOTUM ⚡", url="https://t.me/kolgetaggerbot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 ƏMRLƏR" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 OWNER 🇦🇿", url=f"https://t.me/sesizKOLGE"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["məlumat", f"məlumat@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text("     📎 QEYD:\n\n Botun Aktif İşləməsi Üçün 3 Yetkiyə Ehdiyacı var:\n- Mesaj silmə yetkisi,\n- Bağlantı ile dəvət etmə yetkisi,\n- Səsli söhbeti İdaraə Etmə yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "📚 Hərkəs Üçün Əmr", callback_data="herkes")
                 ],[                     
                     InlineKeyboardButton(
                         "📚 Adminlər Üçün Əmr", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "📱 Əsas Menu", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "DİGƏR BOTUM ⚡", url="https://t.me/kolgetaggerbot")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text("    📎 QEYD:\nBotun Aktif İşləməsi Üçün 3 Yetkiyə Ehdiyac Var:\n- Mesaj Silmə yetkisi,\n- Bağlantı ilə dəvet etmə yetkisi,\n- Səsli sohbeti İdarə Etmə yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "📚 Hərkıs Üçün Əmr", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "👮‍♂️ Admin Əmirləri",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "📱 Əsas Menu", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "👨‍💻 OWNER 🇦🇿", url="https://t.me/sesizKOLGE")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam 👋 {query.from_user.mention}!\nBu Botun Hərkəs Üçün Əmr Menusudu ⚡\n\n ▶️ /play - Musiqi Adı\n\n▶️ /play - URL°YouTube\n\n 🎧 /song - Musiqi Adı - Musiqi Yükləyər\n\n 🎬 /vsong - Link`YouTube` Vidyo Yükləyər\n\n 🔍 /search <Link> - YouTube Dən Oxşar Musiqi, Vidyoları Tapar \n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "👨‍💻 OWNER 🇦🇿", url="https://t.me/sesizKOLGE")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ GERİ ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam 👋 {query.from_user.mention}!\nBu Botun Adminler Üçün Əmrlər Menusudu ⚡\n\n▶️ /resume - Musiqi Oxutmağa Davam Edər\n⏸️ /pause - Səsləndirilən Musiqini Dayandirar\n⏩ /skip- Növbədəki Musiqiyə Keçər.\n ⏺ /end - Səsli Yayındakı Musiqini Sonlandırar\n💂‍♂️ /yetgiver - Userə İsdifadəçi Yetgisi Verər\n💂‍♂️ /yetgial - Userə Verilən İsdifadəçi Yetgisin Alar\n🤖 /asistan - Asistanı Qrupunuza Qatar\n♻️ /reload - Botu Yenidən Başladar\n⚜ /alive - Botun İşləyib İşləmədəyin Yoxlayar\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "👨‍💻 OWNER 🇦🇿", url="https://t.me/sesizKOLGE")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**Salam 👋 {query.from_user.mention} 🎵\nMən {bot}!\nSəsli Söhbətlərdə Musiqi Oxuya Bilən Musiqi Botuyam. Ban Yetkisi Olmadan, Səsli Söhbəti İdarə Etmə Yetgisi Verib, Asistanı Qruba Qatın.\n\n👨‍💻 OWNER [𝐊 𝐎 𝐋 𝐆 Ə _ 𝐌 𝐏 3 🎧](https://t.me/sesizKOLGE).**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Qrupuna Eklə ❱ ➕", url=f"https://t.me/Kolgempbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/KolgeMp3Asistan"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 OWNER 🇦🇿", url="https://t.me/sesizKOLGE"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 ƏMRLƏR" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        " DİGƏR BOTUM ⚡", url=f"https://t.me/kolgetaggerbot"
                    )
                ]
                
           ]
        ),
    )
