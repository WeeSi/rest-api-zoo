from pydantic import BaseModel


class EspaceGriffesEtCrocs(BaseModel):
    type: str
    color: str
    taille: str
    sexe: str
