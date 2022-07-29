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
with open("assets/subreddits.json") as f:
    subreddits = json.load(f)

with open("assets/nsfw_subreddits.json") as f:
    nsfw_subreddits = json.load(f)

with open("assets/text_game_responses.json") as f:
    text_game_responses = json.load(f)

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
