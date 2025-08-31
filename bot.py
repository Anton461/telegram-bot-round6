import os
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

def round_div6(n: float) -> float:
    return round(n / 6, 2) * 6

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Надішли число — я округлю так, щоб при діленні на 6 було не більше 2 знаків після коми.")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text.strip().replace(",", ".")
        num = float(text)
        res = round_div6(num)
        await update.message.reply_text(f"Результат: {res}")
    except ValueError:
        await update.message.reply_text("Будь ласка, надішли число (приклад: 3012 або 3012,5).")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.run_polling()

if __name__ == "__main__":
    main()
