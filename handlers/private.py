from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://i.ibb.co/khRz42f/Turkish-Voice.jpg",
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
                        "👨‍💻 OWNER", url="https://t.me/sesizKOLGE"
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
                         "⚡ Hazırladı", url="https://t.me/sesizKOLGE")
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
    await query.edit_message_text(f"""<b>Salam 👋 {query.from_user.mention}!\nBu Botun Hərkəs Üçün Əmr Menusudu ⚡\n\n ▶️ /oynat - şarkı çalmak için youtube url'sine veya şarkı dosyasına yanıt verme\n ▶️ /oynat <song name> - istediğiniz şarkıyı çal\n 🔴 \n 🎵 /bul <song name> - istediğiniz şarkıları hızlı bir şekilde bulun\n 🎵 /vbul istediğiniz videoları hızlı bir şekilde bulun\n 🔍 /ara <query> - youtube'da ayrıntıları içeren videoları arama\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Geliştirici", url="https://t.me/Mahoaga")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun adminler için komut menüsü 🤩\n\n ▶️ /devam - şarkı çalmaya devam et\n ⏸️ /durdur - çalan parçayı duraklatmak için\n 🔄 /atla- Sıraya alınmış müzik parçasını atlatır.\n ⏹ /son - müzik çalmayı durdurma\n 🔼 /ver botun sadece yönetici için kullanılabilir olan komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun yönetici komutlarını kullanabilen kullanıcının yetkisini al\n\n ⚪ /asistan - Müzik asistanı grubunuza katılır.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Geliştirici", url="https://t.me/Mahoaga")
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
    await query.edit_message_text(f"""**Merhaba {query.from_user.mention} 🎵\nBen {bot}!\nSesli sohbetlerde müzik çalabilen botum. Ban yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz.\n\nDüzen Tasarım [Talia Müzik 🎙️](https://t.me/Sohbetdestek).**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Grubuna Ekle ❱ ➕", url=f"https://t.me/Efsanestar_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/Taliamusicasistant"
                    ),
                    InlineKeyboardButton(
                        "💬 Sohbet", url="https://t.me/Sohbetskyfall"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌀 Komutlar" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Resmi Kanal 🇹🇷", url=f"https://t.me/Sohbetdestek"
                    )
                ]
                
           ]
        ),
    )
