import random

import asyncpraw
from asyncpraw import exceptions
from fastapi import APIRouter
from loguru import logger

from api import config as conf
from api.utils import filter_reddit_url

router = APIRouter(
    prefix="/memes",
    tags=["memes"],
    responses={404: {"description": "Not found"}},
)

try:
    reddit = asyncpraw.Reddit(
        client_id=conf.reddit_client_id,
        client_secret=conf.reddit_client_secret,
        user_agent=conf.USER_AGENT
    )
except exceptions.MissingRequiredAttributeException:
    logger.error("Please set correct reddit environment variables to run.")


# -- Router paths --
@router.get("/")
async def root():
    subreddit = await reddit.subreddit(
        random.choice(conf.subreddits_list["memes"])
    )
    await subreddit.load()

    posts_list = [post async for post in subreddit.hot(limit=1000) if not post.is_self]

    random_post = random.choice(posts_list)

    return {
        "title": random_post.title,
        "description": random_post.selftext,
        "url": filter_reddit_url(random_post.url),
        "post_url": random_post.shortlink,
        "author": random_post.author.name,
        "spoilers": subreddit.spoilers_enabled,
        "nsfw": subreddit.over18
    }
