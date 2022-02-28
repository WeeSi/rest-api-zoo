def visitEntity(item) -> dict:

    return {
        "_id": str(item['_id']),
        "type": str(item['type']),
        "Name": str(item['Name']),
    }


def visitsEntity(entity) -> list:
    return [visitEntity(item) for item in entity]


def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
