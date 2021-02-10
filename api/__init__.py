import sys

from loguru import logger

from api.app import app

# -- Logger configuration --
log_file = "logs/server.log"
log_level = "INFO"
log_format = "<green>{time:YYYY-MM-DD hh:mm:ss}</green> | <level>{level: <8}</level> | " \
             "<cyan>{name: <18}</cyan> | <level>{message}</level>"

logger.configure(handlers=[
    dict(sink=sys.stdout, format=log_format, level=log_level),
    dict(sink=log_file, format=log_format, level=log_level, rotation="500 MB")
])
