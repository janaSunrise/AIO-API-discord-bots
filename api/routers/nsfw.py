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


@router.get("/4k")
async def _4k():
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["fourk"]),
        fetch=True
    )

    return await get_random_post(subreddit)


@router.get("/ass")
async def ass():
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["ass"]),
        fetch=True
    )

    return await get_random_post(subreddit)


@router.get("/bdsm")
async def bdsm():
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["bdsm"]),
        fetch=True
    )

    return await get_random_post(subreddit)


@router.get("/blowjob")
async def blowjob():
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["blowjob"]),
        fetch=True
    )

    return await get_random_post(subreddit)


@router.get("/deepthroat")
async def deepthroat():
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["deepthroat"]),
        fetch=True
    )

    return await get_random_post(subreddit)


@router.get("/hentai")
async def hentai():
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["hentai"]),
        fetch=True
    )

    return await get_random_post(subreddit)


@router.get("/lesbian")
async def lesbian():
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["lesbian"]),
        fetch=True
    )

    return await get_random_post(subreddit)


@router.get("/public")
async def public():
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["public"]),
        fetch=True
    )

    return await get_random_post(subreddit)


@router.get("/rule34")
async def rule34():
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["rule34"]),
        fetch=True
    )

    return await get_random_post(subreddit)


@router.get("/boobs")
async def boobs():
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["boobs"]),
        fetch=True
    )

    return await get_random_post(subreddit)


@router.get("/milf")
async def milf():
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["milf"]),
        fetch=True
    )

    return await get_random_post(subreddit)
