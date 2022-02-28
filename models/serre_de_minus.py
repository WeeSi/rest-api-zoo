from pydantic import BaseModel


class SerreDeMinus(BaseModel):
    type: str
    color: str
    taille: str
    sexe: str
