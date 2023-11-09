import os
from uvicorn import run

from server import app
from server.routes import (
    recipes,
    users,
    index,
    auths,
    comments,
    favourite_recipes,
    ratings,
)

app.include_router(index.router)
app.include_router(auths.router)
app.include_router(users.router)
app.include_router(recipes.router)
app.include_router(comments.router)
app.include_router(favourite_recipes.router)
app.include_router(ratings.router)

if __name__ == "__main__":
    host = "0.0.0.0"
    port = int(os.environ.get("PORT", 8000))
    run("main:app", host=host, port=port)
