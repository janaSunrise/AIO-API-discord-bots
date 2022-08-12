from __future__ import annotations

import random

from fastapi import APIRouter, Request

from ..config import APIConfig

router = APIRouter(
    prefix="/nasa",
    tags=["NASA endpoint"],
    responses={
        404: {"description": "Not found"},
    },
)

NASA_API = APIConfig.NASA_API


@router.get("/apod")
async def apod(request: Request) -> dict[str, str]:
    """Get the astronomy picture of the day."""
    http_client = request.app.state.http_client

    async with http_client().get(
        f"https://api.nasa.gov/planetary/apod?api_key={NASA_API}"
    ) as resp:
        data = await resp.json()

    return {
        "title": data["title"],
        "explanation": data["explanation"],
        "img": data["hdurl"],
    }


@router.get("/nasa-search")
async def nasa_search(request: Request, query: str) -> dict[str, str]:
    """Lookup nasa for your queries."""
    http_client = request.app.state.http_client

    async with http_client().get(
        f"https://images-api.nasa.gov/search?q={query}"
    ) as resp:
        data = await resp.json()

    items = data["collection"]["items"]

    if len(items) > 0:
        rand_item = random.randint(0, len(items) - 1)
        item = items[rand_item]

        return {
            "description": item["data"][0]["description"],
            "img": item["links"][0]["href"],
            "id": item["data"][0]["nasa_id"],
        }

    return {"error": "No results found!"}


@router.get("/epic")
async def epic(request: Request, maximum: int = 1) -> dict[str, list[dict[str, str]]]:
    """Get to know about a nasa EPIC."""
    http_client = request.app.state.http_client

    async with http_client().get(
        "https://epic.gsfc.nasa.gov/api/images.php"
    ) as response:
        json = await response.json()

    result = []

    for i in range(min(maximum, len(json))):
        result.append(
            {
                "description": json[i].get("caption"),
                "img": (
                    "https://epic.gsfc.nasa.gov/epic-archive/jpg/"
                    + json[i]["image"]  # noqa: W503
                    + ".jpg"  # noqa: W503
                ),
            }
        )

    return {"result": result}
