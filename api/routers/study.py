import io
import urllib

from fastapi import APIRouter
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
async def urban(word: str):
    url = "http://api.urbandictionary.com/v0/define"
    async with http_client.session.get(url, params={"term": word}) as resp:
        json = await resp.json()
        data = json.get("list", [])

    return {
        "data": data
    }


@router.get("/calc")
@log_error()
async def calc(equation: str):
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
async def wiki(query: str):
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
            "https://en.wikipedia.org/w/api.ph",
            params=payload,
            headers={"user-agent": config.USER_AGENT}
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
        return {
            "error": "No results for your query!"
        }


@router.get("/wolfram")
@log_error()
async def wolfram(appid: str, query: str):
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
async def wolfram_page(appid: str, query: str):
    pages = await get_pod_pages(appid, query)

    if not pages:
        return {
            "error": "No results found!"
        }

    return {
        "pages": pages
    }
