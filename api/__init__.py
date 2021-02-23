import sys
import typing as t

import aiml
import aiohttp
from fastapi import FastAPI
from loguru import logger
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address

from api import config as conf


# -- AIOHTTP client --
class HttpClient:
    _session: t.Optional[aiohttp.ClientSession] = None
    _tcp_session: t.Optional[aiohttp.ClientSession] = None

    def start(self) -> None:
        self._session = aiohttp.ClientSession()
        self._tcp_session = aiohttp.ClientSession(
            connector=aiohttp.TCPConnector()
        )

    @property
    def session(self) -> aiohttp.ClientSession:
        if not self._session:
            raise ValueError("Instance isn't started")
        return self._session

    @property
    def tcp_session(self) -> aiohttp.ClientSession:
        if not self._tcp_session:
            raise ValueError("Instance isn't started")
        return self._tcp_session

    async def stop(self) -> None:
        await self.session.close()
        await self.tcp_session.close()

        self._session = None
        self._tcp_session = None

    def __call__(self) -> aiohttp.ClientSession:
        return self.session


http_client = HttpClient()


# -- Define the API --
app = FastAPI(
    title="AIO API",
    version="0.1.0",
    description="The only api you'll ever need to make your discord bot spicy, fun and stand out.",
    docs_url="/",
    redoc_url=None
)
global redis


# -- Event handlers --
@app.on_event("startup")
async def on_start_up() -> None:
    http_client.start()


@app.on_event("shutdown")
async def on_shutdown() -> None:
    await http_client.stop()


# -- Configure the limiter --
limiter = Limiter(key_func=get_remote_address, default_limits=["15/minute"])
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

# -- AI section
if conf.ai_enabled:
    AIML_KERNEL = aiml.Kernel()
    AIML_KERNEL.setBotPredicate("name", "Overflow")
    AIML_KERNEL.bootstrap(learnFiles=["api/std-startup.xml"], commands=["LOAD AIML B"])

# -- Imports for router --
from api.routers import (
    animals,
    comics,
    fun,
    lyrics,
    games,
    gifs,
    images,
    main,
    nasa,
    neko,
    nsfw,
    reddit,
    search,
    study
)

# -- Include the routers --
app.include_router(animals.router)
app.include_router(comics.router)
app.include_router(fun.router)
app.include_router(lyrics.router)
app.include_router(games.router)
app.include_router(gifs.router)
app.include_router(images.router)
app.include_router(main.router)
app.include_router(nasa.router)
app.include_router(neko.router)
app.include_router(nsfw.router)
app.include_router(reddit.router)
app.include_router(search.router)
app.include_router(study.router)

# -- AI Section --
if conf.ai_enabled:
    from api.routers import ai
    app.include_router(ai.router)


# -- Logger configuration --
logger.configure(handlers=[
    dict(sink=sys.stdout, format=conf.log_format, level=conf.log_level),
    dict(sink=conf.log_file, format=conf.log_format, level=conf.log_level, rotation="500 MB")
])
