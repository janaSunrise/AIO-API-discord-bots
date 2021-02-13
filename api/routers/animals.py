from fastapi import APIRouter

router = APIRouter(
    prefix="/animals",
    tags=["animals"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
