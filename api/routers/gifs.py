from fastapi import APIRouter

from api.app import http_client

router = APIRouter(
    prefix="/gifs",
    tags=["gifs"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/wink")
async def wink():
    async with http_client.session.get("https://some-random-api.ml/animu/wink") as resp:
        json = await resp.json()

    return {
        "url": json["link"]
    }


@router.get("/pat")
async def pat():
    async with http_client.session.get("https://some-random-api.ml/animu/pat") as resp:
        json = await resp.json()

    return {
        "url": json["link"]
    }


@router.get("/hug")
async def hug():
    async with http_client.session.get("https://some-random-api.ml/animu/hug") as resp:
        json = await resp.json()

    return {
        "url": json["link"]
    }
