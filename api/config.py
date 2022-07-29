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
