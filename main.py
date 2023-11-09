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
