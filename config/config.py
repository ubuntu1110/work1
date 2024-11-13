import os


TELEGRAM_TOKEN = ''
IMGBB_API_KEY = ''


LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs', 'bot.log')

print(f"TELEGRAM_TOKEN is set: {bool(TELEGRAM_TOKEN)}")
print(f"IMGBB_API_KEY is set: {bool(IMGBB_API_KEY)}")
