import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Application

TOKEN = '7917687353:AAF1Al7xIvEg8v8iMWE-vxrnCzCriY-4qGs'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

scripts = {
    'brookhaven': """
🔥 **Brookhaven RP** (январь 2026)

**Soluna Hub** — лучший тролл:
loadstring(game:HttpGet("https://raw.githubusercontent.com/Patheticcs/Soluna-API/refs/heads/main/brookhaven.lua",true))()

**Infinite Yield** — админ команды:
loadstring(game:HttpGet("https://raw.githubusercontent.com/EdgeIY/infiniteyield/master/source"))()

ID: 4924922222 | Только альт-аккаунт!
    """,

    'fishit': """
🎣 **Fish It!** (январь 2026)

**ViKai HUB** — авто-фарм:
loadstring(game:HttpGet("https://raw.githubusercontent.com/ViKaiHub/ViKai/main/FishIt"))()

**VinzHub**:
loadstring(game:HttpGet("https://raw.githubusercontent.com/VinzHub/Vinz/main/FishIt"))()

ID: 121864768012064
    """,

    'bloxfruits': """
🍈 **Blox Fruits**

**Redz Hub**:
loadstring(game:HttpGet("https://raw.githubusercontent.com/RedZHub/RedZHub/main/RedZ"))()
    """,

    'arsenal': """
🔫 **Arsenal**

**Owl Hub**:
loadstring(game:HttpGet("https://raw.githubusercontent.com/CriShoux/OwlHub/master/OwlHub.txt"))()
    """,

    'petsimulator': """
🐾 **Pet Simulator 99**

**Vynixius**:
loadstring(game:HttpGet("https://raw.githubusercontent.com/RegularVynixu/Vynixius/main/Pet%20Simulator%2099/Script.lua"))()
    """
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 **Привет! Я бот Roblox-скриптов** 😈\n\n"
        "Пиши /script [игра]\n\n"
        "Примеры:\n"
        "/script brookhaven\n"
        "/script fishit\n"
        "/script bloxfruits\n\n"
        "Скрипты свежие 2026 года!",
        parse_mode='Markdown'
    )

async def get_script(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Напиши название игры после /script")
        return

    game = ' '.join(context.args).lower()
    if game in scripts:
        await update.message.reply_text(scripts[game], parse_mode='Markdown', disable_web_page_preview=True)
    else:
        await update.message.reply_text(f"Скрипта для {game} пока нет. Напиши название — добавлю!")

if __name__ == '__main__':
    # Создаём приложение
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("script", get_script))
    print("🤖 Бот запущен на webhook!")
    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 8443)),
        url_path=TOKEN,
        webhook_url=f"https://script-roblox-bot.onrender.com/{TOKEN}"
    )
    
