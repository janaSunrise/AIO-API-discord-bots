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

# -- Logger configuration --
log_file = "logs/server.log"
log_level = "INFO"
log_format = "<green>{time:YYYY-MM-DD hh:mm:ss}</green> | <level>{level: <8}</level> | " \
             "<cyan>{name: <18}</cyan> | <level>{message}</level>"

# -- Reddit variable config --
reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
reddit_client_secret = os.getenv("REDDIT_CLIENT_SECRET")
nasa_api = os.getenv("NASA_API")
ai_enabled = os.getenv("AI_ENABLED", default="false").lower() in ["true", 1]

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

nsfw_subreddits_list = {
    "all": [
        "gonewild",
        "nsfw",
        "RealGirls",
        "NSFW_GIF",
        "holdthemoan",
        "BustyPetite",
        "LegalTeens",
        "cumsluts",
        "PetiteGoneWild",
        "realmoms",
        "milf",
        "gonewild30plus",
        "legalteens",
        "collegesluts",
        "gonewild18",
        "fauxbait",
        "realgirls",
        "amateur",
        "nsfw_amateurs",
        "funwithfriends",
        "camsluts",
        "streamersgonewild",
        "ratemynudebody",
        "goneerotic",
        "gwpublic",
        "gonewildcouples",
        "gwcumsluts",
        "gonewildcurvy",
        "BigBoobsGW",
        "mycleavage",
        "AsiansGoneWild",
        "latinasgw",
        "indiansgonewild",
        "workgonewild",
        "GoneWildScrubs",
        "NSFW_Snapchat",
        "snapleaks",
        "wifesharing",
        "hotwife",
        "slutwife",
        "wouldyoufuckmywife",
        "yogapants",
        "boobies",
        "boobs",
        "tits",
        "breastenvy",
        "BustyPetite",
        "hugeboobs",
        "stacked",
        "2busty2hide",
        "pokies",
        "nipples",
        "lactation",
        "stockings",
        "legs",
        "tightshorts",
        "pussy",
        "innie",
        "LabiaGW",
        "godpussy",
        "hairypussy",
        "breakingtheseal",
        "SexyTummies",
        "thick",
        "SlimThick",
        "dirtysmall",
        "cumsluts",
        "GirlsFinishingTheJob",
        "impressedbycum",
        "wetfetish",
        "NSFW_GIFS",
        "Ass",
        "BigAsses",
        "NSFW_HTML5",
        "peegonewild",
        "iWantToFuckHer",
        "curvy",
        "petite",
        "OnOff"
    ],
    "fourk": [
        "HighResNSFW",
        "UHDnsfw",
        "nsfw_hd",
        "NSFW_Wallpapers",
        "closeup"
    ],
    "ahegao": [
        "AhegaoGirls",
        "RealAhegao",
        "EyeRollOrgasm",
        "MouthWideOpen",
        "O_Faces"
    ],
    "ass": [
        "ass",
        "pawg",
        "AssholeBehindThong",
        "girlsinyogapants",
        "girlsinleggings",
        "bigasses",
        "asshole",
        "AssOnTheGlass",
        "TheUnderbun",
        "asstastic",
        "booty",
        "AssReveal",
        "beautifulbutt",
        "Mooning",
        "BestBooties",
        "brunetteass",
        "assinthong",
        "paag",
        "asstastic",
        "GodBooty",
        "Underbun",
        "datass",
        "ILikeLittleButts",
        "datgap"
    ],
    "anal":  [
        "MasterOfAnal",
        "analgonewild",
        "anal",
        "buttsex",
        "buttsthatgrip",
        "AnalGW",
        "analinsertions",
        "AnalGW",
        "assholegonewild"
    ],
    "bdsm": [
        "BDSMGW",
        "bdsm",
        "ropeart",
        "shibari"
    ],
    "blowjob": [
        "blowjobsandwich",
        "Blowjobs",
        "BlowjobGifs",
        "BlowjobEyeContact",
        "blowbang",
        "AsianBlowjobs",
        "SuckingItDry",
        "OralCreampie",
        "SwordSwallowers"
    ],
    "boobs": [
        "boobs",
        "TheHangingBoobs",
        "bigboobs",
        "BigBoobsGW",
        "hugeboobs",
        "pokies",
        "ghostnipples",
        "PiercedNSFW",
        "piercedtits",
        "PerfectTits",
        "BestTits",
        "Boobies",
        "JustOneBoob",
        "tits",
        "naturaltitties",
        "smallboobs",
        "Nipples",
        "homegrowntits",
        "TheUnderboob",
        "BiggerThanYouThought",
        "fortyfivefiftyfive",
        "Stacked",
        "BigBoobsGonewild",
        "AreolasGW",
        "TittyDrop",
        "Titties",
        "Boobies",
        "boobbounce",
        "TinyTits",
        "cleavage",
        "BoobsBetweenArms",
        "BustyNaturals",
        "burstingout"
    ],
    "cunnilingus": [
        "cunnilingus",
        "CunnilingusSelfie",
        "Hegoesdown"
    ],
    "bottomless": [
        "upskirt",
        "Bottomless",
        "nopanties",
        "Pantiesdown"
    ],
    "cumshots": [
        "OralCreampie",
        "cumfetish",
        "cumontongue",
        "cumshots",
        "CumshotSelfies",
        "facialcumshots",
        "pulsatingcumshots",
        "gwcumsluts",
        "ImpresssedByCum",
        "GirlsFinishingTheJob",
        "amateurcumsluts",
        "unexpectedcum",
        "bodyshots",
        "ContainTheLoad",
        "bodyshots"
    ],
    "dick": [
        "DickPics4Freedom",
        "mangonewild",
        "MassiveCock",
        "penis",
        "cock",
        "ThickDick"
    ],
    "doublepenetration":  [
        "doublepenetration",
        "dp_porn",
        "Technical_DP"
    ],
    "deepthroat": [
        "DeepThroatTears",
        "deepthroat",
        "SwordSwallowers"
    ],
    "gay":  [
        "gayporn",
        "ladybonersgw",
        "mangonewild"
    ],
    "group": [
        "GroupOfNudeGirls",
        "GroupOfNudeMILFs",
        "groupsex"
    ],
    "hentai": [
        "hentai",
        "thick_hentai",
        "HQHentai",
        "AnimeBooty",
        "thighdeology",
        "ecchigifs",
        "nsfwanimegifs",
        "oppai_gif"
    ],
    "lesbian": [
        "lesbians",
        "HDLesbianGifs",
        "amateurlesbians",
        "Lesbian_gifs"
    ],
    "milf": [
        "amateur_milfs",
        "GroupOfNudeMILFs",
        "ChocolateMilf",
        "milf",
        "Milfie",
        "hairymilfs",
        "HotAsianMilfs",
        "HotMILFs",
        "MILFs",
        "maturemilf",
        "puremilf",
        "amateur_milfs"
    ],
    "public": [
        "RealPublicNudity",
        "FlashingAndFlaunting",
        "FlashingGirls",
        "PublicFlashing",
        "Unashamed",
        "NudeInPublic",
        "publicplug",
        "casualnudity"
    ],
    "rule34": [
        "rule34",
        "rule34cartoons",
        "Rule_34",
        "Rule34LoL",
        "AvatarPorn",
        "Overwatch_Porn",
        "Rule34Overwatch",
        "WesternHentai"
    ],
    "thigh": [
        "Thighs",
        "ThickThighs",
        "thighhighs",
        "Thigh",
        "leggingsgonewild"
    ],
    "trap": [
        "Transex",
        "DeliciousTraps",
        "traps",
        "trapgifs",
        "GoneWildTrans",
        "SexyShemales",
        "Shemales",
        "shemale_gifs",
        "Shemales",
        "ShemalesParadise",
        "Shemale_Big_Cock",
        "ShemaleGalleries"
    ],
    "wild": [
        "gonewild",
        "GWNerdy",
        "dirtysmall",
        "MyCalvins",
        "AsiansGoneWild",
        "GoneWildSmiles",
        "gonewildcurvy",
        "BigBoobsGonewild",
        "gonewildcouples",
        "gonewildcolor",
        "PetiteGoneWild",
        "GWCouples",
        "BigBoobsGW",
        "altgonewild",
        "LabiaGW",
        "UnderwearGW",
        "JustTheTop",
        "TallGoneWild",
        "LingerieGW",
        "Swingersgw",
        "workgonewild"
    ],
    "redhead": [
        "redheadxxx",
        "redheads",
        "ginger",
        "FireBush",
        "FreckledRedheads",
        "redhead",
        "thesluttyginger",
        "RedheadGifs"
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
