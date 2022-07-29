import random
from typing import cast

from bs4 import BeautifulSoup, Tag
from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/comics",
    tags=["Comics endpoint"],
    responses={
        404: {"description": "Not found"},
    },
)


@router.get("/ohno")
async def ohno(request: Request) -> dict:
    """Send a random 'Webcomic Name' comic."""
    http_client = request.app.state.http_client

    async with http_client().get("http://webcomicname.com/random") as response:
        soup = BeautifulSoup(await response.text(), "lxml")

    img_url = cast(dict, soup.find(property="og:image"))["content"]

    return {"url": img_url}


@router.get("/saturday-morning")
async def smbc(request: Request) -> dict:
    """Send a random 'Saturday Morning' comic."""
    http_client = request.app.state.http_client

    async with http_client().get(
        "http://www.smbc-comics.com/comic/archive",
        headers={"Connection": "keep-alive"},
    ) as response:
        soup = BeautifulSoup(await response.text(), "lxml")

    all_comics = cast(Tag, soup.find("select", attrs={"name": "comic"}))
    all_comics_url_stubs = [option["value"] for option in all_comics.findChildren()]

    random_comic = random.choice(all_comics_url_stubs)

    async with http_client.session.get(
        f"http://www.smbc-comics.com/{random_comic}",
        headers={"Connection": "keep-alive"},
    ) as resp:
        soup = BeautifulSoup(await resp.text(), "lxml")
        img_url = cast(dict, soup.find(property="og:image"))["content"]

    return {"url": img_url}


@router.get("/perry-bible")
async def perry_bible(request: Request) -> dict:
    """Send a random 'The Perry Bible' comic."""
    http_client = request.app.state.http_client

    async with http_client().get("http://pbfcomics.com/random") as response:
        soup = BeautifulSoup(await response.text(), "lxml")

    img_url = cast(dict, soup.find(property="og:image"))["content"]

    return {"url": img_url}


@router.get("/xkcd")
async def xkcd(request: Request) -> dict:
    """See a random 'xkcd' comic."""
    http_client = request.app.state.http_client

    async with http_client().get("https://xkcd.com/info.0.json") as response:
        data = await response.json()

    random_comic = random.randint(1, data["num"])

    async with http_client().get(
        f"https://xkcd.com/{random_comic}/info.0.json"
    ) as response:
        if response.status == 200:
            data = await response.json()

    return {"url": data["img"]}


@router.get("/mrls")
async def mrls(request: Request) -> dict:
    """Send a random 'Mr. Lovenstein' comic."""
    http_client = request.app.state.http_client

    async with http_client().get("http://www.mrlovenstein.com/shuffle") as response:
        soup = BeautifulSoup(await response.text(), "lxml")

    img_url = (
        "http://www.mrlovenstein.com"
        + cast(dict, soup.find(id="comic_main_image"))["src"]  # noqa: W503
    )

    return {"url": img_url}


@router.get("/chainsaw")
async def chainsaw(request: Request) -> dict:
    """Send a random 'Chainsawsuit' comic."""
    http_client = request.app.state.http_client

    async with http_client().get(
        "http://chainsawsuit.com/comic/random/?random&nocache=1"
    ) as response:
        soup = BeautifulSoup(await response.text(), "lxml")

    img_url = cast(dict, soup.find(property="og:image"))["content"]

    return {"url": img_url}


@router.get("/sarah")
async def sarah(request: Request) -> dict:
    """Send a random 'Sarah's Scribbles' comic."""
    http_client = request.app.state.http_client

    async with http_client().get(
        "http://www.gocomics.com/random/sarahs-scribbles"
    ) as response:
        soup = BeautifulSoup(await response.text(), "lxml")

    img_url = cast(dict, soup.find(property="og:image"))["content"]

    return {"url": img_url}


@router.get("/garfield")
async def garfield(request: Request) -> dict:
    """Send a random 'garfield' comic."""
    http_client = request.app.state.http_client

    async with http_client().get(
        "https://many-api.vercel.app/garfield/random"
    ) as response:
        img_url = (await response.json())["url"]

    return {"url": img_url}
