from .api_coordinates import *
from .app import app
from mongoengine import get_connection
from importlib.metadata import version
from .settings import settings


@app.get("/")
def hello():
    return "hello world"


@app.get("/info")
def info():
    connection = get_connection()
    db_info = connection.server_info()
    paddleocr_version = version("paddleocr")
    return {
        "mongodb_version": db_info["version"],
        "paddleocr_version": paddleocr_version,
        "copy_hero_version": settings.copy_hero_version,
    }
