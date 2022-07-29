from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler  # type: ignore
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address

from .config import APIConfig
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


# Configure the ratelimiting
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)
