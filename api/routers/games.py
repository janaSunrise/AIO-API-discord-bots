import random

from fastapi import APIRouter

from api import config as conf
from api.utils import get_random_text_response

router = APIRouter(
    prefix="/games",
    tags=["games"],
    responses={
        404: {"description": "Not found"},
    },
)


# -- Router paths --
@router.get("/8ball")
async def ball8(question: str):
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
async def truth():
    truth_resp = get_random_text_response("truths")

    return {
        "truth": truth_resp
    }


@router.get("/dares")
async def dares():
    dare_resp = get_random_text_response("dares")

    return {
        "dare": dare_resp
    }


@router.get("/neverhaveiever")
async def nhie():
    nhie_resp = get_random_text_response("nhie")

    return {
        "never_have_i_ever": "Have you ever .." + nhie_resp
    }


@router.get("/wouldyourrather")
async def wyr():
    wyr_resp = get_random_text_response("wyr")

    return {
        "would_you_rather": "Would you rather .." + wyr_resp
    }
