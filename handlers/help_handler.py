from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение с помощью при вводе команды /help."""
    await update.message.reply_text(
        "Просто отправь мне фотографию, и я верну ссылку на изображение, размещённое на imgbb.com."
    )
