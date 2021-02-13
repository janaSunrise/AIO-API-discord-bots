from fastapi import APIRouter

from api import config
from api.app import http_client

router = APIRouter(
    prefix="/study",
    tags=["study"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/urban")
async def urban(word: str):
    url = "http://api.urbandictionary.com/v0/define"
    async with http_client.session.get(url, params={"term": word}) as resp:
        json = await resp.json()
        data = json.get("list", [])

    return {
        "data": data
    }


@router.get("/calc")
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

