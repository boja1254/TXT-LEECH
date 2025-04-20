import os

API_ID    = os.environ.get("API_ID", 28962746)
API_HASH  = os.environ.get("API_HASH", "727457f88d661b08e636188a949cd9f3")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7966372736:AAGvPrULpIOJLXkAh5798BjH05P5YwA96Z4") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 6969))  # Default to 8000 if not set
