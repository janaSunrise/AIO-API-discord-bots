import random

from fastapi import APIRouter

from api import config as conf
from api.config import reddit
from api.utils import get_random_post

router = APIRouter(
    tags=["reddit post"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/memes")
async def memes():
    subreddit = await reddit.subreddit(
        random.choice(conf.subreddits_list["memes"]),
        fetch=True
    )

    return await get_random_post(subreddit)


@router.get("/aww")
async def aww():
    subreddit = await reddit.subreddit(
        random.choice(conf.subreddits_list["aww"]),
        fetch=True
    )

    return await get_random_post(subreddit)


@router.get("/funny")
async def funny():
    subreddit = await reddit.subreddit(
        random.choice(conf.subreddits_list["funny"]),
        fetch=True
    )

    return await get_random_post(subreddit)


@router.get("/cursedcomments")
async def funny():
    subreddit = await reddit.subreddit(
        "cursedcomments",
        fetch=True
    )

    return await get_random_post(subreddit)
