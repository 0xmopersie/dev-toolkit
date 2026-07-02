from telegram.ext import Application

from config import BOT_TOKEN


def main() -> None:
    app = Application.builder().token(BOT_TOKEN).build()

    print("Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()