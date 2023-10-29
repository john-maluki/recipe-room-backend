from fastapi import FastAPI


app = FastAPI()

from . import routes
from . import database
from . import models
