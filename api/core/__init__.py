import functools
import typing as t

from loguru import logger


# -- Decorators --
def log_error() -> t.Any:
    """Decorator for logging errors."""

    def error_logging(func: t.Callable) -> t.Callable:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs) -> t.Any:
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                logger.error(f"ERROR: {e!r} | Location: {func.__name__}")
                return {"error": f"{e!r} | Please try again later."}

        return wrapper

    return error_logging
