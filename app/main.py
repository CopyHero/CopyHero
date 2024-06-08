# coding:utf-8

from .settings import logger
from .api import *
from .app import app

logger.info("App is running")
main_app = app
