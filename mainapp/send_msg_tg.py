import requests
from django.conf import settings

def send_message_tg(message):
    tg_id = settings.TELEGRAM_MY_ID
    bot_token = settings.TELEGRAM_BOT_TOKEN
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': tg_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()