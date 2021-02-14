from fastapi import APIRouter

from api import http_client

router = APIRouter(
    prefix="/lyrics",
    tags=["lyrics"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/")
async def lyrics(songname: str):
    """Get the lyrics for some song which you need."""
    async with http_client.session.get(f"https://some-random-api.ml/lyrics?title={songname}") as resp:
        json = await resp.json()

    return {
        "title": json["title"],
        "author": json["author"],
        "lyrics": json["lyrics"],
        "thumbnail": json["thumbnail"]["genius"]
    }

