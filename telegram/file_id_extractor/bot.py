from telegram.ext import Application

from config import BOT_TOKEN


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    print("File ID Extractor Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()