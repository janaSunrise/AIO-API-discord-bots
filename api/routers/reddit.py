import random

from fastapi import APIRouter

from api.core import log_error
from api.config import reddit
from api.utils import filter_reddit_url

router = APIRouter(
    prefix="/reddit",
    tags=["Custom reddit post endpoint"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/hot")
@log_error()
async def hot(subreddit: str) -> dict:
    subreddit = await reddit.subreddit(subreddit, fetch=True)
    random_post = random.choice([post async for post in subreddit.hot() if not post.is_self])

    return {
        "title": random_post.title,
        "description": random_post.selftext,
        "url": filter_reddit_url(random_post.url),
        "post_url": random_post.shortlink,
        "author": random_post.author.name,
        "score": random_post.score,
        "spoilers": subreddit.spoilers_enabled,
        "nsfw": subreddit.over18
    }


@router.get("/new")
@log_error()
async def new(subreddit: str) -> dict:
    subreddit = await reddit.subreddit(subreddit, fetch=True)
    random_post = random.choice(
        [post async for post in subreddit.new() if not post.is_self]
    )

    return {
        "title": random_post.title,
        "description": random_post.selftext,
        "url": filter_reddit_url(random_post.url),
        "post_url": random_post.shortlink,
        "author": random_post.author.name,
        "score": random_post.score,
        "spoilers": subreddit.spoilers_enabled,
        "nsfw": subreddit.over18
    }


@router.get("/random")
@log_error()
async def reddit_random(subreddit: str) -> dict:
    subreddit = await reddit.subreddit(subreddit, fetch=True)
    random_post = await subreddit.random()

    if not random_post:
        return {"error": "The subreddit doesn't support random post."}

    return {
        "title": random_post.title,
        "description": random_post.selftext,
        "url": filter_reddit_url(random_post.url),
        "post_url": random_post.shortlink,
        "author": random_post.author.name,
        "score": random_post.score,
        "spoilers": subreddit.spoilers_enabled,
        "nsfw": subreddit.over18
    }
