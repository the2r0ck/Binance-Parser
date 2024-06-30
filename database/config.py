import os

class Config:
    host = os.getenv("TRADINGBOT_DATABASE_HOST")
    user = os.getenv("TRADINGBOT_DATABASE_USER")
    port = os.getenv("TRADINGBOT_DATABASE_PORT")
    password = os.getenv("TRADINGBOT_DATABASE_PASSWORD")
    name = os.getenv("TRADINGBOT_DATABASE_NAME")
    