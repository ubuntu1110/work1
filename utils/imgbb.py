import requests
import os
import logging
from config.config import IMGBB_API_KEY

logger = logging.getLogger(__name__)

def upload_image(file_path: str) -> str:
    """Загружает изображение на imgbb и возвращает URL."""
    upload_url = 'https://api.imgbb.com/1/upload'
    try:
        with open(file_path, "rb") as img_file:
            payload = {
                'key': IMGBB_API_KEY
            }
            files = {
                'image': img_file
            }
            response = requests.post(upload_url, data=payload, files=files)
        
        logger.info(f"Ответ от imgbb: {response.text}")
        
        response.raise_for_status()
        data = response.json()
        image_url = data['data']['url']
        return image_url
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при загрузке изображения на imgbb: {e}")
        return None
    except KeyError:
        logger.error(f"Некорректный ответ от imgbb: {response.text}")
        return None
