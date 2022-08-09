from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/animals",
    tags=["Images of animals"],
    responses={
        404: {"description": "Not found"},
    },
)


@router.get("/cat")
async def cat(request: Request) -> dict:
    """Get a random cat image."""
    http_client = request.app.state.http_client

    async with http_client().get("https://some-random-api.ml/img/cat") as resp:
        json = await resp.json()

    return {"url": json["link"]}


@router.get("/cat-fact")
async def cat_fact(request: Request) -> dict:
    """Get a random cat fact."""
    http_client = request.app.state.http_client

    async with http_client().get("https://some-random-api.ml/facts/cat") as resp:
        json = await resp.json()

    return {"fact": json["fact"]}


@router.get("/dog")
async def dog(request: Request) -> dict:
    http_client = request.app.state.http_client

    async with http_client().get("https://dog.ceo/api/breeds/image/random") as resp:
        json = await resp.json()

    return {"url": json["message"]}


@router.get("/dog-fact")
async def dog_fact(request: Request) -> dict:
    """Get a random dog image."""
    http_client = request.app.state.http_client

    async with http_client().get("https://some-random-api.ml/facts/dog") as resp:
        json = await resp.json()

    return {"fact": json["fact"]}


@router.get("/panda-fact")
async def panda_fact(request: Request) -> dict:
    """Get a random interesting fact about pandas."""
    http_client = request.app.state.http_client

    async with http_client().get("https://some-random-api.ml/facts/panda") as resp:
        json = await resp.json()

    return {"fact": json["fact"]}


@router.get("/fox")
async def fox(request: Request) -> dict:
    """Get a random fox image."""
    http_client = request.app.state.http_client

    async with http_client().get("https://randomfox.ca/floof/") as resp:
        json = await resp.json()

    return {"url": json["image"]}


@router.get("/panda")
async def panda(request: Request) -> dict:
    """Get a random panda image."""
    http_client = request.app.state.http_client

    async with http_client().get("https://some-random-api.ml/img/panda") as resp:
        json = await resp.json()

    return {"url": json["link"]}


@router.get("/koala")
async def koala(request: Request) -> dict:
    """Get a random koala image."""
    http_client = request.app.state.http_client

    async with http_client().get("https://some-random-api.ml/img/koala") as resp:
        json = await resp.json()

    return {"url": json["link"]}


@router.get("/birb")
async def birb(request: Request) -> dict:
    """Get a random bird image."""
    http_client = request.app.state.http_client

    async with http_client().get("https://some-random-api.ml/img/birb") as resp:
        json = await resp.json()

    return {"url": json["link"]}


@router.get("/duck")
async def duck(request: Request) -> dict:
    """Get a random duck image."""
    http_client = request.app.state.http_client

    async with http_client().get("https://random-d.uk/api/v2/random") as resp:
        json = await resp.json()

    return {"url": json["url"]}
