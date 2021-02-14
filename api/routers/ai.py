from fastapi import APIRouter
from loguru import logger

from api import AIML_KERNEL

router = APIRouter(
    prefix="/ai",
    tags=["ai"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/")
async def root(message: str):
    try:
        aiml_response = AIML_KERNEL.respond(message)
        aiml_response = aiml_response.replace("://", "").replace("@", "")  # Prevent tagging and links

        if len(aiml_response) > 1800:
            aiml_response = aiml_response[0:1800]

        return {
            "response": aiml_response
        }
    except Exception as e:
        logger.critical(f"General Error: {e}")

