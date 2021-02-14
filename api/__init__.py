import sys

import aiohttp
import aiml
from fastapi import FastAPI
from loguru import logger

from api import config as conf


# -- AIOHTTP client --
class HttpClient:
    session: aiohttp.ClientSession = None
    tcp_session: aiohttp.ClientSession = None

    def start(self):
        self.session = aiohttp.ClientSession()
        self.tcp_session = aiohttp.ClientSession(connector=aiohttp.TCPConnector())

    async def stop(self):
        await self.session.close()
        await self.tcp_session.close()

        self.session = None
        self.tcp_session = None

    def __call__(self) -> aiohttp.ClientSession:
        assert self.session is not None
        return self.session


http_client = HttpClient()


# -- Event handlers --
async def on_start_up() -> None:
    http_client.start()


async def on_shutdown() -> None:
    await http_client.stop()


# -- Define the API --
app = FastAPI(docs_url="/", on_startup=[on_start_up], on_shutdown=[on_shutdown])

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
