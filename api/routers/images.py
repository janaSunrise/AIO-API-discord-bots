import typing as t

from fastapi import APIRouter, Request

from api import config as conf
from api.core import log_error

router = APIRouter(
    prefix="/images",
    tags=["Image editing endpoint"],
    responses={404: {"description": "Not found"},},
)


@log_error()
async def fetch_nekobot_api(http_client, params: dict) -> t.Any:
    async with http_client.session.get(conf.NEKOBOT_API_ROOT, params=params,) as resp:
        json = await resp.json()

    return json["message"]


# -- Router paths --
@router.get("/clyde")
@log_error()
async def clyde(request: Request, text: str) -> dict:
    http_client = request.app.state.http_client

    return {
        "image": await fetch_nekobot_api(http_client, {"type": "clyde", "text": text})
    }


@router.get("/captcha")
@log_error()
async def captcha(request: Request, username: str, image_url: str) -> dict:
    http_client = request.app.state.http_client

    return {
        "image": await fetch_nekobot_api(
            http_client, {"type": "captcha", "url": image_url, "username": username}
        )
    }


@router.get("/changemymind")
@log_error()
async def cmm(request: Request, text: str) -> dict:
    http_client = request.app.state.http_client
    return {
        "image": await fetch_nekobot_api(
            http_client, {"type": "changemymind", "text": text}
        )
    }


@router.get("/iphonex")
@log_error()
async def iphonex(request: Request, image_url: str) -> dict:
    http_client = request.app.state.http_client
    return {
        "image": await fetch_nekobot_api(
            http_client, {"type": "iphonex", "url": image_url}
        )
    }


@router.get("/kms")
@log_error()
async def kms(request: Request, image_url: str) -> dict:
    http_client = request.app.state.http_client
    return {
        "image": await fetch_nekobot_api(http_client, {"type": "kms", "url": image_url})
    }


@router.get("/trap")
@log_error()
async def trap(request: Request, name: str, author: str, image_url: str) -> dict:
    http_client = request.app.state.http_client
    return {
        "image": await fetch_nekobot_api(
            http_client,
            {"type": "trap", "name": name, "author": author, "image": image_url},
        )
    }


@router.get("/nichijou")
@log_error()
async def nichijou(request: Request, text: str) -> dict:
    http_client = request.app.state.http_client
    return {
        "image": await fetch_nekobot_api(
            http_client, {"type": "nichijou", "text": text}
        )
    }


@router.get("/trumptweet")
@log_error()
async def trumptweet(request: Request, text: str) -> dict:
    http_client = request.app.state.http_client
    return {
        "image": await fetch_nekobot_api(
            http_client, {"type": "trumptweet", "text": text}
        )
    }


@router.get("/tweet")
@log_error()
async def tweet(request: Request, username: str, text: str) -> dict:
    http_client = request.app.state.http_client
    return {
        "image": await fetch_nekobot_api(
            http_client, {"type": "tweet", "username": username, "text": text}
        )
    }


@router.get("/magik")
@log_error()
async def magik(request: Request, image_url: str, intensity: int = 5) -> dict:
    http_client = request.app.state.http_client
    return {
        "image": await fetch_nekobot_api(
            http_client, {"type": "magik", "image": image_url, "intensity": intensity}
        )
    }


@router.get("/stickbug")
@log_error()
async def stickbug(request: Request, image_url: str) -> dict:
    http_client = request.app.state.http_client
    return {
        "image": await fetch_nekobot_api(
            http_client, {"type": "stickbug", "url": image_url,},
        )
    }


@router.get("/gay")
@log_error()
async def gay(_: Request, avatar: str) -> dict:
    return {"url": f"https://some-random-api.ml/canvas/gay?avatar={avatar}"}


@router.get("/glass")
@log_error()
async def glass(_: Request, avatar: str) -> dict:
    return {"url": f"https://some-random-api.ml/canvas/glass?avatar={avatar}"}


@router.get("/wasted")
@log_error()
async def wasted(_: Request, avatar: str) -> dict:
    return {"url": f"https://some-random-api.ml/canvas/wasted?avatar={avatar}"}


@router.get("/triggered")
@log_error()
async def triggered(_: Request, avatar: str) -> dict:
    return {"url": f"https://some-random-api.ml/canvas/triggered?avatar={avatar}"}


@router.get("/youtube")
@log_error()
async def youtube(_: Request, picture: str, name: str, comment: str) -> dict:
    return {
        "url": (
            "https://some-random-api.ml/canvas/youtube-comment"
            f"?avatar={picture}&username={name}&comment={comment}"
        ),
    }


@router.get("/greyscale")
@log_error()
async def greyscale(_: Request, avatar: str) -> dict:
    return {
        "url": f"https://some-random-api.ml/canvas/greyscale?avatar={avatar}",
    }


@router.get("/threshold")
@log_error()
async def threshold(_: Request, avatar: str) -> dict:
    return {
        "url": f"https://some-random-api.ml/canvas/threshold?avatar={avatar}",
    }


@router.get("/color-viewer")
@log_error()
async def colorviewer(_: Request, color: str) -> dict:
    return {
        "url": (
            f"https://some-random-api.ml/canvas/colorviewer?color={color.strip('#')}"
        ),
    }
