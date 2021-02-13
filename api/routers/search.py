import re

import html2text
from fastapi import APIRouter

from api import config
from api.app import http_client


router = APIRouter(
    prefix="/search",
    tags=["search"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
class Search:
    def __init__(self) -> None:
        self.tomd = html2text.HTML2Text()
        self.tomd.ignore_links = True
        self.tomd.ignore_images = True
        self.tomd.ignore_tables = True
        self.tomd.ignore_emphasis = True
        self.tomd.body_width = 0

    @staticmethod
    async def _search_logic(query: str, category: str = "web", count: int = 5) -> list:
        """Use scrapestack and the Qwant API to find search results."""
        base = "https://api.qwant.com/api"

        search_url = f"{base}/search/{category}" \
                     f"?count={count}" \
                     f"&q={query.replace(' ', '+')}" \
                     f"&t=web&locale=en_US&uiv=4"

        # Searching
        headers = {"User-Agent": config.USER_AGENT}
        async with http_client.session.get(search_url, headers=headers) as resp:
            to_parse = await resp.json()

        return to_parse["data"]["result"]["items"]

    async def basic_search(self, query: str, category: str, count: int):
        """Basic search formatting."""
        results = await self._search_logic(query, category, count=count)

        count = len(results)

        # Return if no results
        if not count:
            return {"error": f"No results found for `{query}`."}

        # Gets the first entry's data
        first_title = self.tomd.handle(results[0]["title"]).rstrip("\n").strip("<>")
        first_url = results[0]["url"]
        first_desc = self.tomd.handle(results[0]["desc"]).rstrip("\n")

        first_dict = {
            "title": first_title,
            "description": first_desc,
            "url": first_url
        }

        # Builds the substring for each of the other result.
        other_results = []

        for result in results[1: count]:
            title = self.tomd.handle(result["title"]).rstrip("\n")
            url = result["url"]
            other_results.append({
                "title": title,
                "url": url
            })

        return {
            "main": first_dict,
            "others": other_results
        }


@router.get("/")
async def search(query: str, count: int = 5):
    search_obj = Search()
    data = await search_obj.basic_search(query, category="web", count=count)

    return data
