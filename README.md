# Telegram Image Uploader Bot

Этот бот принимает фотографии от пользователей, загружает их на imgbb.com и возвращает ссылку на изображение.

## Структура проекта


## Установка

1. **Склонируйте репозиторий:**
    ```bash
    git clone https://github.com/yourusername/telegram_imgbb_bot.git
    cd telegram_imgbb_bot
    ```

2. **Создайте и активируйте виртуальное окружение:**
    ```powershell
    python -m venv telegram_bot_env
    # Windows
    .\telegram_bot_env\Scripts\Activate.ps1
    # macOS/Linux
    source telegram_bot_env/bin/activate
    ```

3. **Установите зависимости:**
    ```powershell
    pip install -r requirements.txt
    ```

4. **Создайте файл `.env` и добавьте ваши API ключи:**
    ```env
    TELEGRAM_TOKEN=your_telegram_bot_token_here
    IMGBB_API_KEY=your_imgbb_api_key_here
    ```

5. **Запустите бота:**
    ```powershell
    python bot.py
    ```

## Использование

- Отправьте боту фотографию.
- Получите ссылку на изображение, загруженное на imgbb.com.

## Лицензия

MIT
