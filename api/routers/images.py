from fastapi import APIRouter

router = APIRouter(
    prefix="/images",
    tags=["images"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/gay")
async def gay(avatar: str):
    return {
        "url": f"https://some-random-api.ml/canvas/gay?avatar={avatar}"
    }


@router.get("/glass")
async def glass(avatar: str):
    return {
        "url": f"https://some-random-api.ml/canvas/glass?avatar={avatar}"
    }


@router.get("/wasted")
async def wasted(avatar: str):
    return {
        "url": f"https://some-random-api.ml/canvas/wasted?avatar={avatar}"
    }


@router.get("/triggered")
async def triggered(avatar: str):
    return {
        "url": f"https://some-random-api.ml/canvas/triggered?avatar={avatar}"
    }


@router.get("/greyscale")
async def greyscale(avatar: str):
    return {
        "url": f"https://some-random-api.ml/canvas/greyscale?avatar={avatar}"
    }


@router.get("/threshold")
async def threshold(avatar: str):
    return {
        "url": f"https://some-random-api.ml/canvas/threshold?avatar={avatar}"
    }


@router.get("/color-viewer")
async def colorviewer(color: str):
    return {
        "url": f"https://some-random-api.ml/canvas/colorviewer?color={color.strip('#')}"
    }
