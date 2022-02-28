def accoEntity(item) -> dict:
    return {
        "_id": str(item['_id']),
        "type": str(item['type']),
        "Keeper": str(item['Keeper']),
    }


def accosEntity(entity) -> list:
    return [accoEntity(item) for item in entity]


def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
