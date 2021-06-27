import random

from bs4 import BeautifulSoup
from fastapi import APIRouter, Request

from api.core import log_error

router = APIRouter(
    prefix="/comics",
    tags=["Comics endpoint"],
    responses={404: {"description": "Not found"},},
)


# -- Router paths --
@router.get("/ohno")
@log_error()
async def ohno(request: Request) -> dict:
    """Send a random 'Webcomic Name' comic."""
    url = "http://webcomicname.com/random"
    http_client = request.app.state.http_client

    async with http_client.session.get(url) as response:
        soup = BeautifulSoup(await response.text(), "html.parser")

    img_url = soup.find(property="og:image")["content"]

    return {"url": img_url}


@router.get("/saturday-morning")
@log_error()
async def smbc(request: Request) -> dict:
    """Send a random 'Saturday Morning' comic."""
    url = "http://www.smbc-comics.com/comic/archive"
    http_client = request.app.state.http_client

    async with http_client.session.get(
        url, headers={"Connection": "keep-alive"},
    ) as response:
        soup = BeautifulSoup(await response.text(), "html.parser")

    all_comics = soup.find("select", attrs={"name": "comic"})
    all_comics_url_stubs = [option["value"] for option in all_comics.findChildren()]

    random_comic = random.choice(all_comics_url_stubs)
    comic_url = f"http://www.smbc-comics.com/{random_comic}"

    async with http_client.session.get(
        comic_url, headers={"Connection": "keep-alive"},
    ) as resp:
        soup = BeautifulSoup(await resp.text(), "html.parser")
        img_url = soup.find(property="og:image")["content"]

    return {"url": img_url}


@router.get("/perry-bible")
@log_error()
async def perry_bible(request: Request) -> dict:
    """Send a random 'The Perry Bible' comic."""
    url = "http://pbfcomics.com/random"
    http_client = request.app.state.http_client

    async with http_client.session.get(url) as response:
        soup = BeautifulSoup(await response.text(), "html.parser")

    img_url = soup.find(property="og:image")["content"]

    return {"url": img_url}


@router.get("/cah")
@log_error()
async def cah(request: Request) -> dict:
    """Send a random 'Cyanide and Happiness' comic."""
    url = "http://explosm.net/comics/random"
    http_client = request.app.state.http_client

    async with http_client.session.get(url) as response:
        soup = BeautifulSoup(await response.text(), "html.parser")

    img_url = soup.find(property="og:image")["content"]

    return {"url": img_url}


@router.get("/xkcd")
@log_error()
async def xkcd(request: Request) -> dict:
    """See a random 'xkcd' comic."""
    url = "https://xkcd.com/info.0.json"
    http_client = request.app.state.http_client

    async with http_client.session.get(url) as response:
        data = await response.json()

    random_comic = random.randint(1, data["num"])

    url = f"https://xkcd.com/{random_comic}/info.0.json"

    async with http_client.session.get(url) as response:
        if response.status == 200:
            data = await response.json()

    return {"url": data["img"]}


@router.get("/mrls")
@log_error()
async def mrls(request: Request) -> dict:
    """Send a random 'Mr. Lovenstein' comic."""
    url = "http://www.mrlovenstein.com/shuffle"
    http_client = request.app.state.http_client

    async with http_client.session.get(url) as response:
        soup = BeautifulSoup(await response.text(), "html.parser")

    img_url = "http://www.mrlovenstein.com" + soup.find(id="comic_main_image")["src"]

    return {"url": img_url}


@router.get("/chainsaw")
@log_error()
async def chainsaw(request: Request) -> dict:
    """Send a random 'Chainsawsuit' comic."""
    url = "http://chainsawsuit.com/comic/random/?random&nocache=1"
    http_client = request.app.state.http_client

    async with http_client.session.get(url) as response:
        soup = BeautifulSoup(await response.text(), "html.parser")

    img_url = soup.find(property="og:image")["content"]

    return {"url": img_url}


@router.get("/sarah")
@log_error()
async def sarah(request: Request) -> dict:
    """Send a random 'Sarah's Scribbles' comic."""
    url = "http://www.gocomics.com/random/sarahs-scribbles"
    http_client = request.app.state.http_client

    async with http_client.session.get(url) as response:
        soup = BeautifulSoup(await response.text(), "html.parser")

    img_url = soup.find(property="og:image")["content"]

    return {"url": img_url}


@router.get("/garfield")
@log_error()
async def garfield(request: Request) -> dict:
    """Send a random 'garfield' comic."""
    url = "https://many-api.vercel.app/garfield/random"
    http_client = request.app.state.http_client

    async with http_client.session.get(url) as response:
        img_url = (await response.json())["url"]

    return {"url": img_url}
