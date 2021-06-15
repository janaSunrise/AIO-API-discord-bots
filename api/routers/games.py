import random

from fastapi import APIRouter, Request

from api import config as conf
from api.core import log_error
from api.utils import get_random_text_response

router = APIRouter(
    prefix="/games",
    tags=["Games endpoints"],
    responses={404: {"description": "Not found"},},
)


# -- Router paths --
@router.get("/8ball")
@log_error()
async def ball8(_: Request, question: str) -> dict:
    """Play the game of 8 ball."""
    reply_type = random.randint(1, 3)

    if reply_type == 1:
        answer = random.choice(conf.BALL_REPLIES["positive"])
    elif reply_type == 2:
        answer = random.choice(conf.BALL_REPLIES["negative"])
    else:
        answer = random.choice(conf.BALL_REPLIES["error"])

    return {"question": question, "answer": answer}


@router.get("/truth")
@log_error()
async def truth(_: Request) -> dict:
    """Get a random truth question."""
    truth_resp = get_random_text_response("truths")

    return {"truth": truth_resp}


@router.get("/dares")
@log_error()
async def dares(_: Request):
    """Get a random dare."""
    dare_resp = get_random_text_response("dares")

    return {"dare": dare_resp}


@router.get("/neverhaveiever")
@log_error()
async def nhie(_: Request) -> dict:
    """Play never have I ever."""
    nhie_resp = get_random_text_response("nhie")

    return {"never_have_i_ever": f"Have you ever ..{nhie_resp}"}


@router.get("/wouldyourrather")
@log_error()
async def wyr(_: Request) -> dict:
    """Play would you rather."""
    wyr_resp = get_random_text_response("wyr")

    return {"would_you_rather": f"Would you rather ..{wyr_resp}"}
