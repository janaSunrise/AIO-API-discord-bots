from fastapi import APIRouter, Request

from api.core import log_error

router = APIRouter(
    prefix="/images",
    tags=["Image editing endpoint"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
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
