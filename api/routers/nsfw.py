import random

from fastapi import APIRouter

from api.core import log_error
import api.config as conf
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
@log_error()
async def random_nsfw():
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["all"]),
        fetch=True
    )

    return await get_random_post(subreddit)
