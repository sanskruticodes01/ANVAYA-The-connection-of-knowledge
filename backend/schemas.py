from pydantic import BaseModel


class PlaceCreate(BaseModel):
    name: str

class EventCreate(BaseModel):
    title: str
    description: str | None = None
    year: int | None = None
    place_id: int | None = None    