from fastapi import APIRouter

from api.app import http_client

router = APIRouter(
    prefix="/fun",
    tags=["fun"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/joke")
async def joke(explicit: bool = False):
    if explicit:
        url = "http://api.icndb.com/jokes/random"
    else:
        url = "http://api.icndb.com/jokes/random?exclude=[explicit]"

    async with http_client.session.get(url) as resp:
        json = await resp.json()

    return {
        "joke": json["value"]["joke"].replace("&quote", '"')
    }


@router.get("/chucknorris")
async def chucknorris():
    async with http_client.session.get("https://api.chucknorris.io/jokes/random") as resp:
        json = await resp.json()

    return {
        "joke": json["value"]
    }


@router.get("/why")
async def why():
    async with http_client.session.get("https://nekos.life/api/why") as resp:
        json = await resp.json()

    return {
        "why": json["why"]
    }


@router.get("/yesno")
async def yesno(question: str):
    async def get_answer(self, ans: str) -> str:
        return_str = ""
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
        "answer": get_answer(json["answer"])
    }
