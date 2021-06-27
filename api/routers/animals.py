from fastapi import APIRouter, Request

from api.core import log_error

router = APIRouter(
    prefix="/animals",
    tags=["Images of animals"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/cat")
@log_error()
async def cat(request: Request) -> dict:
    """Get a random cat image."""
    http_client = request.app.state.http_client

    async with http_client.session.get("https://some-random-api.ml/img/cat") as resp:
        json = await resp.json()

    return {"url": json["link"]}


@router.get("/cat-fact")
@log_error()
async def cat_fact(request: Request) -> dict:
    """Get a random cat fact."""
    http_client = request.app.state.http_client

    async with http_client.session.get("https://some-random-api.ml/facts/cat") as resp:
        json = await resp.json()

    return {"fact": json["fact"]}


@router.get("/dog")
@log_error()
async def dog(request: Request) -> dict:
    http_client = request.app.state.http_client

    async with http_client.session.get(
        "https://dog.ceo/api/breeds/image/random"
    ) as resp:
        json = await resp.json()

    return {"url": json["message"]}


@router.get("/dog-fact")
@log_error()
async def dog_fact(request: Request) -> dict:
    """Get a random dog image."""
    http_client = request.app.state.http_client

    async with http_client.session.get("https://some-random-api.ml/facts/dog") as resp:
        json = await resp.json()

    return {"fact": json["fact"]}


@router.get("/panda-fact")
@log_error()
async def panda_fact(request: Request) -> dict:
    """Get a random interesting fact about pandas."""
    http_client = request.app.state.http_client

    async with http_client.session.get(
        "https://some-random-api.ml/facts/panda"
    ) as resp:
        json = await resp.json()

    return {"fact": json["fact"]}


@router.get("/fox")
@log_error()
async def fox(request: Request) -> dict:
    """Get a random fox image."""
    http_client = request.app.state.http_client

    async with http_client.session.get("https://randomfox.ca/floof/") as resp:
        json = await resp.json()

    return {"url": json["image"]}


@router.get("/panda")
@log_error()
async def panda(request: Request) -> dict:
    """Get a random panda image."""
    http_client = request.app.state.http_client

    async with http_client.session.get("https://some-random-api.ml/img/panda") as resp:
        json = await resp.json()

    return {"url": json["link"]}


@router.get("/koala")
@log_error()
async def koala(request: Request) -> dict:
    """Get a random koala image."""
    http_client = request.app.state.http_client

    async with http_client.session.get("https://some-random-api.ml/img/koala") as resp:
        json = await resp.json()

    return {"url": json["link"]}


@router.get("/birb")
@log_error()
async def birb(request: Request) -> dict:
    """Get a random bird image."""
    http_client = request.app.state.http_client

    async with http_client.session.get("https://some-random-api.ml/img/birb") as resp:
        json = await resp.json()

    return {"url": json["link"]}


@router.get("/duck")
@log_error()
async def duck(request: Request) -> dict:
    """Get a random duck image."""
    http_client = request.app.state.http_client

    async with http_client.session.get("https://random-d.uk/api/v2/random") as resp:
        json = await resp.json()

    return {"url": json["url"]}
