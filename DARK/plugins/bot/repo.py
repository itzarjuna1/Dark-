from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DARK import app
from config import BOT_USERNAME
from DARK.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ ᴛᴏ 𝗧ᴇᴀᴍ ᴅᴀʀᴋ ʙᴏᴛs ✰
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ ʀᴇᴘᴏ Dɪᴋʜᴀɴᴀ ʜᴏᴛᴀ ᴛᴏʜ ʙᴏᴛ ᴘʀɪᴠᴀᴛᴇʟʏ ǫ ʙᴀɴᴀᴛᴀ ʙʜᴀɪ

✰ || @ll_KUZE_ll ||
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛ᴇʟᴘ", url="hhttps://t.me/dark_x_knight_musiczz_support"),
          InlineKeyboardButton("❰ ꪜ乇乙 乂 ιꪀᠻιꪀι𝕥ꪗ ❱", url="https://t.me/ll_KUZE_ll"),
          ],
               [
                InlineKeyboardButton("ᴛᴇᴀᴍ ᴅᴀʀᴋ ʙᴏᴛs", url=f"https://t.me/dark_x_knight_musiczz_support"),
],
[
InlineKeyboardButton("𝗠ᴀɪɴ 𝗕ᴏᴛ", url=f"https://t.me/infinity_powerfull_bot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/p6iyy9.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
