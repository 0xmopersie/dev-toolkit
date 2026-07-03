# Telegram Custom Emoji ID Extractor

A simple Telegram bot that extracts **Telegram Custom Emoji IDs** from messages.

## Features

- ✅ Extract custom emoji IDs
- ✅ Supports multiple custom emojis
- ✅ Supports captions
- ✅ Supports replied messages
- ✅ Supports forwarded messages
- ✅ Built with python-telegram-bot 22.x
- ✅ Structured logging

## Installation

```bash
git clone https://github.com/0xmopersie/dev-toolkit.git

cd dev-toolkit/telegram/emoji_id_extractor
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
BOT_TOKEN=YOUR_BOT_TOKEN
```

Run:

```bash
python bot.py
```

## Example Output

```
🎉 Found 2 Custom Emoji(s)

#1
ID: 5424972470023104089
Type: Custom Emoji
Offset: 0
Length: 2

#2
ID: 5461151367559141950
Type: Custom Emoji
Offset: 8
Length: 2
```

## Project Structure

```
emoji_id_extractor/
├── bot.py
├── config.py
├── handlers.py
├── utils.py
├── requirements.txt
├── .env.example
└── README.md
```

## License

MIT