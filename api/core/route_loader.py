from __future__ import annotations

import importlib
import pkgutil
import types
from typing import Iterable, NoReturn

from .. import routers


def get_module_name(name: str) -> str:
    return name.split(".")[-1]


def get_modules_list(package: types.ModuleType) -> Iterable[str]:
    def on_error(name: str) -> NoReturn:
        raise ImportError(name=name)

    for submodule in pkgutil.walk_packages(
        package.__path__,
        f"{package.__name__}.",
        onerror=on_error,
    ):
        if get_module_name(submodule.name).startswith("_"):
            continue

        imported = importlib.import_module(submodule.name)

        if not hasattr(imported, "router"):
            continue

        # If the module has the attribute `__autoload__` set to False, skip.
        if not getattr(imported, "__autoload__", True):
            continue

        yield submodule.name


ROUTES = get_modules_list(routers)
