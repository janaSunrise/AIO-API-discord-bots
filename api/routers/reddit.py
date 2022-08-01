import random

from fastapi import APIRouter, Request

from ..config import reddit, subreddits
from ..utils.reddit import filter_reddit_url, get_random_post

router = APIRouter(
    prefix="/reddit",
    tags=["Reddit endpoint"],
    responses={
        404: {"description": "Not found"},
    },
)


@router.get("/hot")
async def hot(_: Request, subreddit: str) -> dict:
    sub = await reddit.subreddit(subreddit, fetch=True)
    random_post = random.choice([post async for post in sub.hot() if not post.is_self])

    return {
        "title": random_post.title,
        "description": random_post.selftext,
        "url": filter_reddit_url(random_post.url),
        "post_url": random_post.shortlink,
        "author": random_post.author.name,
        "score": random_post.score,
        "spoilers": sub.spoilers_enabled,
        "nsfw": sub.over18,
    }


@router.get("/new")
async def new(_: Request, subreddit: str) -> dict:
    sub = await reddit.subreddit(subreddit, fetch=True)
    random_post = random.choice([post async for post in sub.new() if not post.is_self])

    return {
        "title": random_post.title,
        "description": random_post.selftext,
        "url": filter_reddit_url(random_post.url),
        "post_url": random_post.shortlink,
        "author": random_post.author.name,
        "score": random_post.score,
        "spoilers": sub.spoilers_enabled,
        "nsfw": sub.over18,
    }


@router.get("/random")
async def reddit_random(_: Request, subreddit: str) -> dict:
    sub = await reddit.subreddit(subreddit, fetch=True)
    random_post = await sub.random()

    if not random_post:
        return {"error": "The subreddit doesn't support random post."}

    return {
        "title": random_post.title,
        "description": random_post.selftext,
        "url": filter_reddit_url(random_post.url),
        "post_url": random_post.shortlink,
        "author": random_post.author.name,
        "score": random_post.score,
        "spoilers": sub.spoilers_enabled,
        "nsfw": sub.over18,
    }


@router.get("/memes")
async def memes(_: Request) -> dict:
    """Have an awesome meme."""
    subreddit = await reddit.subreddit(
        random.choice(subreddits["memes"]),
        fetch=True,
    )
    return await get_random_post(subreddit)


@router.get("/aww")
async def aww(_: Request) -> dict:
    """Get an image that makes you say "aww"."""
    subreddit = await reddit.subreddit(
        random.choice(subreddits["aww"]),
        fetch=True,
    )
    return await get_random_post(subreddit)


@router.get("/funny")
async def funny(_: Request) -> dict:
    """Get a random funny image."""
    subreddit = await reddit.subreddit(
        random.choice(subreddits["funny"]),
        fetch=True,
    )
    return await get_random_post(subreddit)


@router.get("/cursedcomments")
async def cursed_comments(_: Request) -> dict:
    """Get a cursed comment image."""
    subreddit = await reddit.subreddit("cursedcomments", fetch=True)
    return await get_random_post(subreddit)
