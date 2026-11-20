from pydantic import BaseModel


class PlaceCreate(BaseModel):
    name: str