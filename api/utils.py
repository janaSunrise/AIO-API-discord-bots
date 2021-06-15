import json
import random
import urllib

from api.config import (
    ACCEPTED_EXTENSIONS,
    DEFAULT_OUTPUT_FORMAT,
    IMGUR_LINKS,
    MAX_PODS,
    QUERY,
)

with open("api/assets/text_games_response.json") as file:
    TEXT_GAMES_RESPONSE = json.load(file)


def filter_reddit_url(url) -> str:
    if not url.startswith("https://v.redd.it/") or url.startswith(
        "https://youtube.com/"
    ):
        if url.startswith(IMGUR_LINKS):
            if url.endswith(".mp4"):
                url = url[:-3] + "gif"
            elif url.endswith(".gifv"):
                url = url[:-1]
            elif url.endswith(ACCEPTED_EXTENSIONS):
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


def get_random_text_response(category: str) -> str:
    data = TEXT_GAMES_RESPONSE[category]

    return random.choice(data)


async def get_pod_pages(http_client, appid: str, query: str):
    """Get the Wolfram API pod pages for the provided query."""
    url_str = urllib.parse.urlencode(
        {
            "input": query,
            "appid": appid,
            "output": DEFAULT_OUTPUT_FORMAT,
            "format": "image,plaintext",
            "location": "the moon",
            "latlong": "0.0,0.0",
            "ip": "1.1.1.1",
        }
    )
    request_url = QUERY.format(request="query", data=url_str)

    async with http_client.session.get(request_url) as response:
        data = await response.json(content_type="text/plain")

    result = data["queryresult"]

    if result["error"]:
        if result["error"]["msg"] == "Invalid appid":
            message = "Wolfram API key is invalid or missing."
            return {"error": message}

        message = (
            "Something went wrong internally with your request, please notify staff!"
        )
        return {"error": message}

    if not result["success"]:
        message = f"I couldn't find anything for {query}."
        return {"error": message}

    if not result["numpods"]:
        message = "Could not find any results."
        return {"error": message}

    pods = result["pods"]
    pages = []
    for pod in pods[:MAX_PODS]:
        subs = pod.get("subpods")

        for sub in subs:
            title = sub.get("title") or sub.get("plaintext") or sub.get("id", "")
            img = sub["img"]["src"]
            pages.append((title, img))

    return pages
