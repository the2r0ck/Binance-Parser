import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers.root import router as RootRouter


DIRNAME = os.path.dirname(os.path.realpath(__file__))


app = FastAPI()

app.include_router(RootRouter)

app.mount("/static", StaticFiles(directory=f"{DIRNAME}/static"), name="static")
