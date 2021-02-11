import random

from fastapi import APIRouter

from api import config as conf
from api.config import reddit
from api.utils import get_random_post

router = APIRouter(
    prefix="/funny",
    tags=["funny"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/")
async def root():
    subreddit = await reddit.subreddit(
        random.choice(conf.subreddits_list["funny"]),
        fetch=True
    )

    return await get_random_post(subreddit)
