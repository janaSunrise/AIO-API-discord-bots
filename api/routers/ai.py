from fastapi import APIRouter

from api import AIML_KERNEL
from api.core import log_error

router = APIRouter(
    prefix="/ai",
    tags=["AI based endpoint."],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/")
@log_error()
async def root(message: str) -> dict:
    aiml_response = AIML_KERNEL.respond(message)
    aiml_response = aiml_response.replace("://", "").replace("@", "")  # Prevent tagging and links

    if len(aiml_response) > 1800:
        aiml_response = aiml_response[0:1800]

    return {
        "response": aiml_response
    }

