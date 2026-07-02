from telegram import Update
from telegram.ext import ContextTypes

from utils import extract_custom_emojis


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Send me a message containing Telegram custom emojis."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    text = message.text or message.caption or ""

    entities = message.entities or message.caption_entities

    emojis = extract_custom_emojis(entities)

    if not emojis:
        await message.reply_text("❌ No custom emoji found.")
        return

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

    await message.reply_text(
        "\n".join(lines),
        parse_mode="Markdown",
    )