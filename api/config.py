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
    "memes": frozenset({
        "ComedyCemetery",
        "dankmemes",
        "DeepFriedMemes",
        "funny",
        "meirl",
        "memes",
        "wholesomememes",
    }),
    "funny": frozenset({
        "BeAmazed",
        "blackmagicfuckery",
        "cursedimages",
        "fakehistoryporn",
        "gifsthatkeepongiving",
        "hmmm",
        "mildlyinteresting",
        "MurderedByWords",
        "nevertellmetheodds",
        "nostalgia",
        "OldSchoolCool",
        "reactiongifs",
        "Unexpected",
        "WatchPeopleDieInside",
    }),
    "aww": frozenset({
        "AnimalsBeingJerks",
        "guineapigs",
        "NatureIsFuckingLit",
        "natureismetal",
        "Rabbits",
        "StartledCats",
        "WhatsWrongWithYourDog",
    })
}

nsfw_subreddits_list = {
    "all": frozenset({
        "2busty2hide",
        "amateur",
        "AsiansGoneWild",
        "Ass",
        "BigAsses",
        "BigBoobsGW",
        "boobies",
        "boobs",
        "breakingtheseal",
        "breastenvy",
        "BustyPetite",
        "camsluts",
        "collegesluts",
        "cumsluts",
        "curvy",
        "dirtysmall",
        "fauxbait",
        "funwithfriends",
        "GirlsFinishingTheJob",
        "godpussy",
        "goneerotic",
        "gonewild",
        "gonewild18",
        "gonewild30plus",
        "gonewildcouples",
        "gonewildcurvy",
        "GoneWildScrubs",
        "gwcumsluts",
        "gwpublic",
        "hairypussy",
        "holdthemoan",
        "hotwife",
        "hugeboobs",
        "impressedbycum",
        "indiansgonewild",
        "innie",
        "iWantToFuckHer",
        "LabiaGW",
        "lactation",
        "latinasgw",
        "LegalTeens",
        "legalteens",
        "legs",
        "milf",
        "mycleavage",
        "nipples",
        "nsfw",
        "nsfw_amateurs",
        "NSFW_GIF",
        "NSFW_GIFS",
        "NSFW_HTML5",
        "NSFW_Snapchat",
        "OnOff",
        "peegonewild",
        "petite",
        "PetiteGoneWild",
        "pokies",
        "pussy",
        "ratemynudebody",
        "RealGirls",
        "realgirls",
        "realmoms",
        "SexyTummies",
        "SlimThick",
        "slutwife",
        "snapleaks",
        "stacked",
        "stockings",
        "streamersgonewild",
        "thick",
        "tightshorts",
        "tits",
        "wetfetish",
        "wifesharing",
        "workgonewild",
        "wouldyoufuckmywife",
        "yogapants",
    }),
    "fourk": frozenset({
        "closeup",
        "HighResNSFW",
        "nsfw_hd",
        "NSFW_Wallpapers",
        "UHDnsfw",
    }),
    "ahegao": frozenset({
        "AhegaoGirls",
        "EyeRollOrgasm",
        "MouthWideOpen",
        "O_Faces",
        "RealAhegao",
    }),
    "ass": frozenset({
        "ass",
        "asshole",
        "AssholeBehindThong",
        "assinthong",
        "AssOnTheGlass",
        "AssReveal",
        "asstastic",
        "beautifulbutt",
        "BestBooties",
        "bigasses",
        "booty",
        "brunetteass",
        "datass",
        "datgap",
        "girlsinleggings",
        "girlsinyogapants",
        "GodBooty",
        "ILikeLittleButts",
        "Mooning",
        "paag",
        "pawg",
        "TheUnderbun",
        "Underbun",
    }),
    "anal":  frozenset({
        "anal",
        "analgonewild",
        "AnalGW",
        "analinsertions",
        "assholegonewild",
        "buttsex",
        "buttsthatgrip",
        "MasterOfAnal",
    }),
    "bdsm": frozenset({
        "bdsm",
        "BDSMGW",
        "ropeart",
        "shibari",
    }),
    "blowjob": frozenset({
        "AsianBlowjobs",
        "blowbang",
        "BlowjobEyeContact",
        "BlowjobGifs",
        "Blowjobs",
        "blowjobsandwich",
        "OralCreampie",
        "SuckingItDry",
        "SwordSwallowers",
    }),
    "boobs": frozenset({
        "AreolasGW",
        "BestTits",
        "bigboobs",
        "BigBoobsGonewild",
        "BigBoobsGW",
        "BiggerThanYouThought",
        "boobbounce",
        "Boobies",
        "boobs",
        "BoobsBetweenArms",
        "burstingout"
        "BustyNaturals",
        "cleavage",
        "fortyfivefiftyfive",
        "ghostnipples",
        "homegrowntits",
        "hugeboobs",
        "JustOneBoob",
        "naturaltitties",
        "Nipples",
        "PerfectTits",
        "PiercedNSFW",
        "piercedtits",
        "pokies",
        "smallboobs",
        "Stacked",
        "TheHangingBoobs",
        "TheUnderboob",
        "TinyTits",
        "tits",
        "Titties",
        "TittyDrop",
    }),
    "cunnilingus": frozenset({
        "cunnilingus",
        "CunnilingusSelfie",
        "Hegoesdown",
    }),
    "bottomless": frozenset({
        "Bottomless",
        "nopanties",
        "Pantiesdown",
        "upskirt",
    }),
    "cumshots": frozenset({
        "amateurcumsluts",
        "bodyshots",
        "ContainTheLoad",
        "cumfetish",
        "cumontongue",
        "cumshots",
        "CumshotSelfies",
        "facialcumshots",
        "GirlsFinishingTheJob",
        "gwcumsluts",
        "ImpresssedByCum",
        "OralCreampie",
        "pulsatingcumshots",
        "unexpectedcum",
    }),
    "dick": frozenset({
        "cock",
        "DickPics4Freedom",
        "mangonewild",
        "MassiveCock",
        "penis",
        "ThickDick",
    }),
    "doublepenetration": frozenset({
        "doublepenetration",
        "dp_porn",
        "Technical_DP",
    }),
    "deepthroat": frozenset({
        "deepthroat",
        "DeepThroatTears",
        "SwordSwallowers",
    }),
    "gay": frozenset({
        "gayporn",
        "ladybonersgw",
        "mangonewild",
    }),
    "group": frozenset({
        "GroupOfNudeGirls",
        "GroupOfNudeMILFs",
        "groupsex",
    }),
    "hentai": frozenset({
        "AnimeBooty",
        "ecchigifs",
        "hentai",
        "HQHentai",
        "nsfwanimegifs",
        "oppai_gif",
        "thick_hentai",
        "thighdeology",
    }),
    "lesbian": frozenset({
        "amateurlesbians",
        "HDLesbianGifs",
        "lesbians",
        "Lesbian_gifs",
    }),
    "milf": frozenset({
        "amateur_milfs",
        "ChocolateMilf",
        "GroupOfNudeMILFs",
        "hairymilfs",
        "HotAsianMilfs",
        "HotMILFs",
        "maturemilf",
        "milf",
        "Milfie",
        "MILFs",
        "puremilf",
    }),
    "public": frozenset({
        "casualnudity",
        "FlashingAndFlaunting",
        "FlashingGirls",
        "NudeInPublic",
        "PublicFlashing",
        "publicplug",
        "RealPublicNudity",
        "Unashamed",
    }),
    "rule34": frozenset({
        "AvatarPorn",
        "Overwatch_Porn",
        "rule34",
        "rule34cartoons",
        "Rule34LoL",
        "Rule34Overwatch",
        "Rule_34",
        "WesternHentai",
    }),
    "thigh": frozenset({
        "leggingsgonewild",
        "ThickThighs",
        "Thigh",
        "thighhighs",
        "Thighs",
    }),
    "trap": frozenset({
        "DeliciousTraps",
        "GoneWildTrans",
        "SexyShemales",
        "ShemaleGalleries",
        "Shemales",
        "ShemalesParadise",
        "Shemale_Big_Cock",
        "shemale_gifs",
        "Transex",
        "trapgifs",
        "traps",
    }),
    "wild": frozenset({
        "altgonewild",
        "AsiansGoneWild",
        "BigBoobsGonewild",
        "BigBoobsGW",
        "dirtysmall",
        "gonewild",
        "gonewildcolor",
        "gonewildcouples",
        "gonewildcurvy",
        "GoneWildSmiles",
        "GWCouples",
        "GWNerdy",
        "JustTheTop",
        "LabiaGW",
        "LingerieGW",
        "MyCalvins",
        "PetiteGoneWild",
        "Swingersgw",
        "TallGoneWild",
        "UnderwearGW",
        "workgonewild",
    }),
    "redhead": frozenset({
        "FireBush",
        "FreckledRedheads",
        "ginger",
        "redhead",
        "RedheadGifs",
        "redheads",
        "redheadxxx",
        "thesluttyginger",
    }),
}

# -- 8Ball config --
BALL_REPLIES = {
    "positive": frozenset({
        "Absolutely!",
        "Affirmative!",
        "Alright.",
        "Aye aye, cap'n!",
        "Can do!",
        "I'll allow it.",
        "I got you.",
        "No problem.",
        "Of course!",
        "Okay.",
        "ROGER THAT",
        "Sure.",
        "Sure thing!",
        "Yeah okay.",
        "Yep.",
        "You got it!",
        "You're the boss!",
    }),
    "negative": frozenset({
        "Certainly not.",
        "Fat chance.",
        "Huh? No.",
        "I don't think so.",
        "I'm sorry Dave, I'm afraid I can't do that.",
        "Nah.",
        "Naw.",
        "NEGATORY.",
        "No way, José.",
        "Noooooo!!",
        "Nope.",
        "Not gonna happen.",
        "Not in a million years.",
        "Not in my house!",
        "Not likely.",
        "Nuh-uh.",
        "Out of the question.",
    }),
    "error": frozenset({
        "Are you trying to kill me?",
        "Do you mind?",
        "I can't believe you've done this",
        "In the future, don't do that.",
        "Noooooo!!",
        "Please don't do that.",
        "That was a mistake.",
        "You blew it.",
        "You have to stop.",
        "You're bad at computers.",
    }),
}

# -- study --
RESPONSES = {
    200: True,
    301: "Switching to a different endpoint",
    400: "Bad Request",
    401: "Not Authenticated",
    404: "The resource you tried to access wasn't found on the server.",
    403: (
        "The resource you’re trying to access is forbidden — "
        "you don’t have the right permissions to see it."
    ),
}

# -- Wolfram alpha --
DEFAULT_OUTPUT_FORMAT = "JSON"
QUERY = "http://api.wolframalpha.com/v2/{request}?{data}"
MAX_PODS = 20
