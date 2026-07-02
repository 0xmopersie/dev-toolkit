import logging

from telegram import Message, Update
from telegram.ext import ContextTypes

from utils import extract_custom_emojis

logger = logging.getLogger(__name__)


def get_target_message(message: Message) -> Message:
    """Return the replied message if available, otherwise the current message."""
    return message.reply_to_message or message


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Send or reply to a message containing Telegram custom emojis."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = get_target_message(update.message)

    logger.info(
        "Message received | chat_id=%s | user_id=%s",
        message.chat.id,
        message.from_user.id if message.from_user else "Unknown",
    )

    entities = message.entities or message.caption_entities

    emojis = extract_custom_emojis(entities)

    if not emojis:
        logger.info("No custom emoji found.")
        await update.message.reply_text("❌ No custom emoji found.")
        return

    logger.info("Found %d custom emoji(s).", len(emojis))

    lines = [
        f"🎉 Found {len(emojis)} Custom Emoji(s)",
        "",
    ]

    for index, item in enumerate(emojis, start=1):
        lines.extend(
            [
                f"#{index}",
                f"ID: `{item['id']}`",
                f"Type: {item['type']}",
                f"Offset: {item['offset']}",
                f"Length: {item['length']}",
                "",
            ]
        )

    await update.message.reply_text(
        "\n".join(lines),
        parse_mode="Markdown",
    )

    logger.info("Response sent successfully.")