from fastapi import APIRouter

from api import http_client
from api.core import log_error

router = APIRouter(
    prefix="/gifs",
    tags=["GIF makers"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/wink")
@log_error()
async def wink() -> dict:
    async with http_client.session.get("https://some-random-api.ml/animu/wink") as resp:
        json = await resp.json()

    return {"url": json["link"]}


@router.get("/pat")
@log_error()
async def pat() -> dict:
    async with http_client.session.get("https://some-random-api.ml/animu/pat") as resp:
        json = await resp.json()

    return {"url": json["link"]}


@router.get("/hug")
@log_error()
async def hug() -> dict:
    async with http_client.session.get("https://some-random-api.ml/animu/hug") as resp:
        json = await resp.json()

    return {"url": json["link"]}
