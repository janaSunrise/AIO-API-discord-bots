import os

import asyncpraw
from asyncpraw import exceptions
from loguru import logger

# -- Constants definition --
USER_AGENT = "AIO-API for discord bots"

IMGUR_LINKS = (
    "https://imgur.com/",
    "https://i.imgur.com/",
    "http://i.imgur.com/",
    "http://imgur.com",
    "https://m.imgur.com"
)
ACCEPTED_EXTENSIONS = (
    ".png",
    ".jpg",
    ".jpeg",
    ".gif"
)

# -- Reddit variable config --
reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
reddit_client_secret = os.getenv("REDDIT_CLIENT_SECRET")
nasa_api = os.getenv("NASA_API")

try:
    reddit = asyncpraw.Reddit(
        client_id=reddit_client_id,
        client_secret=reddit_client_secret,
        user_agent=USER_AGENT
    )
except exceptions.MissingRequiredAttributeException:
    logger.error("Please set correct reddit environment variables to run.")

# -- Subreddit config --
subreddits_list = {
    "memes": [
        "memes",
        "dankmemes",
        "funny",
        "ComedyCemetery",
        "wholesomememes",
        "meirl",
        "DeepFriedMemes",
    ],
    "funny": [
        "blackmagicfuckery",
        "OldSchoolCool",
        "nevertellmetheodds",
        "WatchPeopleDieInside",
        "BeAmazed",
        "mildlyinteresting",
        "MurderedByWords",
        "reactiongifs",
        "hmmm",
        "cursedimages",
        "nostalgia",
        "gifsthatkeepongiving",
        "Unexpected",
        "fakehistoryporn"
    ],
    "aww": [
        "AnimalsBeingJerks",
        "NatureIsFuckingLit",
        "WhatsWrongWithYourDog",
        "StartledCats",
        "natureismetal",
        "guineapigs",
        "Rabbits"
    ]
}

# -- 8Ball config --
BALL_REPLIES = {
    "positive": [
        "Yep.",
        "Absolutely!",
        "Can do!",
        "Affirmative!",
        "Yeah okay.",
        "Sure.",
        "Sure thing!",
        "You're the boss!",
        "Okay.",
        "No problem.",
        "I got you.",
        "Alright.",
        "You got it!",
        "ROGER THAT",
        "Of course!",
        "Aye aye, cap'n!",
        "I'll allow it.",
    ],
    "negative": [
        "Noooooo!!",
        "Nope.",
        "I'm sorry Dave, I'm afraid I can't do that.",
        "I don't think so.",
        "Not gonna happen.",
        "Out of the question.",
        "Huh? No.",
        "Nah.",
        "Naw.",
        "Not likely.",
        "No way, José.",
        "Not in a million years.",
        "Fat chance.",
        "Certainly not.",
        "NEGATORY.",
        "Nuh-uh.",
        "Not in my house!",
    ],
    "error": [
        "Please don't do that.",
        "You have to stop.",
        "Do you mind?",
        "In the future, don't do that.",
        "That was a mistake.",
        "You blew it.",
        "You're bad at computers.",
        "Are you trying to kill me?",
        "Noooooo!!",
        "I can't believe you've done this",
    ]
}

# -- study --
RESPONSES = {
    200: True,
    301: "Switching to a different endpoint",
    400: "Bad Request",
    401: "Not Authenticated",
    404: "The resource you tried to access wasn't found on the server.",
    403: "The resource you’re trying to access is forbidden — you don’t have the right permissions to see it.",
}

# -- Wolfram alpha --
DEFAULT_OUTPUT_FORMAT = "JSON"
QUERY = "http://api.wolframalpha.com/v2/{request}?{data}"
MAX_PODS = 20
