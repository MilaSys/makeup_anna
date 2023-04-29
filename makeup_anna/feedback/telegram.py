import os
from dotenv import load_dotenv

from telegram import Bot

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
bot = Bot(token=TELEGRAM_TOKEN)

def send_message(bot, message):
    """Отправка сообщения в Телеграмм."""
    chat_id = TELEGRAM_CHAT_ID
    bot.send_message(chat_id, message)