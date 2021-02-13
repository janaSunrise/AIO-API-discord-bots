import random
import json

from api.config import IMGUR_LINKS, ACCEPTED_EXTENSIONS


def filter_reddit_url(url) -> str:
    if not url.startswith("https://v.redd.it/") or url.startswith("https://youtube.com/"):
        if url.startswith(IMGUR_LINKS):
            if url.endswith(".mp4"):
                url = url[:-3] + "gif"
            elif url.endswith(".gifv"):
                url = url[:-1]
            elif url.endswith(ACCEPTED_EXTENSIONS):
                url = url
            else:
                url = url + ".png"
        elif url.startswith("https://gfycat.com/"):
            url_cut = url.replace("https://gfycat.com/", "")

            url = f"https://thumbs.gfycat.com/{url_cut}-size_restricted.gif"
        elif url.endswith(ACCEPTED_EXTENSIONS):
            url = url

    return url


async def get_random_post(subreddit):
    random_post = random.choice(
        [post async for post in subreddit.hot(limit=500) if not post.is_self]
    )

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


def get_random_text_response(category: str):
    with open("api/assets/text_games_response.json") as file:
        data = json.load(file)

    data = data[category]

    return random.choice(data)
