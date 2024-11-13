from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет приветственное сообщение при вводе команды /start."""
    await update.message.reply_text(
        "Привет! Отправь мне фотографию, и я загружу её на imgbb.com и пришлю ссылку."
    )
