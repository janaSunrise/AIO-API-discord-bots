import importlib
from typing import Callable

from fastapi import FastAPI, Request, Response
from loguru import logger
from slowapi import Limiter, _rate_limit_exceeded_handler  # type: ignore
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address

from .config import APIConfig
from .core.route_loader import ROUTES
from .utils.http_client import HTTPClient

app = FastAPI(
    title="AIO API",
    version=APIConfig.VERSION,
    debug=APIConfig.DEBUG,
    docs_url="/",
    redoc_url=None,
)


@app.on_event("startup")
async def on_start_up() -> None:
    """Initialize stuff on startup."""
    app.state.http_client = HTTPClient()
    app.state.limiter = Limiter(
        key_func=get_remote_address, default_limits=["1/2 seconds"]
    )


@app.on_event("shutdown")
async def on_shutdown() -> None:
    """Cleanup hook."""
    await app.state.http_client.stop()


@app.middleware("http")
async def error_handler(request: Request, callnext: Callable) -> Response:
    try:
        return await callnext(request)
    except Exception as exc:
        log = logger.opt(depth=1)

        log.error(f"Error: {exc!r}", exc_info=True)

        return Response("Internal server error", status_code=500)


# Configure the ratelimiting
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

# Load all the routes dynamically
for route in ROUTES:
    router = importlib.import_module(route)

    if hasattr(router, "router"):
        app.include_router(router.router)
    else:
        logger.warning(f"Router {router.__name__} included but not found")
