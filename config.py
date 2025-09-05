import os
import re
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env
load_dotenv()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📲 Telegram & API Credentials
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
API_ID = int(os.getenv("API_ID", "22657083"))
API_HASH = os.getenv("API_HASH", "d6186691704bd901bdab275ceaab88f3")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "8195241636"))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "x9Ahad")
BOT_USERNAME = os.getenv("BOT_USERNAME", "PreetixMusic_bot")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🛠️ Database & Deployment Configs
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MONGO_DB_URI = os.getenv(
    "MONGO_DB_URI",
    "mongodb+srv://shreyan82683:shreyan82683@cluster0.c8v26ub.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "-1002981254436"))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

# External API URLs and Keys
API_URL = os.getenv("API_URL", "https://api.thequickearn.xyz")
VIDEO_API_URL = os.getenv("VIDEO_API_URL", "https://api.video.thequickearn.xyz")
API_KEY = os.getenv("API_KEY", "30DxNexGenBots121b50")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄 Git & Update Settings
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/Nobi-123/IvanMusic")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔗 Support Links
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/PreetixUpdate")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/preetixmusic")
PRIVACY_LINK = os.getenv("PRIVACY_LINK", "https://graph.org/Privacy-Policy-05-01-30")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⏱️ Duration & Playlist Settings
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 300))
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📦 File Size Limits (in bytes)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎧 Spotify Developer Credentials
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧵 Session Strings (Pyrogram V2)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STRING1 = os.getenv("STRING_SESSION", "")
STRING2 = os.getenv("STRING_SESSION2")
STRING3 = os.getenv("STRING_SESSION3")
STRING4 = os.getenv("STRING_SESSION4")
STRING5 = os.getenv("STRING_SESSION5")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚙️ Runtime Configurations
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", False))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🖼️ Image URLs (Customizable)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/v1asa0.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/ydvqvu.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/p3s1jd.jpg"
STATS_IMG_URL = "https://files.catbox.moe/v1asa0.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/j0na4q.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/j0na4q.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/5f2pwv.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/5f2pwv.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/5f2pwv.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/5f2pwv.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/5f2pwv.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/5f2pwv.jpg"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔐 User & Bot State Stores
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

TEMP_DB_FOLDER = "tempdb"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⏳ Time Conversion Utility
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def time_to_seconds(time: str) -> int:
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ❌ Validate Support Links
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL URL is invalid. It must start with https://")

if SUPPORT_GROUP and not re.match(r"(?:http|https)://", SUPPORT_GROUP):
    raise SystemExit("[ERROR] - SUPPORT_GROUP URL is invalid. It must start with https://")