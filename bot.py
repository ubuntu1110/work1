import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
from config.config import TELEGRAM_TOKEN, LOG_FILE
from handlers.start_handler import start
from handlers.help_handler import help_command
from handlers.photo_handler import handle_photo

def setup_logging():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(__name__)
    return logger

def main():
    """Запуск бота."""
    logger = setup_logging()
    logger.info("Запуск бота...")
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    application.run_polling()

if __name__ == '__main__':
    main()
