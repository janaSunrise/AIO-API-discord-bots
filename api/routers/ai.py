from fastapi import APIRouter, Request

from api.core import log_error

router = APIRouter(
    prefix="/ai",
    tags=["AI based endpoint"],
    responses={404: {"description": "Not found"},},
)


# -- Router paths --
@router.get("/")
@log_error()
async def chatbot(_: Request, message: str) -> dict:
    """The chatbot endpoint to simulate a person talking."""
    from api import AIML_KERNEL  # To prevent circular import

    aiml_response = AIML_KERNEL.respond(message)
    aiml_response = aiml_response.replace("://", "").replace("@", "")

    if len(aiml_response) > 1800:
        aiml_response = aiml_response[:1800]

    return {"response": aiml_response}
