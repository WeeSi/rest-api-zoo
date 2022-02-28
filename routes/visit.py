from fastapi import APIRouter
from bson import ObjectId

from models.visit import Visit
from config.db import db

from schemas.visit import visitsEntity, visitEntity, serializeDict, serializeList
visitRoute = APIRouter()

@visitRoute.post('/visit')
async def create_visit(visit: Visit):
    db.get_collection('visit').insert_one(dict(visit))
    return serializeList(db.get_collection('visit').find())

@visitRoute.get('/visits')
async def find_all_visit():
    return visitsEntity(db.get_collection('visit').find())


@visitRoute.get('/visit/{id}')
async def find_one_visit(id):
    return serializeDict(db.get_collection('visit').find_one({"_id": ObjectId(id)}))


@visitRoute.delete('/visit/{id}')
async def delete_one_visit(id):
    return serializeDict(db.get_collection('visit').find_one_and_delete({"_id": ObjectId(id)}))


@visitRoute.put('/visit/{id}')
async def update_one_visit(id, visit: Visit):
    db.get_collection(
        'visit').find_one_and_update({"_id": ObjectId(id)}, {
            "$set":dict(visit)
        })
    return serializeDict(db.get_collection('visit').find_one({"_id": ObjectId(id)}))