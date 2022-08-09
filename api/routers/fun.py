import random

from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/fun",
    tags=["Fun endpoints"],
    responses={
        404: {"description": "Not found"},
    },
)


@router.get("/joke")
async def joke(request: Request, explicit: bool = False) -> dict:
    """Get a random joke."""
    http_client = request.app.state.http_client

    if explicit:
        url = "http://api.icndb.com/jokes/random"
    else:
        url = "http://api.icndb.com/jokes/random?exclude=[explicit]"

    async with http_client().get(url) as resp:
        json = await resp.json()

    return {"joke": json["value"]["joke"].replace("&quote", '"')}


@router.get("/dadjoke")
async def dad_joke(request: Request) -> dict:
    """Get a random dad joke."""
    http_client = request.app.state.http_client

    async with http_client().get("https://icanhazdadjoke.com") as resp:
        res = await resp.text()
        res = res.encode("utf-8").decode("utf-8")

    return {"joke": res}


@router.get("/excuse")
async def excuse(request: Request) -> dict:
    """Generate an excuse for any occasion."""
    http_client = request.app.state.http_client

    async with http_client().get(
        "http://pages.cs.wisc.edu/~ballard/bofh/excuses"
    ) as resp:
        data = await resp.text()
        lines = data.split("\n")

    return {"excuse": random.choice(lines)}


@router.get("/chucknorris")
async def chuck_norris(request: Request) -> dict:
    """Have a funny chuck norris style joke."""
    http_client = request.app.state.http_client

    async with http_client().get("https://api.chucknorris.io/jokes/random") as resp:
        json = await resp.json()

    return {"joke": json["value"]}


@router.get("/why")
async def why(request: Request) -> dict:
    """Get to know a random why question."""
    http_client = request.app.state.http_client

    async with http_client().get("https://nekos.life/api/why") as resp:
        json = await resp.json()

    return {"why": json["why"]}


@router.get("/yesno")
async def yesno(request: Request, question: str) -> dict:
    """Get a random answer for a yes no question."""
    http_client = request.app.state.http_client

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

    async with http_client().get("https://yesno.wtf/api") as resp:
        json = await resp.json()

    return {
        "question": question,
        "answer": get_answer(json["answer"]),
    }


@router.get("/history")
async def history(request: Request) -> dict:
    """Get to know about an interesting history date."""
    http_client = request.app.state.http_client

    async with http_client().get("http://numbersapi.com/random/date?json") as resp:
        json = await resp.json()

    return {
        "fact": json["text"],
        "year": json["year"],
    }


@router.get("/math-fact")
async def mathfact(request: Request) -> dict:
    """Get to know an interesting math fact."""
    http_client = request.app.state.http_client

    async with http_client().get("http://numbersapi.com/random/math?json") as resp:
        json = await resp.json()

    return {
        "fact": json["text"],
        "number": json["number"],
    }


@router.get("/year-fact")
async def yearfact(request: Request) -> dict:
    """Get to know an interesting year fact."""
    http_client = request.app.state.http_client

    async with http_client().get("http://numbersapi.com/random/year?json") as resp:
        json = await resp.json()

    return {
        "fact": json["text"],
        "year": json["number"],
    }


@router.get("/idea")
async def idea(request: Request) -> dict:
    """Get an interesting idea."""
    http_client = request.app.state.http_client

    async with http_client().get(
        "http://itsthisforthat.com/api.php", params="json"
    ) as resp:
        json = await resp.json(content_type="text/javascript")

    return {"idea": f"{json['this']} for {json['that']}"}


@router.get("/insult")
async def insult(request: Request) -> dict:
    """Get an random insult."""
    http_client = request.app.state.http_client

    async with http_client().get("http://quandyfactory.com/insult/json") as resp:
        json = await resp.json()

    return {"insult": json["insult"]}


@router.get("/advice")
async def advice(request: Request) -> dict:
    """Get an useful advice."""
    http_client = request.app.state.http_client

    async with http_client().get("https://api.adviceslip.com/advice") as resp:
        json = await resp.json(content_type="text/html")

    return {"advice": json["slip"]["advice"]}


@router.get("/inspire")
async def inspire(request: Request) -> dict:
    """Get inspired."""
    http_client = request.app.state.http_client

    async with http_client().get("https://affirmations.dev/") as response:
        res = await response.json()

    return {"advice": res["affirmation"]}
