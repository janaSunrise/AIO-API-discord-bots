import os

import asyncpraw
from asyncpraw import exceptions
from loguru import logger

# -- Constants definition --
USER_AGENT = "AIO-API for discord bots"

# -- Reddit variable config --
reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
reddit_client_secret = os.getenv("REDDIT_CLIENT_SECRET")

try:
    reddit = asyncpraw.Reddit(
        client_id=reddit_client_id,
        client_secret=reddit_client_secret,
        user_agent=USER_AGENT
    )
except exceptions.MissingRequiredAttributeException:
    logger.error("Please set correct reddit environment variables to run.")

# -- Subreddit config --
subreddits_list = {
    "memes": [
        "memes",
        "dankmemes",
        "funny",
        "ComedyCemetery",
        "wholesomememes",
        "meirl",
        "DeepFriedMemes",
    ]
}
