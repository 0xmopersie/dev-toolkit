from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Send me a message containing Telegram custom emojis."
    )


from telegram import Update
from telegram.ext import ContextTypes

from utils import extract_custom_emojis


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Send me a message containing Telegram custom emojis."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    entities = update.message.entities

    emoji_ids = extract_custom_emojis(entities)

    if not emoji_ids:
        await update.message.reply_text("❌ No custom emoji found.")
        return

    text = "🎉 Custom Emoji IDs\n\n"

    for emoji_id in emoji_ids:
        text += f"`{emoji_id}`\n"

    await update.message.reply_text(text, parse_mode="Markdown")