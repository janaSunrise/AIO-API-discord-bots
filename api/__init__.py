import importlib
import sys

import aiml
from fastapi import FastAPI
from loguru import logger
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address

from api import config as conf
from api import routers

from .core import ROUTES
from .models import HttpClient

# -- Define the API --
app = FastAPI(
    title="AIO API",
    version=conf.VERSION,
    description=(
        "The only api you'll ever need to make your discord bot spicy, "
        "fun and stand out."
    ),
    docs_url="/",
    redoc_url=None,
)


# -- Event handlers --
@app.on_event("startup")
async def on_start_up() -> None:
    """Initialize stuff on startup."""
    app.state.http_client = HttpClient()
    app.state.http_client.start()


@app.on_event("shutdown")
async def on_shutdown() -> None:
    """Cleanup hook."""
    await app.state.http_client.stop()


# -- Configure the limiter --
limiter = Limiter(key_func=get_remote_address, default_limits=["1/2 seconds"])

app.state.limiter = limiter

app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

# -- Logger configuration --
logger.configure(
    handlers=[
        dict(sink=sys.stdout, format=conf.log_format, level=conf.log_level),
        dict(
            sink=conf.log_file,
            format=conf.log_format,
            level=conf.log_level,
            rotation="300 MB",
        ),
    ]
)

# Chatbot
if conf.ai_enabled:
    AIML_KERNEL = aiml.Kernel()
    AIML_KERNEL.setBotPredicate("name", "Overflow")
    AIML_KERNEL.bootstrap(learnFiles=["api/std-startup.xml"], commands=["LOAD AIML B"])

    app.include_router(routers.ai.router)

# Auto route loader
for route in ROUTES:
    router = importlib.import_module(route)

    if hasattr(router, "router"):
        app.include_router(getattr(router, "router"))
    else:
        print(f"[WARNING] Router {router.__name__} included but not found")
