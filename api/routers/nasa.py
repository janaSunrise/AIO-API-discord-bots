import random

from fastapi import APIRouter

from api import http_client
from api.config import nasa_api as NASA_API

router = APIRouter(
    prefix="/nasa",
    tags=["Nasa info and images"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/apod")
async def apod():
    async with http_client.session.get(f"https://api.nasa.gov/planetary/apod?api_key={NASA_API}") as resp:
        data = await resp.json()

    return {
        "title": data["title"],
        "explanation": data["explanation"],
        "img": data["hdurl"]
    }


@router.get("/nasa-search")
async def nasa_search(query: str):
    async with http_client.session.get(f"https://images-api.nasa.gov/search?q={query}") as resp:
        data = await resp.json()

    items = data["collection"]["items"]
    if len(items) > 0:
        rand_item = random.randint(0, len(items) - 1)
        item = items[rand_item]

        return {
            "description": item["data"][0]["description"],
            "img": item["links"][0]["href"],
            "id": item['data'][0]['nasa_id']
        }
    else:
        return {
            "error": "No results found!"
        }


@router.get("/epic")
async def epic(max: int = 1):
    async with http_client.session.get("https://epic.gsfc.nasa.gov/api/images.php") as response:
        json = await response.json()

    result = {}

    for i in range(min(max, len(json))):
        result[i] = {
            "description": json[i].get("caption"),
            "img": "https://epic.gsfc.nasa.gov/epic-archive/jpg/" + json[i]["image"] + ".jpg"
        }

    return result