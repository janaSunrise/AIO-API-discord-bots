import io
import typing as t
import urllib

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
async def urban(request: Request, word: str) -> dict:
    """Lookup urban dictionary for a term."""
    url = "http://api.urbandictionary.com/v0/define"
    async with http_client.session.get(url, params={"term": word}) as resp:
        json = await resp.json()
        data = json.get("list", [])

    return {"data": data}


@router.get("/calc")
@log_error()
async def calc(request: Request, equation: str) -> dict:
    """Get computers to solve your maths equation/"""
    params = {"expr": equation}
    url = "http://api.mathjs.org/v4/"

    async with http_client.session.get(url, params=params) as resp:
        r = await resp.text()
        try:
            response = config.RESPONSES[resp.status]
        except KeyError:
            return {"error": "❌ Invalid Equation Specified, Please Recheck the Equation"}

        return {"answer": r}


@router.get("/wiki")
@log_error()
async def wiki(request: Request, query: str) -> dict:
    """Search wikipedia for your knowledge hunt."""
    payload = {
        "action": "query",
        "titles": query.replace(" ", "_"),
        "format": "json",
        "formatversion": "2",
        "prop": "extracts",
        "exintro": "1",
        "redirects": "1",
        "explaintext": "1"
    }

    async with http_client.tcp_session.get(
            "https://en.wikipedia.org/w/api.php", params=payload, headers={"user-agent": config.USER_AGENT}
    ) as res:
        result = await res.json()

    try:
        for page in result["query"]["pages"]:
            title = page["title"]
            description = page["extract"].strip().replace("\n", "\n\n")
            url = "https://en.wikipedia.org/wiki/{}".format(title.replace(" ", "_"))

            return {
                "title": title,
                "description": description,
                "url": url
            }
    except KeyError:
        return {"error": "No results for your query!"}


@router.get("/wolfram")
@log_error()
async def wolfram(request: Request, appid: str, query: str) -> StreamingResponse:
    """Lookup wolfram alpha for your queries."""
    url_str = urllib.parse.urlencode({
        "i": query,
        "appid": appid,
        "location": "the moon",
        "latlong": "0.0,0.0",
        "ip": "1.1.1.1"
    })
    query = config.QUERY.format(request="simple", data=url_str)

    async with http_client.session.get(query) as response:
        image_bytes = await response.read()

    return StreamingResponse(io.BytesIO(image_bytes), media_type="image/png")


@router.get("/wolfram-page")
@log_error()
async def wolfram_page(request: Request, appid: str, query: str) -> dict:
    """Get a wolfram page containing images."""
    pages = await get_pod_pages(appid, query)

    if not pages:
        return {"error": "No results found!"}

    return {"pages": pages}


@router.get("/latex")
@log_error()
async def latex(request: Request, equation: str) -> t.Union[dict, StreamingResponse]:
    """Get a latex rendered image."""
    LATEX_URL = "https://latex.codecogs.com/gif.download?%5Cbg_white%20%5Clarge%20"

    raw_eq = r"{}".format(equation)
    url_eq = urllib.parse.quote(raw_eq)

    async with http_client.session.get(LATEX_URL + url_eq) as result:
        img = await result.read()

    if not 200 <= result.status < 300:
        return {"error": f"{equation} is not a valid expression or equation"}

    return StreamingResponse(io.BytesIO(img), media_type="image/png")
