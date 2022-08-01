from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/lyrics",
    tags=["Song lyrics endpoint"],
    responses={
        404: {"description": "Not found"},
    },
)


@router.get("/")
async def lyrics(request: Request, song: str) -> dict:
    """Get the lyrics for some song which you need."""
    http_client = request.app.state.http_client

    async with http_client().get(
        f"https://some-random-api.ml/lyrics?title={song}"
    ) as resp:
        json = await resp.json()

    return {
        "title": json["title"],
        "author": json["author"],
        "lyrics": json["lyrics"],
        "thumbnail": json["thumbnail"]["genius"],
    }
