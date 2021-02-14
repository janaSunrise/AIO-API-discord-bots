import sys

from loguru import logger

from api import config as conf
from api.app import app


# -- Logger configuration --
logger.configure(handlers=[
    dict(sink=sys.stdout, format=conf.log_format, level=conf.log_level),
    dict(sink=conf.log_file, format=conf.log_format, level=conf.log_level, rotation="500 MB")
])
