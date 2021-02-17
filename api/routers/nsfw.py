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
async def random_nsfw() -> dict:
    subreddit = await reddit.subreddit(random.choice(conf.nsfw_subreddits_list["all"]), fetch=True)
    return await get_random_post(subreddit)


@router.get("/4k")
@log_error()
async def _4k() -> dict:
    subreddit = await reddit.subreddit(random.choice(conf.nsfw_subreddits_list["fourk"]), fetch=True)
    return await get_random_post(subreddit)


@router.get("/ass")
@log_error()
async def ass() -> dict:
    subreddit = await reddit.subreddit(random.choice(conf.nsfw_subreddits_list["ass"]), fetch=True)
    return await get_random_post(subreddit)


@router.get("/bdsm")
@log_error()
async def bdsm():
    subreddit = await reddit.subreddit(random.choice(conf.nsfw_subreddits_list["bdsm"]), fetch=True)
    return await get_random_post(subreddit)


@router.get("/blowjob")
@log_error()
async def blowjob():
    subreddit = await reddit.subreddit(random.choice(conf.nsfw_subreddits_list["blowjob"]), fetch=True)
    return await get_random_post(subreddit)


@router.get("/deepthroat")
@log_error()
async def deepthroat():
    subreddit = await reddit.subreddit(random.choice(conf.nsfw_subreddits_list["deepthroat"]), fetch=True)
    return await get_random_post(subreddit)


@router.get("/hentai")
@log_error()
async def hentai():
    subreddit = await reddit.subreddit(random.choice(conf.nsfw_subreddits_list["hentai"]), fetch=True)
    return await get_random_post(subreddit)


@router.get("/lesbian")
@log_error()
async def lesbian():
    subreddit = await reddit.subreddit(random.choice(conf.nsfw_subreddits_list["lesbian"]), fetch=True)
    return await get_random_post(subreddit)


@router.get("/public")
@log_error()
async def public():
    subreddit = await reddit.subreddit(random.choice(conf.nsfw_subreddits_list["public"]), fetch=True)
    return await get_random_post(subreddit)


@router.get("/rule34")
@log_error()
async def rule34():
    subreddit = await reddit.subreddit(random.choice(conf.nsfw_subreddits_list["rule34"]), fetch=True)
    return await get_random_post(subreddit)


@router.get("/boobs")
@log_error()
async def boobs():
    subreddit = await reddit.subreddit(random.choice(conf.nsfw_subreddits_list["boobs"]), fetch=True)
    return await get_random_post(subreddit)


@router.get("/milf")
@log_error()
async def milf():
    subreddit = await reddit.subreddit(random.choice(conf.nsfw_subreddits_list["milf"]), fetch=True)
    return await get_random_post(subreddit)
