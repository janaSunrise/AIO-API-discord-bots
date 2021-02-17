from fastapi import APIRouter

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
async def gay(avatar: str) -> dict:
    return {"url": f"https://some-random-api.ml/canvas/gay?avatar={avatar}"}


@router.get("/glass")
@log_error()
async def glass(avatar: str) -> dict:
    return {"url": f"https://some-random-api.ml/canvas/glass?avatar={avatar}"}


@router.get("/wasted")
@log_error()
async def wasted(avatar: str) -> dict:
    return {"url": f"https://some-random-api.ml/canvas/wasted?avatar={avatar}"}


@router.get("/triggered")
@log_error()
async def triggered(avatar: str) -> dict:
    return {"url": f"https://some-random-api.ml/canvas/triggered?avatar={avatar}"}


@router.get("/youtube")
@log_error()
async def youtube(picture: str, name: str, comment: str) -> dict:
    return {
        "url": f"https://some-random-api.ml/canvas/youtube-comment?avatar={picture}&username={name}&comment={comment}"
    }


@router.get("/greyscale")
@log_error()
async def greyscale(avatar: str) -> dict:
    return {"url": f"https://some-random-api.ml/canvas/greyscale?avatar={avatar}"}


@router.get("/threshold")
@log_error()
async def threshold(avatar: str) -> dict:
    return {"url": f"https://some-random-api.ml/canvas/threshold?avatar={avatar}"}


@router.get("/color-viewer")
@log_error()
async def colorviewer(color: str) -> dict:
    return {"url": f"https://some-random-api.ml/canvas/colorviewer?color={color.strip('#')}"}
