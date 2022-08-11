from __future__ import annotations

import random

from fastapi import APIRouter

from api.config import BALL_REPLIES, text_game_responses

router = APIRouter(
    prefix="/games",
    tags=["Games endpoints"],
    responses={
        404: {"description": "Not found"},
    },
)

get_random_text_response = lambda category: random.choice(text_game_responses[category])


@router.get("/8ball")
async def ball8(question: str) -> dict[str, str]:
    """Play the game of 8 ball."""
    reply_type = random.randint(1, 3)
    reply_type_map = {
        1: "positive",
        2: "negative",
        3: "error",
    }

    answer = random.choice(BALL_REPLIES[reply_type_map[reply_type]])

    return {"question": question, "answer": answer}


@router.get("/truth")
async def truth() -> dict[str, str]:
    """Get a random truth question."""
    truth_resp = get_random_text_response("truths")

    return {"truth": truth_resp}


@router.get("/dares")
async def dares() -> dict[str, str]:
    """Get a random dare."""
    dare_resp = get_random_text_response("dares")

    return {"dare": dare_resp}


@router.get("/neverhaveiever")
async def nhie() -> dict[str, str]:
    """Play never have I ever."""
    nhie_resp = get_random_text_response("nhie")

    return {"never_have_i_ever": f"Have you ever ..{nhie_resp}"}


@router.get("/wouldyourather")
async def wyr() -> dict[str, str]:
    """Play would you rather."""
    wyr_resp = get_random_text_response("wyr")

    return {"would_you_rather": f"Would you rather ..{wyr_resp}"}
