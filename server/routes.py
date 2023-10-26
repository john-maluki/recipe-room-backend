from . import app


@app.get("/")
async def home():
    return {"message": "it is working"}
