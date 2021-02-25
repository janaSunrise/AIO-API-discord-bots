import random

from fastapi import APIRouter, Request

import api.config as conf
from api.config import reddit
from api.core import log_error
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
async def random_nsfw(_: Request) -> dict:
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["all"]),
        fetch=True,
    )
    return await get_random_post(subreddit)


@router.get("/4k")
@log_error()
async def _4k(_: Request) -> dict:
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["fourk"]),
        fetch=True,
    )
    return await get_random_post(subreddit)


@router.get("/ass")
@log_error()
async def ass(_: Request) -> dict:
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["ass"]),
        fetch=True,
    )
    return await get_random_post(subreddit)


@router.get("/bdsm")
@log_error()
async def bdsm(_: Request):
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["bdsm"]),
        fetch=True,
    )
    return await get_random_post(subreddit)


@router.get("/blowjob")
@log_error()
async def blowjob(_: Request):
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["blowjob"]),
        fetch=True,
    )
    return await get_random_post(subreddit)


@router.get("/deepthroat")
@log_error()
async def deepthroat(_: Request):
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["deepthroat"]),
        fetch=True,
    )
    return await get_random_post(subreddit)


@router.get("/hentai")
@log_error()
async def hentai(_: Request):
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["hentai"]),
        fetch=True,
    )
    return await get_random_post(subreddit)


@router.get("/lesbian")
@log_error()
async def lesbian(_: Request):
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["lesbian"]),
        fetch=True,
    )
    return await get_random_post(subreddit)


@router.get("/public")
@log_error()
async def public(_: Request):
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["public"]),
        fetch=True,
    )
    return await get_random_post(subreddit)


@router.get("/rule34")
@log_error()
async def rule34(_: Request):
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["rule34"]),
        fetch=True,
    )
    return await get_random_post(subreddit)


@router.get("/boobs")
@log_error()
async def boobs(_: Request):
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["boobs"]),
        fetch=True,
    )
    return await get_random_post(subreddit)


@router.get("/milf")
@log_error()
async def milf(_: Request):
    subreddit = await reddit.subreddit(
        random.choice(conf.nsfw_subreddits_list["milf"]),
        fetch=True,
    )
    return await get_random_post(subreddit)
