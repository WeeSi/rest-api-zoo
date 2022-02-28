from fastapi import FastAPI
from routes.animal import animalRoute

app = FastAPI()

app.include_router(animalRoute)
