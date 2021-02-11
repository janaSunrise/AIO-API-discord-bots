import random

from fastapi import APIRouter

from api import config as conf
from api.config import reddit
from api.utils import filter_reddit_url

router = APIRouter(
    prefix="/memes",
    tags=["memes"],
    responses={404: {"description": "Not found"}},
)


# -- Router paths --
@router.get("/")
async def root():
    subreddit = await reddit.subreddit(
        random.choice(conf.subreddits_list["memes"]),
        fetch=True
    )

    posts_list = [post async for post in subreddit.hot(limit=500) if not post.is_self]

    random_post = random.choice(posts_list)

    return {
        "title": random_post.title,
        "description": random_post.selftext,
        "url": filter_reddit_url(random_post.url),
        "post_url": random_post.shortlink,
        "author": random_post.author.name,
        "score": random_post.score,
        "spoilers": subreddit.spoilers_enabled,
        "nsfw": subreddit.over18
    }
