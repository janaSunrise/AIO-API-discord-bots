import sys

from loguru import logger

from .app import app  # noqa: F401
from .config import LoggerConfig

# Setup logging
logger.configure(
    handlers=[
        dict(
            sink=sys.stdout,
            format=LoggerConfig.LOG_FORMAT,
            level=LoggerConfig.LOG_LEVEL,
        ),
        dict(
            sink=LoggerConfig.LOG_FILE,
            format=LoggerConfig.LOG_FORMAT,
            level=LoggerConfig.LOG_LEVEL,
            rotation="300 MB",
        ),
    ]
)
