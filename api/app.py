from fastapi import FastAPI

from api.routers import memes

# -- Define the API --
app = FastAPI()

# -- Include the routers --
app.include_router(memes.router)


# -- API endpoints --
@app.get("/")
async def root():
    return {"message": "Hello World"}
