import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "37262228"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "201e693fe80a87ee2a1206ff729e1e2c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "9195352172:AAErDW0QD2JgxWG0W7RtzzIsA4OoDoQsKLA")

OWNER_ID = int(os.environ.get("OWNER_ID", "2053552336"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1004329721940"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "")  # Optional here you'll get all logs
