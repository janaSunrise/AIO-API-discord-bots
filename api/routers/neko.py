import random

from bs4 import BeautifulSoup
from fastapi import APIRouter

from api import http_client

router = APIRouter(
    prefix="/neko",
    tags=["Neko NSFW images endpoint"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Helper function --
async def neko_get(url: str):
    """Gets pictures from Neko API."""
    async with http_client.session.get("https://api.nekos.dev/api/v3/" + url) as response:
        req = await response.json()

    return req['data']['response']["url"]


# -- Router paths --
@router.get("/neko")
async def neko():
    sources = ["images/nsfw/gif/neko", "images/nsfw/img/neko_lewd", "images/nsfw/img/neko_ero"]
    url = await neko_get(random.choice(sources))

    return {
        "url": url
    }


@router.get("/lewd")
async def lewd():
    sources = ["images/nsfw/img/classic_lewd", "images/nsfw/img/neko_lewd", "images/nsfw/img/neko_ero"]
    url = await neko_get(random.choice(sources))

    return {
        "url": url
    }


@router.get("/blowjob")
async def neko_blowjob():
    sources = ["images/nsfw/gif/blow_job", "images/nsfw/img/blowjob_lewd"]
    url = await neko_get(random.choice(sources))

    return {
        "url": url
    }


@router.get("/pussy")
async def neko_pussy():
    sources = ["images/nsfw/gif/pussy_wank", "images/nsfw/gif/pussy", "images/nsfw/img/pussy_lewd"]
    url = await neko_get(random.choice(sources))

    return {
        "url": url
    }


@router.get("/cum")
async def cum():
    sources = ["images/nsfw/gif/cum", "images/nsfw/img/cum_lewd"]
    url = await neko_get(random.choice(sources))

    return {
        "url": url
    }


@router.get("/bdsm")
async def bdsm():
    url = await neko_get("images/nsfw/img/bdsm_lewd")

    return {
        "url": url
    }


@router.get("/trap")
async def trap():
    sources = ["images/nsfw/img/trap_lewd", "images/nsfw/img/futanari_lewd"]
    url = await neko_get(random.choice(sources))

    return {
        "url": url
    }


@router.get("/furry")
async def furry():
    sources = ["images/nsfw/gif/yiff", "images/nsfw/img/yiff_lewd"]
    url = await neko_get(random.choice(sources))

    return {
        "url": url
    }


@router.get("/feet")
async def feet():
    sources = ["images/nsfw/gif/feet", "images/nsfw/img/feet_lewd", "images/nsfw/img/feet_ero"]
    url = await neko_get(random.choice(sources))

    return {
        "url": url
    }


@router.get("/yuri")
async def yuri():
    sources = ["images/nsfw/gif/yuri", "images/nsfw/img/yuri_lewd", "images/nsfw/img/yuri_ero"]
    url = await neko_get(random.choice(sources))

    return {
        "url": url
    }


@router.get("/solo")
async def solo():
    sources = ["images/nsfw/gif/girls_solo", "images/nsfw/img/solo_lewd"]
    url = await neko_get(random.choice(sources))

    return {
        "url": url
    }


@router.get("/yandere")
async def yandere():
    try:
        query = "https://yande.re/post/random"
        page = await (await http_client.session.get(query)).text()
        soup = BeautifulSoup(page, 'html.parser')

        image = soup.find(id="highres").get("href")
        return {
            "url": image
        }
    except Exception as e:
        return {
            "error": e
        }


@router.get("/e621")
async def e621():
    try:
        query = "https://e621.net/post/random"
        page = await (await http_client.session.get(query)).text()
        soup = BeautifulSoup(page, 'html.parser')

        image = soup.find(id="highres").get("href")
        return {
            "url": image
        }
    except Exception as e:
        return {
            "error": e
        }


@router.get("/rule34")
async def rule34():
    try:
        query = "http://rule34.xxx/index.php?page=post&s=random"
        page = await (await http_client.session.get(query)).text()
        soup = BeautifulSoup(page, 'html.parser')

        image = soup.find(id="image").get("src")
        return {
            "url": image
        }
    except Exception as e:
        return {"error": e}


@router.get("/danbooru")
async def danbooru():
    try:
        query = "http://danbooru.donmai.us/posts/random"
        page = await (await http_client.session.get(query)).text()
        soup = BeautifulSoup(page, 'html.parser')

        image = soup.find(id="image").get("src")
        return {
            "url": image
        }
    except Exception as e:
        return {"error": e}


@router.get("/gelbooru")
async def gelbooru():
    try:
        query = "http://www.gelbooru.com/index.php?page=post&s=random"
        page = await (await http_client.session.get(query)).text()
        soup = BeautifulSoup(page, 'html.parser')

        image = soup.find(id="image").get("src")
        return {
            "url": image
        }
    except Exception as e:
        return {"error": e}


@router.get("/xbooru")
async def xbooru():
    try:
        query = "http://xbooru.com/index.php?page=post&s=random"
        page = await (await http_client.session.get(query)).text()
        soup = BeautifulSoup(page, 'html.parser')

        image = soup.find(id="image").get("src")
        return {
            "url": image
        }
    except Exception as e:
        return {"error": e}


@router.get("/lolibooru")
async def lolibooru():
    try:
        query = "https://lolibooru.moe/post/random/"
        page = await (await http_client.session.get(query)).text()
        soup = BeautifulSoup(page, 'html.parser')

        image = soup.find(id="image").get("src")
        image = image.replace(' ', '%20')
        return {
            "url": image
        }
    except Exception as e:
        return {"error": e}

