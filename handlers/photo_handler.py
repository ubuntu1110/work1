import os
import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.imgbb import upload_image

logger = logging.getLogger(__name__)

MAX_PHOTOS_PER_MESSAGE = 10  
MAX_FILE_SIZE = 10 * 1024 * 1024  

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обрабатывает полученные фотографии, сохраняет их и загружает на imgbb."""
    try:
        photos = update.message.photo  # Список объектов PhotoSize для одной фотографии
        user_id = update.message.from_user.id
        logger.info(f"Получено {len(photos)} PhotoSize объектов от пользователя {user_id}")
        if not photos:
            await update.message.reply_text("Вы не отправили никаких фотографий.")
            logger.warning(f"Пользователь {user_id} не отправил фотографий.")
            return
        if len(photos) > MAX_PHOTOS_PER_MESSAGE:
            await update.message.reply_text(
                f"Вы отправили слишком много фотографий. Пожалуйста, отправьте не более {MAX_PHOTOS_PER_MESSAGE} фото за раз."
            )
            logger.warning(
                f"Пользователь {user_id} отправил {len(photos)} PhotoSize объектов, что превышает лимит."
            )
            return
        image_urls = []
        downloads_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'downloads')
        downloads_path = os.path.abspath(downloads_path)
        if not os.path.exists(downloads_path):
            os.makedirs(downloads_path)
            logger.info(f"Создана папка для загрузок: {downloads_path}")
        highest_res_photo = photos[-1]  
        logger.info(f"Обработка фотографии с размером: {highest_res_photo.width}x{highest_res_photo.height}")
        file = await highest_res_photo.get_file()
        file_size = file.file_size
        logger.info(f"Размер файла: {file_size} байт")

        if file_size > MAX_FILE_SIZE:
            await update.message.reply_text(
                f"Файл слишком большой (больше {MAX_FILE_SIZE // (1024 * 1024)} МБ). Пожалуйста, отправьте меньший файл."
            )
            logger.warning(
                f"Файл от пользователя {user_id} превышает максимальный размер: {file_size} байт."
            )
            return
        file_extension = os.path.splitext(file.file_path)[1] or '.jpg'
        file_name = f"user_{user_id}_photo{file_extension}"
        file_path = os.path.join(downloads_path, file_name)
        await file.download_to_drive(file_path)
        logger.info(f"Фотография сохранена по пути: {file_path}")
        image_url = upload_image(file_path)
        if image_url:
            logger.info(f"Фотография успешно загружена на imgbb: {image_url}")
            image_urls.append(image_url)
        else:
            logger.error(
                f"Не удалось загрузить фотографию от пользователя {user_id} на imgbb."
            )
            image_urls.append("Не удалось загрузить это изображение.")
        os.remove(file_path)
        logger.info(f"Удаление локального файла: {file_path}")

        if image_urls:
            response_message = f"Вот ваша ссылка на изображение:\n\n[Изображение]({image_urls[0]})"
            await update.message.reply_text(response_message, parse_mode='Markdown')
            logger.info(f"Отправлена ссылка пользователю {user_id}")
        else:
            await update.message.reply_text("Не удалось загрузить изображение.")
            logger.warning(f"Не удалось загрузить изображение от пользователя {user_id}")

    except Exception as e:
        logger.exception(f"Ошибка в обработчике фотографий: {e}")
        await update.message.reply_text("Произошла ошибка при обработке ваших фотографий.")
