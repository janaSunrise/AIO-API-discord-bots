import functools
import importlib
import pkgutil
import types
import typing as t

from loguru import logger

from .. import routers


def log_error() -> t.Callable:
    """Decorator for logging errors."""

    def error_logging(func: t.Callable) -> t.Callable:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs) -> t.Any:
            logger_ = logger.opt(depth=1)

            try:
                return await func(*args, **kwargs)
            except Exception as e:
                logger_.error(
                    f"ERROR: {e!r} | Location: {func.__name__}", exc_info=True
                )
                return {"error": f"{e!r} | Please try again later."}

        return wrapper

    return error_logging


def get_module_name(name: str) -> str:
    return name.split(".")[-1]


def is_a_route(module: types.ModuleType) -> bool:
    imported = importlib.import_module(module.name)
    return hasattr(imported, "router")


def get_modules_list(
    package: types.ModuleType, check: t.Optional[types.FunctionType] = None
) -> t.List[str]:
    """Get the list of the submodules from the specified package."""
    modules = []

    for submodule in pkgutil.walk_packages(package.__path__, f"{package.__name__}."):
        if get_module_name(submodule.name).startswith("_"):
            continue

        if check and not check(submodule):
            continue

        modules.append(submodule.name)

    return modules


ROUTES = get_modules_list(routers, check=is_a_route)
