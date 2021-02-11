from fastapi import FastAPI

from api.routers import memes
from api.routers import funny

# -- Define the API --
app = FastAPI()

# -- Include the routers --
app.include_router(memes.router)
app.include_router(funny.router)


# -- API endpoints --
@app.get("/")
async def root():
    return {"message": "Hello World"}
