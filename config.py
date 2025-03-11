from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 24276024))
API_HASH = getenv("API_HASH", "d07b4f8342e732adbb300caedad3efc8")
BOT_TOKEN = getenv("BOT_TOKEN", "7585970299:AAFdRGBFS3-Vqvuny--47HcXs5UyD8dZae4")
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://surajit54321:surajit54321@cluster0.7mn37.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = int(getenv("OWNER_ID", "1380852165"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/surajit77707/Cb")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
SUPPORT_GRP = getenv("SUPPORT_GRP", "UmbrellaUCorp")
UPDATE_CHNL = getenv("UPDATE_CHNL", "moviiieeeesss")
OWNER_USERNAME = getenv("OWNER_USERNAME", "addyxassitant")
# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", "")
