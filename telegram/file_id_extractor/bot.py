import logging

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN
from handlers import handle_message, start

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.exception(
        "Unhandled exception while processing update",
        exc_info=context.error,
    )


def main():
    logger.info("Starting File ID Extractor Bot...")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
    MessageHandler(
        filters.ALL,
        handle_message,
    )
)

    app.add_error_handler(error_handler)

    logger.info("Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()