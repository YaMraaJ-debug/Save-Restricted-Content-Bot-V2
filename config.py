# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "1721373"))
API_HASH = getenv("API_HASH", "d029ff3bc5680a0ac7c448415ccbc442")
BOT_TOKEN = getenv("BOT_TOKEN", "1591149653:AAEeECrgh0pYWAdRecuOFaLPTTsujK8GXQg")
OWNER_ID = list(map(int, getenv("OWNER_ID", "799036495").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://lok:like@cluster0.nqmprqy.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = getenv("LOG_GROUP", "-1002239640141")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001246452766"))
