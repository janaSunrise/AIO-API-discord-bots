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

from api import routers


# -- AIOHTTP client --
class HttpClient:
    """HTTP client used for requests."""

    _session: t.Optional[aiohttp.ClientSession] = None
    _tcp_session: t.Optional[aiohttp.ClientSession] = None

    def start(self) -> None:
        """Start the client."""
        self._session = aiohttp.ClientSession()
        self._tcp_session = aiohttp.ClientSession(
            connector=aiohttp.TCPConnector()
        )

    @property
    def session(self) -> aiohttp.ClientSession:
        """Return the session, raising an error if there isn't any."""
        if not self._session:
            raise ValueError("Instance isn't started")
        return self._session

    @property
    def tcp_session(self) -> aiohttp.ClientSession:
        """Return the tcp session, raising an error if there isn't any."""
        if not self._tcp_session:
            raise ValueError("Instance isn't started")
        return self._tcp_session

    async def stop(self) -> None:
        """Stop the client"""
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
    version=conf.VERSION,
    description=(
        "The only api you'll ever need to make your discord bot spicy, "
        "fun and stand out."
    ),
    docs_url="/",
    redoc_url=None
)


# -- Event handlers --
@app.on_event("startup")
async def on_start_up() -> None:
    """Initialize stuff on startup."""
    http_client.start()


@app.on_event("shutdown")
async def on_shutdown() -> None:
    """Cleanup hook."""
    await http_client.stop()


# -- Configure the limiter --
limiter = Limiter(key_func=get_remote_address, default_limits=["25/minute"])
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

# -- Logger configuration --
logger.configure(handlers=[
    dict(sink=sys.stdout, format=conf.log_format, level=conf.log_level),
    dict(
        sink=conf.log_file,
        format=conf.log_format,
        level=conf.log_level,
        rotation="500 MB",
    ),
])

# -- AI section
if conf.ai_enabled:
    AIML_KERNEL = aiml.Kernel()
    AIML_KERNEL.setBotPredicate("name", "Overflow")
    AIML_KERNEL.bootstrap(
        learnFiles=["api/std-startup.xml"],
        commands=["LOAD AIML B"]
    )

for router in conf.ROUTERS:
    if hasattr(routers, router):
        app.include_router(getattr(routers, router).router)
    else:
        logger.warning(f"Router {router} included but not found")

# -- AI Section --
if conf.ai_enabled:
    app.include_router(routers.ai.router)
