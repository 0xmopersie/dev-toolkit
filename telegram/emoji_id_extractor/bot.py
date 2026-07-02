from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN
from handlers import handle_message, start


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT | filters.Caption(True), handle_message)
    )

    print("Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()