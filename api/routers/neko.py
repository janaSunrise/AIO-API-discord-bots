from __future__ import annotations

import random
from typing import cast

from bs4 import BeautifulSoup
from fastapi import APIRouter, Request

from ..utils.http_client import HTTPClient

router = APIRouter(
    prefix="/neko",
    tags=["Neko NSFW images endpoint"],
    responses={
        404: {"description": "Not found"},
    },
)


async def neko_get(http_client: HTTPClient, url: str) -> str:
    """Gets pictures from Neko API."""
    async with http_client().get(f"https://api.nekos.dev/api/v3/{url}") as response:
        req = await response.json()

    return req["data"]["response"]["url"]


@router.get("/neko")
async def neko(request: Request) -> dict[str, str]:
    http_client = request.app.state.http_client
    sources = (
        "images/nsfw/gif/neko",
        "images/nsfw/img/neko_lewd",
        "images/nsfw/img/neko_ero",
    )
    url = await neko_get(http_client, random.choice(sources))

    return {"url": url}


@router.get("/lewd")
async def lewd(request: Request) -> dict[str, str]:
    http_client = request.app.state.http_client
    sources = (
        "images/nsfw/img/classic_lewd",
        "images/nsfw/img/neko_lewd",
        "images/nsfw/img/neko_ero",
    )
    url = await neko_get(http_client, random.choice(sources))

    return {"url": url}


@router.get("/blowjob")
async def blowjob(request: Request) -> dict[str, str]:
    http_client = request.app.state.http_client
    sources = ("images/nsfw/gif/blow_job", "images/nsfw/img/blowjob_lewd")
    url = await neko_get(http_client, random.choice(sources))

    return {"url": url}


@router.get("/pussy")
async def pussy(request: Request) -> dict[str, str]:
    http_client = request.app.state.http_client
    sources = (
        "images/nsfw/gif/pussy_wank",
        "images/nsfw/gif/pussy",
        "images/nsfw/img/pussy_lewd",
    )
    url = await neko_get(http_client, random.choice(sources))

    return {"url": url}


@router.get("/cum")
async def cum(request: Request) -> dict[str, str]:
    http_client = request.app.state.http_client
    sources = ("images/nsfw/gif/cum", "images/nsfw/img/cum_lewd")
    url = await neko_get(http_client, random.choice(sources))

    return {"url": url}


@router.get("/bdsm")
async def bdsm(request: Request) -> dict[str, str]:
    http_client = request.app.state.http_client
    url = await neko_get(http_client, "images/nsfw/img/bdsm_lewd")

    return {"url": url}


@router.get("/trap")
async def trap(request: Request) -> dict[str, str]:
    http_client = request.app.state.http_client
    sources = ("images/nsfw/img/trap_lewd", "images/nsfw/img/futanari_lewd")
    url = await neko_get(http_client, random.choice(sources))

    return {"url": url}


@router.get("/furry")
async def furry(request: Request) -> dict[str, str]:
    http_client = request.app.state.http_client
    sources = ("images/nsfw/gif/yiff", "images/nsfw/img/yiff_lewd")
    url = await neko_get(http_client, random.choice(sources))

    return {"url": url}


@router.get("/feet")
async def feet(request: Request) -> dict[str, str]:
    http_client = request.app.state.http_client
    sources = (
        "images/nsfw/gif/feet",
        "images/nsfw/img/feet_lewd",
        "images/nsfw/img/feet_ero",
    )
    url = await neko_get(http_client, random.choice(sources))

    return {"url": url}


@router.get("/yuri")
async def yuri(request: Request) -> dict[str, str]:
    http_client = request.app.state.http_client
    sources = (
        "images/nsfw/gif/yuri",
        "images/nsfw/img/yuri_lewd",
        "images/nsfw/img/yuri_ero",
    )
    url = await neko_get(http_client, random.choice(sources))

    return {"url": url}


@router.get("/solo")
async def solo(request: Request) -> dict[str, str]:
    http_client = request.app.state.http_client
    sources = ("images/nsfw/gif/girls_solo", "images/nsfw/img/solo_lewd")
    url = await neko_get(http_client, random.choice(sources))

    return {"url": url}


@router.get("/yandere")
async def yandere(request: Request) -> dict[str, str]:
    http_client = request.app.state.http_client

    page = await (await http_client().get("https://yande.re/post/random")).text()

    soup = BeautifulSoup(page, "html.parser")
    image = cast(dict, soup.find(id="highres"))["href"]

    return {"url": image}


@router.get("/e621")
async def e621(request: Request) -> dict[str, str]:
    http_client = request.app.state.http_client

    page = await (await http_client().get("https://e621.net/post/random")).text()

    soup = BeautifulSoup(page, "html.parser")
    image = cast(dict, soup.find(id="highres"))["href"]

    return {"url": image}


@router.get("/rule34")
async def rule34(request: Request) -> dict[str, str]:
    http_client = request.app.state.http_client

    page = await (
        await http_client().get("http://rule34.xxx/index.php?page=post&s=random")
    ).text()

    soup = BeautifulSoup(page, "html.parser")
    image = cast(dict, soup.find(id="image"))["src"]

    return {"url": image}


@router.get("/danbooru")
async def danbooru(request: Request) -> dict[str, str]:
    http_client = request.app.state.http_client

    page = await (
        await http_client().get("http://danbooru.donmai.us/posts/random")
    ).text()

    soup = BeautifulSoup(page, "html.parser")
    image = cast(dict, soup.find(id="image"))["src"]

    return {"url": image}


@router.get("/gelbooru")
async def gelbooru(request: Request) -> dict[str, str]:
    http_client = request.app.state.http_client

    page = await (
        await http_client().get("http://www.gelbooru.com/index.php?page=post&s=random")
    ).text()

    soup = BeautifulSoup(page, "html.parser")
    image = cast(dict, soup.find(id="image"))["src"]

    return {"url": image}


@router.get("/xbooru")
async def xbooru(request: Request) -> dict[str, str]:
    http_client = request.app.state.http_client

    page = await (
        await http_client().get("http://xbooru.com/index.php?page=post&s=random")
    ).text()

    soup = BeautifulSoup(page, "html.parser")
    image = cast(dict, soup.find(id="image"))["src"]

    return {"url": image}


@router.get("/lolibooru")
async def lolibooru(request: Request) -> dict[str, str]:
    http_client = request.app.state.http_client

    page = await (await http_client().get("https://lolibooru.moe/post/random/")).text()

    soup = BeautifulSoup(page, "html.parser")
    image = cast(dict, soup.find(id="image"))["src"]
    image = image.replace(" ", "%20")

    return {"url": image}
