import functools

from loguru import logger


# -- Decorators --
def log_error():
    """Decorator for logging errors."""
    def error_logging(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                logger.error(f"ERROR: {e!r} | Location: {func.__name__}")
                return {"error": f"{e!r}"}

        return wrapper
    return error_logging
