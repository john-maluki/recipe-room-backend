from fastapi import FastAPI
from server.database import engine, BaseModel


app = FastAPI()

from . import routes
from . import database
from . import models

BaseModel.metadata.create_all(bind=engine)
