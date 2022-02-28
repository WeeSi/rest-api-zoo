from pydantic import BaseModel


class PlaineAfricaine(BaseModel):
    type: str
    color: str
    taille: str
    sexe: str
