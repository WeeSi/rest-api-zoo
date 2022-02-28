from pydantic import BaseModel


class Accommodation(BaseModel):
    type: str
    Keeper: str