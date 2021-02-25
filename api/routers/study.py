import io
import typing as t
import urllib

from bs4 import BeautifulSoup
from fastapi import APIRouter, Request
from starlette.responses import StreamingResponse

from api import config, http_client
from api.core import log_error
from api.utils import get_pod_pages

router = APIRouter(
    prefix="/study",
    tags=["Study based commands"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/urban")
@log_error()
async def urban(_: Request, word: str) -> dict:
    """Lookup urban dictionary for a term."""
    url = "http://api.urbandictionary.com/v0/define"
    async with http_client.session.get(url, params={"term": word}) as resp:
        json = await resp.json()
        data = json.get("list", [])

    return {"data": data}


@router.get("/calc")
@log_error()
async def calc(_: Request, equation: str) -> dict:
    """Get computers to solve your maths equation/"""
    params = {"expr": equation}
    url = "http://api.mathjs.org/v4/"

    async with http_client.session.get(url, params=params) as resp:
        response = await resp.text()
        if resp.status not in config.RESPONSES:
            return {
                "error": (
                    "❌ Invalid Equation Specified, " "Please Recheck the Equation"
                ),
            }

        return {"answer": response}


@router.get("/word-definition")
@log_error()
async def word_def(_: Request, word: str) -> dict:
    url = "https://www.vocabulary.com/dictionary/" + word + ""
    htmlfile = urllib.request.urlopen(url)
    soup = BeautifulSoup(htmlfile, "lxml")

    soup1 = soup.find(class_="short")

    try:
        short_meaning = soup1.get_text()
    except AttributeError:
        return {"error": "No such word!"}

    soup2 = soup.find(class_="long")
    long_meaning = soup2.get_text()

    soup3 = soup.find(class_="instances")
    txt = soup3.get_text()
    instances = txt.rstrip()

    return {
        "short": short_meaning,
        "long": long_meaning,
        "instances": " ".join(instances.split()),
    }


@router.get("/wiki")
@log_error()
async def wiki(_: Request, query: str) -> dict:
    """Search wikipedia for your knowledge hunt."""
    payload = {
        "action": "query",
        "titles": query.replace(" ", "_"),
        "format": "json",
        "formatversion": "2",
        "prop": "extracts",
        "exintro": "1",
        "redirects": "1",
        "explaintext": "1",
    }

    async with http_client.tcp_session.get(
        "https://en.wikipedia.org/w/api.php",
        params=payload,
        headers={"user-agent": config.USER_AGENT},
    ) as res:
        result = await res.json()

    try:
        return {
            "query": query,
            "results": [
                {
                    "title": page["title"],
                    "description": page["extract"]
                    .strip()
                    .replace(
                        "\n",
                        "\n\n",
                    ),
                    "url": "https://en.wikipedia.org/wiki/{}".format(
                        page["title"].replace(" ", "_")
                    ),
                }
                for page in result["query"]["pages"]
            ],
        }
    except KeyError:
        return {"error": "No results for your query!"}


@router.get("/wolfram")
@log_error()
async def wolfram(_: Request, appid: str, query: str) -> StreamingResponse:
    """Lookup wolfram alpha for your queries."""
    url_str = urllib.parse.urlencode(
        {
            "i": query,
            "appid": appid,
            "location": "the moon",
            "latlong": "0.0,0.0",
            "ip": "1.1.1.1",
        }
    )
    query = config.QUERY.format(request="simple", data=url_str)

    async with http_client.session.get(query) as response:
        image_bytes = await response.read()

    return StreamingResponse(io.BytesIO(image_bytes), media_type="image/png")


@router.get("/wolfram-page")
@log_error()
async def wolfram_page(_: Request, appid: str, query: str) -> dict:
    """Get a wolfram page containing images."""
    pages = await get_pod_pages(appid, query)

    if not pages:
        return {"error": "No results found!"}

    return {"pages": pages}


@router.get("/latex")
@log_error()
async def latex(_: Request, equation: str) -> t.Union[dict, StreamingResponse]:
    """Get a latex rendered image."""
    LATEX_URL = "https://latex.codecogs.com/gif.download?%5Cbg_white%20%5Clarge%20"

    raw_eq = r"{}".format(equation)
    url_eq = urllib.parse.quote(raw_eq)

    async with http_client.session.get(LATEX_URL + url_eq) as result:
        img = await result.read()

    if not 200 <= result.status < 300:
        return {"error": f"{equation} is not a valid expression or equation"}

    return StreamingResponse(io.BytesIO(img), media_type="image/png")
