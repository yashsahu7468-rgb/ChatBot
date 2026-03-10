import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API
API_ID = int(os.getenv("API_ID", 37912172))  
API_HASH = os.getenv("API_HASH", "4ebe9e1de9d1209a724a2d05a461387b")

# Bot Token / String Session
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
STRING1 = os.getenv("STRING_SESSION", None)

# Database
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://pusers:nycreation@nycreation.pd4klp1.mongodb.net/?retryWrites=true&w=majority&appName=NYCREATION")

# Owner / Admin
OWNER_ID = int(os.getenv("OWNER_ID", 8533355240))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "@ll_sexy_naxer_xd")

# Support / Updates
SUPPORT_GRP = os.getenv("SUPPORT_GRP", "https://t.me/+9Sy5xMqd5Ac4NjI1")
UPDATE_CHNL = os.getenv("UPDATE_CHNL", "@KASHIKA_MUSIC_UPDATE")