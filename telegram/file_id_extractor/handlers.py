import logging

from telegram import Update
from telegram.ext import ContextTypes

from utils import (
    extract_custom_emojis,
    format_animation_info,
    format_audio_info,
    format_document_info,
    format_photo_info,
    format_sticker_info,
    format_video_info,
    format_video_note_info,
    format_voice_info,
)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📁 Send me any Telegram media and I'll extract its File ID."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    # -------- Custom Emoji --------

    entities = message.entities or message.caption_entities
    custom_emojis = extract_custom_emojis(entities)

    if custom_emojis:
        lines = [
            f"🎉 Found {len(custom_emojis)} Custom Emoji(s)",
            "",
        ]

        for index, emoji in enumerate(custom_emojis, start=1):
            lines.extend(
                [
                    f"#{index}",
                    f"ID: `{emoji['id']}`",
                    f"Offset: {emoji['offset']}",
                    f"Length: {emoji['length']}",
                    "",
                ]
            )

        await message.reply_text(
            "\n".join(lines),
            parse_mode="Markdown",
        )

    # -------- Media --------

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
        logger.info("Video Note received.")
        await message.reply_text(
            format_video_note_info(message.video_note),
            parse_mode="Markdown",
        )
        return

    if message.document:
        logger.info("Document received.")
        await message.reply_text(
            format_document_info(message.document),
            parse_mode="Markdown",
        )
        return

    if message.audio:
        logger.info("Audio received.")
        await message.reply_text(
            format_audio_info(message.audio),
            parse_mode="Markdown",
        )
        return

    if message.voice:
        logger.info("Voice received.")
        await message.reply_text(
            format_voice_info(message.voice),
            parse_mode="Markdown",
        )
        return

    if message.sticker:
        logger.info("Sticker received.")
        await message.reply_text(
            format_sticker_info(message.sticker),
            parse_mode="Markdown",
        )
        return

    if not custom_emojis:
        await message.reply_text(
            "❌ Unsupported media type."
        )