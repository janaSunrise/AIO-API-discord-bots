from fastapi import APIRouter

from api import http_client
from api.core import log_error

router = APIRouter(
    prefix="/animals",
    tags=["Images of animals"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/cat")
@log_error()
async def cat():
    async with http_client.session.get("https://some-random-api.ml/img/cat") as resp:
        json = await resp.json()

    return {
        "url": json["link"]
    }


@router.get("/catfact")
@log_error()
async def catfact():
    async with http_client.session.get("https://some-random-api.ml/facts/cat") as resp:
        json = await resp.json()

    return {
        "fact": json["fact"]
    }


@router.get("/dog")
@log_error()
async def dog():
    async with http_client.session.get("https://dog.ceo/api/breeds/image/random") as resp:
        json = await resp.json()

    return {
        "url": json["message"]
    }


@router.get("/dogfact")
@log_error()
async def dogfact():
    async with http_client.session.get("https://some-random-api.ml/facts/dog") as resp:
        json = await resp.json()

    return {
        "fact": json["fact"]
    }


@router.get("/pandafact")
@log_error()
async def pandafact():
    async with http_client.session.get("https://some-random-api.ml/facts/panda") as resp:
        json = await resp.json()

    return {
        "fact": json["fact"]
    }


@router.get("/fox")
@log_error()
async def fox():
    async with http_client.session.get("https://randomfox.ca/floof/") as resp:
        json = await resp.json()

    return {
        "url": json["image"]
    }


@router.get("/panda")
@log_error()
async def panda():
    async with http_client.session.get("https://some-random-api.ml/img/panda") as resp:
        json = await resp.json()

    return {
        "url": json["link"]
    }


@router.get("/koala")
@log_error()
async def koala():
    async with http_client.session.get("https://some-random-api.ml/img/koala") as resp:
        json = await resp.json()

    return {
        "url": json["link"]
    }


@router.get("/birb")
@log_error()
async def birb():
    async with http_client.session.get("https://some-random-api.ml/img/birb") as resp:
        json = await resp.json()

    return {
        "url": json["link"]
    }


@router.get("/duck")
@log_error()
async def duck():
    async with http_client.session.get("https://random-d.uk/api/v2/random") as resp:
        json = await resp.json()

    return {
        "url": json["url"]
    }
