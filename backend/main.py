from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy import select, text
from backend.database import engine, get_db
from backend.models import Place
from backend.schemas import PlaceCreate

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/health/db")
def health_db():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"database": "connected"}

@app.post("/places")
def create_place(place: PlaceCreate, db: Session = Depends(get_db)):
    new_place = Place(name=place.name)
    db.add(new_place)
    db.commit()
    db.refresh(new_place)
    return {"id": new_place.id, "name": new_place.name}

@app.get("/places")
def list_places(db: Session = Depends(get_db)):
    places = db.scalars(select(Place)).all()
    return [{"id": p.id, "name": p.name} for p in places]