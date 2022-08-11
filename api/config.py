import json
from typing import cast

from asyncpraw import Reddit, exceptions
from decouple import config
from loguru import logger


class APIConfig:
    VERSION = "0.1.0"
    DEBUG = cast(bool, config("DEBUG", default=False, cast=bool))

    USER_AGENT = "AIO API for discord bots"

    # Reddit config
    REDDIT_CLIENT_ID = cast(str, config("REDDIT_CLIENT_ID"))
    REDDIT_CLIENT_SECRET = cast(str, config("REDDIT_CLIENT_SECRET"))
    NASA_API = cast(str, config("NASA_API"))
    AI_ENABLED = cast(bool, config("AI_ENABLED", cast=bool))


class LoggerConfig:
    LOG_FILE = "logs/api.log"
    LOG_LEVEL = "DEBUG" if APIConfig.DEBUG else "INFO"
    LOG_FORMAT = (
        "<green>{time:YYYY-MM-DD hh:mm:ss}</green> | <level>{level: <8}</level> | "
        "<cyan>{name: <18}</cyan> | <level>{message}</level>"
    )


class RedditConfig:
    IMGUR_LINKS = (
        "https://imgur.com/",
        "https://i.imgur.com/",
        "http://i.imgur.com/",
        "http://imgur.com",
        "https://m.imgur.com",
    )
    ACCEPTED_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif")


# Reddit client
try:
    reddit = Reddit(
        client_id=APIConfig.REDDIT_CLIENT_ID,
        client_secret=APIConfig.REDDIT_CLIENT_SECRET,
        user_agent=APIConfig.USER_AGENT,
    )
except exceptions.MissingRequiredAttributeException:
    logger.error("Please set correct reddit environment variables to run.")

# Load all the JSON files
with open("api/assets/subreddits.json") as f:
    subreddits = json.load(f)

with open("api/assets/nsfw_subreddits.json") as f:
    nsfw_subreddits = json.load(f)

with open("api/assets/text_games_response.json") as f:
    text_game_responses = json.load(f)

# 8 Ball responses
BALL_REPLIES = {
    "positive": (
        "Absolutely!",
        "Affirmative!",
        "Alright.",
        "Aye aye, cap'n!",
        "Can do!",
        "I'll allow it.",
        "I got you.",
        "No problem.",
        "Of course!",
        "Okay.",
        "ROGER THAT",
        "Sure.",
        "Sure thing!",
        "Yeah okay.",
        "Yep.",
        "You got it!",
        "You're the boss!",
    ),
    "negative": (
        "Certainly not.",
        "Fat chance.",
        "Huh? No.",
        "I don't think so.",
        "I'm sorry Dave, I'm afraid I can't do that.",
        "Nah.",
        "Naw.",
        "NEGATORY.",
        "No way, José.",
        "Noooooo!!",
        "Nope.",
        "Not gonna happen.",
        "Not in a million years.",
        "Not in my house!",
        "Not likely.",
        "Nuh-uh.",
        "Out of the question.",
    ),
    "error": (
        "Are you trying to kill me?",
        "Do you mind?",
        "I can't believe you've done this",
        "In the future, don't do that.",
        "Noooooo!!",
        "Please don't do that.",
        "That was a mistake.",
        "You blew it.",
        "You have to stop.",
        "You're bad at computers.",
    ),
}

# Study router utils
RESPONSES = {
    200: True,
    301: "Switching to a different endpoint",
    400: "Bad Request",
    401: "Not Authenticated",
    404: "The resource you tried to access wasn't found on the server.",
    403: (
        "The resource you're trying to access is forbidden — "
        "you don't have the right permissions to see it."
    ),
}

# Wolfram alpha API config
DEFAULT_OUTPUT_FORMAT = "JSON"
QUERY = "http://api.wolframalpha.com/v2/{request}?{data}"
MAX_PODS = 20
