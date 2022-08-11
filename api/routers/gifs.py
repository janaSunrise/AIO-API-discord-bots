from __future__ import annotations

from fastapi import APIRouter, Request

from api.utils.http_client import HTTPClient

router = APIRouter(
    prefix="/gifs",
    tags=["GIF generation endpoints"],
    responses={
        404: {"description": "Not found"},
    },
)


async def dispatch_gif_url(http_client: HTTPClient, typ: str) -> dict[str, str]:
    async with http_client().get(f"https://some-random-api.ml/animu/{typ}") as resp:
        json = await resp.json()

    return {"url": json["link"]}


@router.get("/wink")
async def wink(request: Request) -> dict[str, str]:
    """Get a random wink gif."""
    http_client = request.app.state.http_client

    return await dispatch_gif_url(http_client, "wink")


@router.get("/pat")
async def pat(request: Request) -> dict[str, str]:
    """Get a random pat gif."""
    http_client = request.app.state.http_client

    return await dispatch_gif_url(http_client, "pat")


@router.get("/hug")
async def hug(request: Request) -> dict[str, str]:
    """Get a random hug gif."""
    http_client = request.app.state.http_client

    return await dispatch_gif_url(http_client, "hug")
