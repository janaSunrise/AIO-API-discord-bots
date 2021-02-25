import random

from fastapi import APIRouter, Request

from api import config as conf
from api.config import reddit
from api.core import log_error
from api.utils import get_random_post

router = APIRouter(
    tags=["Reddit image posts"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/memes")
@log_error()
async def memes(_: Request) -> dict:
    """Have an awesome meme."""
    subreddit = await reddit.subreddit(
        random.choice(conf.subreddits_list["memes"]),
        fetch=True,
    )
    return await get_random_post(subreddit)


@router.get("/aww")
@log_error()
async def aww(_: Request) -> dict:
    """Get an image that makes you say "aww"."""
    subreddit = await reddit.subreddit(
        random.choice(conf.subreddits_list["aww"]),
        fetch=True,
    )
    return await get_random_post(subreddit)


@router.get("/funny")
@log_error()
async def funny(_: Request) -> dict:
    """Get a random funny image."""
    subreddit = await reddit.subreddit(
        random.choice(conf.subreddits_list["funny"]),
        fetch=True,
    )
    return await get_random_post(subreddit)


@router.get("/cursedcomments")
@log_error()
async def cursed_comments(_: Request):
    """Get a cursed comment image."""
    subreddit = await reddit.subreddit("cursedcomments", fetch=True)
    return await get_random_post(subreddit)
