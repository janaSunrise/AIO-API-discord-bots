from fastapi import APIRouter

from api.app import http_client

router = APIRouter(
    prefix="/fun",
    tags=["fun"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/joke")
async def joke(explicit: bool = False):
    if explicit:
        url = "http://api.icndb.com/jokes/random"
    else:
        url = "http://api.icndb.com/jokes/random?exclude=[explicit]"

    async with http_client.session.get(url) as resp:
        json = await resp.json()

    return {
        "joke": json["value"]["joke"].replace("&quote", '"')
    }


@router.get("/chucknorris")
async def chucknorris():
    async with http_client.session.get("https://api.chucknorris.io/jokes/random") as resp:
        json = await resp.json()

    return {
        "joke": json["value"]
    }
