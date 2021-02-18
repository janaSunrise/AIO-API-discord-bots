import random

from bs4 import BeautifulSoup
from fastapi import APIRouter, Request

from api import http_client
from api.core import log_error

router = APIRouter(
    prefix="/neko",
    tags=["Neko NSFW images endpoint"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Helper function --
async def neko_get(url: str) -> str:
    """Gets pictures from Neko API."""
    async with http_client.session.get("https://api.nekos.dev/api/v3/" + url) as response:
        req = await response.json()

    return req['data']['response']["url"]


# -- Router paths --
@router.get("/neko")
@log_error()
async def neko(request: Request) -> dict:
    sources = ["images/nsfw/gif/neko", "images/nsfw/img/neko_lewd", "images/nsfw/img/neko_ero"]
    url = await neko_get(random.choice(sources))

    return {"url": url}


@router.get("/lewd")
@log_error()
async def lewd(request: Request) -> dict:
    sources = ["images/nsfw/img/classic_lewd", "images/nsfw/img/neko_lewd", "images/nsfw/img/neko_ero"]
    url = await neko_get(random.choice(sources))

    return {"url": url}


@router.get("/blowjob")
@log_error()
async def neko_blowjob(request: Request) -> dict:
    sources = ["images/nsfw/gif/blow_job", "images/nsfw/img/blowjob_lewd"]
    url = await neko_get(random.choice(sources))

    return {"url": url}


@router.get("/pussy")
@log_error()
async def neko_pussy(request: Request) -> dict:
    sources = ["images/nsfw/gif/pussy_wank", "images/nsfw/gif/pussy", "images/nsfw/img/pussy_lewd"]
    url = await neko_get(random.choice(sources))

    return {"url": url}


@router.get("/cum")
@log_error()
async def cum(request: Request) -> dict:
    sources = ["images/nsfw/gif/cum", "images/nsfw/img/cum_lewd"]
    url = await neko_get(random.choice(sources))

    return {"url": url}


@router.get("/bdsm")
@log_error()
async def bdsm(request: Request) -> dict:
    url = await neko_get("images/nsfw/img/bdsm_lewd")

    return {"url": url}


@router.get("/trap")
@log_error()
async def trap(request: Request) -> dict:
    sources = ["images/nsfw/img/trap_lewd", "images/nsfw/img/futanari_lewd"]
    url = await neko_get(random.choice(sources))

    return {"url": url}


@router.get("/furry")
@log_error()
async def furry(request: Request) -> dict:
    sources = ["images/nsfw/gif/yiff", "images/nsfw/img/yiff_lewd"]
    url = await neko_get(random.choice(sources))

    return {"url": url}


@router.get("/feet")
@log_error()
async def feet(request: Request) -> dict:
    sources = ["images/nsfw/gif/feet", "images/nsfw/img/feet_lewd", "images/nsfw/img/feet_ero"]
    url = await neko_get(random.choice(sources))

    return {"url": url}


@router.get("/yuri")
@log_error()
async def yuri(request: Request) -> dict:
    sources = ["images/nsfw/gif/yuri", "images/nsfw/img/yuri_lewd", "images/nsfw/img/yuri_ero"]
    url = await neko_get(random.choice(sources))

    return {"url": url}


@router.get("/solo")
@log_error()
async def solo(request: Request) -> dict:
    sources = ["images/nsfw/gif/girls_solo", "images/nsfw/img/solo_lewd"]
    url = await neko_get(random.choice(sources))

    return {"url": url}


@router.get("/yandere")
@log_error()
async def yandere(request: Request) -> dict:
    query = "https://yande.re/post/random"
    page = await (await http_client.session.get(query)).text()
    soup = BeautifulSoup(page, 'html.parser')

    image = soup.find(id="highres").get("href")
    return {"url": image}


@router.get("/e621")
@log_error()
async def e621(request: Request) -> dict:
    query = "https://e621.net/post/random"
    page = await (await http_client.session.get(query)).text()
    soup = BeautifulSoup(page, 'html.parser')

    image = soup.find(id="highres").get("href")
    return {"url": image}


@router.get("/rule34")
@log_error()
async def rule34(request: Request) -> dict:
    query = "http://rule34.xxx/index.php?page=post&s=random"
    page = await (await http_client.session.get(query)).text()
    soup = BeautifulSoup(page, 'html.parser')

    image = soup.find(id="image").get("src")
    return {"url": image}


@router.get("/danbooru")
@log_error()
async def danbooru(request: Request) -> dict:
    query = "http://danbooru.donmai.us/posts/random"
    page = await (await http_client.session.get(query)).text()
    soup = BeautifulSoup(page, 'html.parser')

    image = soup.find(id="image").get("src")
    return {"url": image}


@router.get("/gelbooru")
@log_error()
async def gelbooru(request: Request) -> dict:
    query = "http://www.gelbooru.com/index.php?page=post&s=random"
    page = await (await http_client.session.get(query)).text()
    soup = BeautifulSoup(page, 'html.parser')

    image = soup.find(id="image").get("src")
    return {"url": image}


@router.get("/xbooru")
@log_error()
async def xbooru(request: Request) -> dict:
    query = "http://xbooru.com/index.php?page=post&s=random"
    page = await (await http_client.session.get(query)).text()
    soup = BeautifulSoup(page, 'html.parser')

    image = soup.find(id="image").get("src")
    return {"url": image}


@router.get("/lolibooru")
@log_error()
async def lolibooru(request: Request) -> dict:
    query = "https://lolibooru.moe/post/random/"
    page = await (await http_client.session.get(query)).text()
    soup = BeautifulSoup(page, 'html.parser')

    image = soup.find(id="image").get("src")
    image = image.replace(' ', '%20')
    return {"url": image}

