from fastapi import APIRouter
from bson import ObjectId

from models.accommodation import Accommodation
from config.db import db

from schemas.accommodation import accoEntity, accosEntity, serializeDict, serializeList
accoRoute = APIRouter()
accoRoute.tags = ["Accommodation"]

@accoRoute.post('/acc')
async def create_acco(acc: Accommodation):
    db.get_collection('accommodation').insert_one(dict(acc))
    return serializeList(db.get_collection('accommodation').find())

@accoRoute.get('/accs')
async def find_all_acco():
    return accosEntity(db.get_collection('accommodation').find())


@accoRoute.get('/acc/{id}')
async def find_one_acco(id):
    return serializeDict(db.get_collection('accommodation').find_one({"_id": ObjectId(id)}))


@accoRoute.delete('/acc/{id}')
async def delete_one_acco(id):
    return serializeDict(db.get_collection('accommodation').find_one_and_delete({"_id": ObjectId(id)}))


@accoRoute.put('/acc/{id}')
async def update_one_acco(id, acc: Accommodation):
    db.get_collection(
        'accommodation').find_one_and_update({"_id": ObjectId(id)}, {
            "$set":dict(acc)
        })
    return serializeDict(db.get_collection('accommodation').find_one({"_id": ObjectId(id)}))