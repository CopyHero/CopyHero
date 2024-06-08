from .api_coordinates import *
from .app import app


@app.get("/")
def hello():
    return "hello world"
