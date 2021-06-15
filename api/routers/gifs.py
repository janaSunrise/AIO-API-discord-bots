from fastapi import APIRouter, Request

from api.core import log_error

router = APIRouter(
    prefix="/gifs", tags=["GIF makers"], responses={404: {"description": "Not found"},},
)


# -- Router paths --
@router.get("/wink")
@log_error()
async def wink(request: Request) -> dict:
    """Get a random wink gif."""
    http_client = request.app.state.http_client

    async with http_client.session.get("https://some-random-api.ml/animu/wink") as resp:
        json = await resp.json()

    return {"url": json["link"]}


@router.get("/pat")
@log_error()
async def pat(request: Request) -> dict:
    """Get a random pat gif."""
    http_client = request.app.state.http_client

    async with http_client.session.get("https://some-random-api.ml/animu/pat") as resp:
        json = await resp.json()

    return {"url": json["link"]}


@router.get("/hug")
@log_error()
async def hug(request: Request) -> dict:
    """Get a random hug gif."""
    http_client = request.app.state.http_client

    async with http_client.session.get("https://some-random-api.ml/animu/hug") as resp:
        json = await resp.json()

    return {"url": json["link"]}
