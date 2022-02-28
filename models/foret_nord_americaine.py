from pydantic import BaseModel


class ForetNordAmericaine(BaseModel):
    type: str
    color: str
    taille: str
    sexe: str
