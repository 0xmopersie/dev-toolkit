import logging

from telegram import Update
from telegram.ext import ContextTypes

from utils import (
    format_animation_info,
    format_photo_info,
    format_video_info,
    format_video_note_info,
)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📁 Send me Telegram media and I'll extract its File ID."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    if message.photo:
        logger.info("Photo received.")
        await message.reply_text(
            format_photo_info(message.photo[-1]),
            parse_mode="Markdown",
        )
        return

    if message.video:
        logger.info("Video received.")
        await message.reply_text(
            format_video_info(message.video),
            parse_mode="Markdown",
        )
        return

    if message.animation:
        logger.info("Animation received.")
        await message.reply_text(
            format_animation_info(message.animation),
            parse_mode="Markdown",
        )
        return

    if message.video_note:
        logger.info("Video note received.")
        await message.reply_text(
            format_video_note_info(message.video_note),
            parse_mode="Markdown",
        )
        return

    await message.reply_text(
        "❌ Please send a supported Telegram media."
    )