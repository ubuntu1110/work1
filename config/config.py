import os

# Вставьте ваши реальные токены здесь
TELEGRAM_TOKEN = '7602774898:AAH-zWl4W3EhXvGRltJA0xOEqX02Hdfwr8Y'
IMGBB_API_KEY = '10dc1b6b495fb5faed7b40151ef4023c'

# Путь к файлу логов
LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs', 'bot.log')

# Отладочный вывод (для проверки, удалите после настройки)
print(f"TELEGRAM_TOKEN is set: {bool(TELEGRAM_TOKEN)}")
print(f"IMGBB_API_KEY is set: {bool(IMGBB_API_KEY)}")
