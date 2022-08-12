from __future__ import annotations

from html import unescape
from urllib.parse import quote_plus

import html2text
from fastapi import APIRouter, Request

from api.config import APIConfig
from api.utils.http_client import HTTPClient

router = APIRouter(
    prefix="/search",
    tags=["Searching endpoint"],
    responses={
        404: {"description": "Not found"},
    },
)


class Search:
    def __init__(self) -> None:
        self.tomd = html2text.HTML2Text()
        self.tomd.ignore_links = True
        self.tomd.ignore_images = True
        self.tomd.ignore_tables = True
        self.tomd.ignore_emphasis = True
        self.tomd.body_width = 0

    @staticmethod
    async def _search_logic(
        http_client: HTTPClient,
        query: str,
        category: str = "web",
        count: int = 5,
    ) -> list:
        """Use scrapestack and the Qwant API to find search results."""
        base = "https://api.qwant.com/api"

        url = (
            f"{base}/search/{category}"
            f"?count={count}"
            f"&q={query.replace(' ', '+')}"
            f"&t=web&locale=en_US&uiv=4"
        )

        async with http_client().get(
            url, headers={"User-Agent": APIConfig.USER_AGENT}
        ) as resp:
            json_data = await resp.json()

        return json_data["data"]["result"]["items"]

    async def basic_search(
        self, http_client: HTTPClient, query: str, category: str, count: int
    ) -> dict[str, list[str] | dict[str, str]] | dict[str, str]:
        results = await self._search_logic(http_client, query, category, count=count)

        count = len(results)

        # Return if no results
        if not count:
            return {"error": f"No results found for `{query}`."}

        # Gets the first entry's data
        first_dict = {
            "title": self.tomd.handle(results[0]["title"]).rstrip("\n").strip("<>"),
            "description": self.tomd.handle(results[0]["desc"]).rstrip("\n"),
            "url": results[0]["url"],
        }

        # Builds the substring for each of the other result.
        other_results = []

        for result in results[1:count]:
            title = self.tomd.handle(result["title"]).rstrip("\n")
            url = result["url"]
            other_results.append({"title": title, "url": url})

        return {"main": first_dict, "others": other_results}


@router.get("/search")
async def search(
    request: Request, query: str, count: int = 5
) -> dict[str, list[str] | dict[str, str]] | dict[str, str]:
    """Search for your queires on the web."""
    http_client = request.app.state.http_client
    search = Search()

    data = await search.basic_search(http_client, query, category="web", count=count)

    return data


@router.get("/overflow")
async def overflow(
    request: Request, query: str, questions: int = 6
) -> dict[str, list[dict[str, str | int]]]:
    http_client = request.app.state.http_client
    base_url = (
        "https://api.stackexchange.com/2.2/search/advanced?order=desc&"
        "sort=activity&site=stackoverflow&q={query}"
    )

    async with http_client().get(base_url.format(query=quote_plus(query))) as resp:
        data = await resp.json()

    top = data["items"][:questions]
    results = []

    for item in top:
        results.append(
            {
                "name": unescape(item["title"]),
                "score": item["score"],
                "answers": item["answer_count"],
                "tags": item["tags"],
                "link": item["link"],
            }
        )

    return {
        "results": results,
    }
