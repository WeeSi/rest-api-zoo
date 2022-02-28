def animalEntity(item) -> dict:

    if hasattr(item, 'sexe'):
        print('has')
    else:
        item["sexe"] = ""

    if hasattr(item, 'taille'):
        print('has')
    else:
        item["taille"] = ""

    return {
        "_id": str(item['_id']),
        "type": str(item['type']),
        "color": str(item['color']),
        "sexe": str(item['sexe']),
        "taille": str(item['taille'])
    }


def animalsEntity(entity) -> list:
    return [animalEntity(item) for item in entity]


def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
