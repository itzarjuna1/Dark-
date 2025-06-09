import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "21195558"))
API_HASH = getenv("56f56a1dd7a3c3c3c0ac1df8788ae32f")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7732173919:AAGOQsF_f9rTMWL_gstdpF3qwSQAEra-Dtg")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","ll_KU")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME","Anya_lip_bot")
# --------------------------------------------------------
BOT_NAME = getenv("AnyaXMusic")
# ---------------------------------------------------------


# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002556228441))

# Get this value from @PURVI_HELP_BOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7495324168))


## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Gxinfinity/ANYA_MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/gxinfinity_support")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/infinitygx_bot_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION","BQFKJysAxVxAxgqf61WltaV3rS6KaeO03Mn0Ygv4U_OZJHQFXNd3CcbVfRBMYDyTVCIwQ2g7oyH7uFsQ8XwT_l0PSzowMKBHVTDXoERLJl6h-mueia1XFNeOPdtjMGtEc826AkID4FAcSVDqvcpFw7DZKgEpzPM51tV3o7XQzVH-FbaAfT1ILJMHMuFQ3xY_4qERyiAmuTkxS4c5K_l99Q0-drf5O6gnv4BhQmB7maftnqhruBFpqzRZkE2xUQ1kHJUAb9u1gVcekmOx-dgtCvccKBw54nEAhCuFjaYbDQS_MIGBgTF3_1HmNsQMqcv8JXSsNzkUjCGKY3rIxTEexI1zftYVPAAAAAHVyIxhAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/rca1m3.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/9cevdg.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/i493lf.jpg"
STATS_IMG_URL = "https://files.catbox.moe/i0qmgf.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/8e3552aa743ffdb6f18c9.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/8e3552aa743ffdb6f18c9.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
