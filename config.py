# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "23626191"))
API_HASH = getenv("API_HASH", "a1416a7b389a7d6d4466ae5e014f7518")
BOT_TOKEN = getenv("BOT_TOKEN", "8166451122:AAGsNXECncBD1zW5XqbPa33Rg_EZgR24d2o")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7925792971").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://freestudymaterial2024:mc2pGRMs35YVlbLf@cluster0.fdhci3r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002524058716")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002551977817"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "20"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
