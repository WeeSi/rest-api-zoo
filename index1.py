from fastapi import FastAPI
from routes.animal import animalRoute
from routes.accommodation import accoRoute
from routes.visit import visitRoute

app = FastAPI()

app.include_router(animalRoute)
app.include_router(accoRoute)
app.include_router(visitRoute)
