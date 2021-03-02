import random

from fastapi import APIRouter, Request

from api import http_client
from api.core import log_error

router = APIRouter(
    prefix="/fun",
    tags=["Fun endpoints"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/joke")
@log_error()
async def joke(_: Request, explicit: bool = False) -> dict:
    """Get a random joke."""
    if explicit:
        url = "http://api.icndb.com/jokes/random"
    else:
        url = "http://api.icndb.com/jokes/random?exclude=[explicit]"

    async with http_client.session.get(url) as resp:
        json = await resp.json()

    return {"joke": json["value"]["joke"].replace("&quote", '"')}


@router.get("/dadjoke")
@log_error()
async def dad_joke(_: Request) -> dict:
    """Get a random dad joke."""
    async with http_client.session.get("https://icanhazdadjoke.com") as resp:
        res = await resp.text()
        res = res.encode("utf-8").decode("utf-8")

    return {"joke": res}


@router.get("/excuse")
@log_error()
async def excuse(_: Request) -> dict:
    """Generate an excuse for any occasion."""
    async with http_client.session.get(
        "http://pages.cs.wisc.edu/~ballard/bofh/excuses"
    ) as resp:
        data = await resp.text()
        lines = data.split("\n")

    return {"excuse": random.choice(lines)}


@router.get("/chucknorris")
@log_error()
async def chuck_norris(_: Request) -> dict:
    """Have a funny chuck norris style joke."""
    async with http_client.session.get(
        "https://api.chucknorris.io/jokes/random"
    ) as resp:
        json = await resp.json()

    return {"joke": json["value"]}


@router.get("/why")
@log_error()
async def why(_: Request) -> dict:
    """Get to know a random why question."""
    async with http_client.session.get("https://nekos.life/api/why") as resp:
        json = await resp.json()

    return {"why": json["why"]}


@router.get("/yesno")
@log_error()
async def yesno(_: Request, question: str) -> dict:
    """Get a random answer for a yes no question."""

    async def get_answer(ans: str) -> str:
        if ans == "yes":
            return_str = "Yes."
        elif ans == "no":
            return_str = "NOPE"
        elif ans == "maybe":
            return_str = "maaaaaaybe?"
        else:
            return_str = "Internal Error: Invalid answer LMAOO"

        return return_str

    async with http_client.session.get("https://yesno.wtf/api") as resp:
        json = await resp.json()

    return {
        "question": question,
        "answer": get_answer(json["answer"]),
    }


@router.get("/history")
@log_error()
async def history(_: Request) -> dict:
    """Get to know about an interesting history date."""
    async with http_client.session.get(
        "http://numbersapi.com/random/date?json"
    ) as resp:
        json = await resp.json()

    return {
        "fact": json["text"],
        "year": json["year"],
    }


@router.get("/mathfact")
@log_error()
async def mathfact(_: Request) -> dict:
    """Get to know an interesting math fact."""
    async with http_client.session.get(
        "http://numbersapi.com/random/math?json"
    ) as resp:
        json = await resp.json()

    return {
        "fact": json["text"],
        "number": json["number"],
    }


@router.get("/yearfact")
@log_error()
async def yearfact(_: Request) -> dict:
    """Get to know an interesting year fact."""
    async with http_client.session.get(
        "http://numbersapi.com/random/year?json"
    ) as resp:
        json = await resp.json()

    return {
        "fact": json["text"],
        "year": json["number"],
    }


@router.get("/idea")
@log_error()
async def idea(_: Request) -> dict:
    """Get an interesting idea."""
    async with http_client.session.get(
        "http://itsthisforthat.com/api.php", params="json"
    ) as resp:
        json = await resp.json(content_type="text/javascript")

    return {"idea": f"{json['this']} for {json['that']}"}


@router.get("/insult")
@log_error()
async def insult(_: Request) -> dict:
    """Get an random insult."""
    async with http_client.session.get(
        "http://quandyfactory.com/insult/json"
    ) as resp:
        json = await resp.json()

    return {"insult": json["insult"]}


@router.get("/advice")
@log_error()
async def advice(_: Request) -> dict:
    """Get an useful advice."""
    async with http_client.session.get("https://api.adviceslip.com/advice") as resp:
        json = await resp.json(content_type="text/html")

    return {"advice": json["slip"]["advice"]}


@router.get("/advice")
@log_error()
async def inspire(_: Request) -> dict:
    """Get inspired."""
    async with http_client.session.get("https://affirmations.dev/") as response:
        res = await response.json()

    return {"advice": res["affirmation"]}
