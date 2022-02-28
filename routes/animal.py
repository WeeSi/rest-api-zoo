from fastapi import APIRouter
from bson import ObjectId

from models.baie_des_otaries import BaieDesOtaries
from config.db import db

from schemas.animal import animalEntity, animalsEntity, serializeDict, serializeList
animalRoute = APIRouter()
animalRoute.tags = ["Animal"]

@animalRoute.post('/otarie')
async def create_otarie(otarie: BaieDesOtaries):
    db.get_collection('baie-des-otaries').insert_one(dict(otarie))
    return serializeList(db.get_collection('baie-des-otaries').find())

@animalRoute.get('/otaries')
async def find_all_otaries():
    return animalsEntity(db.get_collection('baie-des-otaries').find())


@animalRoute.get('/otarie/{id}')
async def find_one_otarie(id):
    return serializeDict(db.get_collection('baie-des-otaries').find_one({"_id": ObjectId(id)}))


@animalRoute.delete('/otarie/{id}')
async def delete_one_otarie(id):
    return serializeDict(db.get_collection('baie-des-otaries').find_one_and_delete({"_id": ObjectId(id)}))


@animalRoute.put('/otarie/{id}')
async def update_one_otarie(id, otarie: BaieDesOtaries):
    db.get_collection(
        'baie-des-otaries').find_one_and_update({"_id": ObjectId(id)}, {
            "$set":dict(otarie)
        })
    return serializeDict(db.get_collection('baie-des-otaries').find_one({"_id": ObjectId(id)}))