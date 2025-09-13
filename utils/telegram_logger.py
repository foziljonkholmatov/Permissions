import requests


TELEGRAM_BOT_TOKEN = 'TOKEN'
TELEGRAM_CHAT_ID = 'CHAT_ID'

def send_telegram_error(message: str):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "HTML"}
        requests.post(url, data=payload, timeout=5)
    except Exception as e:
        print('Not sent to telegram', e)
