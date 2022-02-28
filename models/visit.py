from pydantic import BaseModel


class Visit(BaseModel):
    type: str
    Name: str
