import os
import asyncio

import requests


def send_telegram_alert(message: str):
    bot_token = os.getenv("TELEGRAM_ALERT_BOT_TOKEN")
    chat_id = os.getenv("SUPPORT_USER_TELEGRAM_ID")
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, payload)
    return response.status_code == 200


async def send_telegram_info_async(message: str):
    bot_token = os.getenv("TELEGRAM_ALERT_BOT_TOKEN")
    chat_id = os.getenv("SUPPORT_USER_TELEGRAM_ID")
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, payload)
    return response.status_code == 200
