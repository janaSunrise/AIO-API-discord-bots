import random

from fastapi import APIRouter, Request

from api import config as conf
from api.core import log_error
from api.utils import get_random_text_response

router = APIRouter(
    prefix="/games",
    tags=["Games endpoints"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/8ball")
@log_error()
async def ball8(request: Request, question: str) -> dict:
    reply_type = random.randint(1, 3)

    if reply_type == 1:
        answer = random.choice(conf.BALL_REPLIES["positive"])
    elif reply_type == 2:
        answer = random.choice(conf.BALL_REPLIES["negative"])
    elif reply_type == 3:
        answer = random.choice(conf.BALL_REPLIES["error"])

    return {
        "question": question,
        "answer": answer
    }


@router.get("/truth")
@log_error()
async def truth(request: Request) -> dict:
    truth_resp = get_random_text_response("truths")

    return {"truth": truth_resp}


@router.get("/dares")
@log_error()
async def dares(request: Request):
    dare_resp = get_random_text_response("dares")

    return {"dare": dare_resp}


@router.get("/neverhaveiever")
@log_error()
async def nhie(request: Request) -> dict:
    nhie_resp = get_random_text_response("nhie")

    return {"never_have_i_ever": f"Have you ever ..{nhie_resp}"}


@router.get("/wouldyourrather")
@log_error()
async def wyr(request: Request) -> dict:
    wyr_resp = get_random_text_response("wyr")

    return {"would_you_rather": f"Would you rather ..{wyr_resp}"}
