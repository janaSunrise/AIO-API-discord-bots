import random

from fastapi import APIRouter

from api.app import http_client

router = APIRouter(
    prefix="/animals",
    tags=["animals"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/cat")
async def cat():
    async with http_client.session.get("https://some-random-api.ml/img/cat") as resp:
        json = await resp.json()

    return {
        "url": json["link"]
    }


@router.get("/catfact")
async def catfact():
    async with http_client.session.get("https://catfact.ninja/fact") as resp:
        json = await resp.json()

    return {
        "fact": json["fact"]
    }


@router.get("/dog")
async def dog():
    async with http_client.session.get("https://dog.ceo/api/breeds/image/random") as resp:
        json = await resp.json()

    return {
        "url": json["message"]
    }
