from pydantic import BaseModel


class FermeEtLoenie(BaseModel):
    type: str
    color: str
    taille: str
    sexe: str
