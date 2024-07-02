import os

import requests

from config import TelegramConfig


def send_telegram_alert(message: str):
    url = f"https://api.telegram.org/bot{TelegramConfig.alert_bot_token}/sendMessage"
    for chat_id in TelegramConfig.support_user_ids:
        payload = {
            "chat_id": chat_id,
            "text": message
        }
        response = requests.post(url, payload)
    return response.status_code == 200


def send_telegram_info(message: str):
    url = f"https://api.telegram.org/bot{TelegramConfig.info_bot_token}/sendMessage"
    print(url)
    for chat_id in TelegramConfig.support_user_ids:
        payload = {
            "chat_id": chat_id,
            "text": message
        }
        response = requests.post(url, payload)
    print(response.json())
    return response.status_code == 200


async def send_telegram_info_async(message: str):
    url = f"https://api.telegram.org/bot{TelegramConfig.info_bot_token}/sendMessage"
    for chat_id in TelegramConfig.support_user_ids:
        payload = {
            "chat_id": chat_id,
            "text": message
        }
        response = requests.post(url, payload)
    return response.status_code == 200
