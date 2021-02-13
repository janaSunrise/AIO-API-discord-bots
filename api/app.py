import aiohttp
from fastapi import FastAPI


# -- AIOHTTP client --
class HttpClient:
    session: aiohttp.ClientSession = None

    def start(self):
        self.session = aiohttp.ClientSession()

    async def stop(self):
        await self.session.close()
        self.session = None

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

# -- Imports for router --

from api.routers import (
    animals,
    comics,
    fun,
    funny,
    games,
    gifs,
    images,
    memes
)

# -- Include the routers --
app.include_router(animals.router)
app.include_router(comics.router)
app.include_router(fun.router)
app.include_router(funny.router)
app.include_router(games.router)
app.include_router(gifs.router)
app.include_router(images.router)
app.include_router(memes.router)
