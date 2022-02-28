from pydantic import BaseModel


class BaieDesOtaries(BaseModel):
    type: str
    color: str
    taille: str
    sexe: str
