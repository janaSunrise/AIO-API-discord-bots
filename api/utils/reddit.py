import random

from ..config import RedditConfig


def filter_reddit_url(url) -> str:
    if not url.startswith("https://v.redd.it/") or url.startswith(
        "https://youtube.com/"
    ):
        if url.startswith(RedditConfig.IMGUR_LINKS):
            if url.endswith(".mp4"):
                url = url[:-3] + "gif"
            elif url.endswith(".gifv"):
                url = url[:-1]
            elif url.endswith(RedditConfig.ACCEPTED_EXTENSIONS):
                pass
            else:
                url = url + ".png"
        elif url.startswith("https://gfycat.com/"):
            url_cut = url.replace("https://gfycat.com/", "")

            url = f"https://thumbs.gfycat.com/{url_cut}-size_restricted.gif"

    return url


async def get_random_post(subreddit) -> dict:
    random_post = random.choice(
        [post async for post in subreddit.hot() if not post.is_self]
    )

    return {
        "title": random_post.title,
        "description": random_post.selftext,
        "url": filter_reddit_url(random_post.url),
        "post_url": random_post.shortlink,
        "author": random_post.author.name,
        "score": random_post.score,
        "spoilers": subreddit.spoilers_enabled,
        "nsfw": subreddit.over18,
    }
