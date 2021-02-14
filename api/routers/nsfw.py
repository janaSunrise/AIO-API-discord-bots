import random

from fastapi import APIRouter

import api.config as conf
from api import http_client
from api.config import reddit
from api.utils import get_random_post

router = APIRouter(
    prefix="/nsfw",
    tags=["NSFW images endpoint"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/random")
async def random_nsfw():
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["all"]),
        fetch=True
    )

    return await get_random_post(subreddit)
