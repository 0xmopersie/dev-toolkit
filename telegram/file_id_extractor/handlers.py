import logging

from telegram import Update
from telegram.ext import ContextTypes

from utils import format_photo_info

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📁 Send me a photo and I'll extract its File ID."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    if message.photo:
        photo = message.photo[-1]

        logger.info("Photo received.")

        await message.reply_text(
            format_photo_info(photo),
            parse_mode="Markdown",
        )

        return

    await message.reply_text(
        "❌ Please send a photo."
    )