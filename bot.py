from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "mo",
    api_id="18717139",
    api_hash="f63aef030aba7879bd273c1373823465",
    bot_token="5343340817:AAFXfDoGDO19V9UECk3I6qaEIudoBgi2ueY",
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    AFROTOO = "IIUll_l"
    await bot.send_message(MeDoO, "**تم تشغيل ال صانع بنجاح عزيزي المطور ...🥀،**")
    print("[INFO]: تم تشغيل الصانع وارسال رسالة للمطور⚡🚦.")
    await idle()
