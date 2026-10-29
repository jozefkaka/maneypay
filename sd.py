
import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.environ.get("BOT_TOKEN")


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "سلام! 🤖\n"
        "من ربات شما هستم و آنلاینم!\n"
        "هر پیامی بفرستی، جواب می‌دم."
    )


async def reply(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    message = update.message.text
    await update.message.reply_text(
        f"پیامت رو دریافت کردم: {message}"
    )


def main():
    if not TOKEN:
        raise RuntimeError(
            "BOT_TOKEN در تنظیمات محیطی تعریف نشده است."
        )

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, reply)
    )

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
