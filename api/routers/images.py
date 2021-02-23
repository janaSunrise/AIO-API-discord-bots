import typing as t
from fastapi import APIRouter, Request

from api import http_client, config as conf
from api.core import log_error

router = APIRouter(
    prefix="/images",
    tags=["Image editing endpoint"],
    responses={
        404: {"description": "Not found"},
    },
)


@log_error()
async def fetch_nekobot_api(params: dict) -> t.Any:
    async with http_client.session.get(conf.NEKOBOT_API_ROOT, params=params) as resp:
        json = await resp.json()

    return json["message"]


# -- Router paths --
@router.get("/clyde")
@log_error()
async def clyde(request: Request, text: str) -> dict:
    return {"image": await fetch_nekobot_api({
        "type": "clyde",
        "text": text
    })}


@router.get("/captcha")
@log_error()
async def captcha(request: Request, username: str, image_url: str) -> dict:
    return {"image": await fetch_nekobot_api({
        "type": "captcha",
        "url": image_url,
        "username": username
    })}


@router.get("/changemymind")
@log_error()
async def cmm(request: Request, text: str) -> dict:
    return {"image": await fetch_nekobot_api({
        "type": "changemymind",
        "text": text
    })}


@router.get("/iphonex")
@log_error()
async def iphonex(request: Request, image_url: str) -> dict:
    return {"image": await fetch_nekobot_api({
        "type": "iphonex",
        "url": image_url
    })}


@router.get("/kms")
@log_error()
async def kms(request: Request, image_url: str) -> dict:
    return {"image": await fetch_nekobot_api({
        "type": "kms",
        "url": image_url
    })}


@router.get("/trap")
@log_error()
async def trap(request: Request, name: str, author: str, image_url: str) -> dict:
    return {"image": await fetch_nekobot_api({
        "type": "trap",
        "name": name,
        "author": author,
        "image": image_url
    })}


@router.get("/nichijou")
@log_error()
async def nichijou(request: Request, text: str) -> dict:
    return {"image": await fetch_nekobot_api({
        "type": "nichijou",
        "text": text
    })}


@router.get("/trumptweet")
@log_error()
async def trumptweet(request: Request, text: str) -> dict:
    return {"image": await fetch_nekobot_api({
        "type": "trumptweet",
        "text": text
    })}


@router.get("/tweet")
@log_error()
async def tweet(request: Request, username: str, text: str) -> dict:
    return {"image": await fetch_nekobot_api({
        "type": "tweet",
        "username": username,
        "text": text
    })}


@router.get("/magik")
@log_error()
async def magik(request: Request, image_url: str, intensity: int = 5) -> dict:
    return {"image": await fetch_nekobot_api({
        "type": "magik",
        "image": image_url,
        "intensity": intensity
    })}


@router.get("/stickbug")
@log_error()
async def stickbug(request: Request, image_url: str) -> dict:
    return {"image": await fetch_nekobot_api({
        "type": "stickbug",
        "url": image_url,
    })}


@router.get("/gay")
@log_error()
async def gay(request: Request, avatar: str) -> dict:
    return {"url": f"https://some-random-api.ml/canvas/gay?avatar={avatar}"}


@router.get("/glass")
@log_error()
async def glass(request: Request, avatar: str) -> dict:
    return {"url": f"https://some-random-api.ml/canvas/glass?avatar={avatar}"}


@router.get("/wasted")
@log_error()
async def wasted(avatar: str) -> dict:
    return {"url": f"https://some-random-api.ml/canvas/wasted?avatar={avatar}"}


@router.get("/triggered")
@log_error()
async def triggered(request: Request, avatar: str) -> dict:
    return {"url": f"https://some-random-api.ml/canvas/triggered?avatar={avatar}"}


@router.get("/youtube")
@log_error()
async def youtube(request: Request, picture: str, name: str, comment: str) -> dict:
    return {
        "url": f"https://some-random-api.ml/canvas/youtube-comment?avatar={picture}&username={name}&comment={comment}"
    }


@router.get("/greyscale")
@log_error()
async def greyscale(request: Request, avatar: str) -> dict:
    return {"url": f"https://some-random-api.ml/canvas/greyscale?avatar={avatar}"}


@router.get("/threshold")
@log_error()
async def threshold(request: Request, avatar: str) -> dict:
    return {"url": f"https://some-random-api.ml/canvas/threshold?avatar={avatar}"}


@router.get("/color-viewer")
@log_error()
async def colorviewer(request: Request, color: str) -> dict:
    return {"url": f"https://some-random-api.ml/canvas/colorviewer?color={color.strip('#')}"}
