from fastapi import APIRouter, Request

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
async def cat(_: Request) -> dict:
    """Get a random cat image."""
    async with http_client.session.get(
        "https://some-random-api.ml/img/cat"
    ) as resp:
        json = await resp.json()

    return {"url": json["link"]}


@router.get("/catfact")
@log_error()
async def cat_fact(_: Request) -> dict:
    """Get a random cat fact."""
    async with http_client.session.get(
        "https://some-random-api.ml/facts/cat"
    ) as resp:
        json = await resp.json()

    return {"fact": json["fact"]}


@router.get("/dog")
@log_error()
async def dog(_: Request) -> dict:
    async with http_client.session.get(
        "https://dog.ceo/api/breeds/image/random"
    ) as resp:
        json = await resp.json()

    return {"url": json["message"]}


@router.get("/dogfact")
@log_error()
async def dog_fact(_: Request) -> dict:
    """Get a random dog image."""
    async with http_client.session.get(
        "https://some-random-api.ml/facts/dog"
    ) as resp:
        json = await resp.json()

    return {"fact": json["fact"]}


@router.get("/pandafact")
@log_error()
async def panda_fact(_: Request) -> dict:
    """Get a random interesting fact about pandas."""
    async with http_client.session.get(
        "https://some-random-api.ml/facts/panda"
    ) as resp:
        json = await resp.json()

    return {"fact": json["fact"]}


@router.get("/fox")
@log_error()
async def fox(_: Request) -> dict:
    """Get a random fox image."""
    async with http_client.session.get(
        "https://randomfox.ca/floof/"
    ) as resp:
        json = await resp.json()

    return {"url": json["image"]}


@router.get("/panda")
@log_error()
async def panda(_: Request) -> dict:
    """Get a random panda image."""
    async with http_client.session.get(
        "https://some-random-api.ml/img/panda"
    ) as resp:
        json = await resp.json()

    return {"url": json["link"]}


@router.get("/koala")
@log_error()
async def koala(_: Request) -> dict:
    """Get a random koala image."""
    async with http_client.session.get(
        "https://some-random-api.ml/img/koala"
    ) as resp:
        json = await resp.json()

    return {"url": json["link"]}


@router.get("/birb")
@log_error()
async def birb(_: Request) -> dict:
    """Get a random bird image."""
    async with http_client.session.get(
        "https://some-random-api.ml/img/birb"
    ) as resp:
        json = await resp.json()

    return {"url": json["link"]}


@router.get("/duck")
@log_error()
async def duck(_: Request) -> dict:
    """Get a random duck image."""
    async with http_client.session.get(
        "https://random-d.uk/api/v2/random"
    ) as resp:
        json = await resp.json()

    return {"url": json["url"]}
