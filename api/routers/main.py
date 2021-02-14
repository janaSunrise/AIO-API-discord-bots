import random

from fastapi import APIRouter

from api import config as conf
from api.core import log_error
from api.config import reddit
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
async def memes():
    subreddit = await reddit.subreddit(
        random.choice(conf.subreddits_list["memes"]),
        fetch=True
    )

    return await get_random_post(subreddit)


@router.get("/aww")
@log_error()
async def aww():
    subreddit = await reddit.subreddit(
        random.choice(conf.subreddits_list["aww"]),
        fetch=True
    )

    return await get_random_post(subreddit)


@router.get("/funny")
@log_error()
async def funny():
    subreddit = await reddit.subreddit(
        random.choice(conf.subreddits_list["funny"]),
        fetch=True
    )

    return await get_random_post(subreddit)


@router.get("/cursedcomments")
@log_error()
async def cursed_comments():
    subreddit = await reddit.subreddit(
        "cursedcomments",
        fetch=True
    )

    return await get_random_post(subreddit)
