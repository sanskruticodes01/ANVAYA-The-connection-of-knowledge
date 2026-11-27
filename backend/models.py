
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    place_id: Mapped[int | None] = mapped_column(ForeignKey("places.id"))
    description: Mapped[str | None] = mapped_column(Text())
    year: Mapped[int | None] = mapped_column()
    place : Mapped["Place"] = relationship()
    
class Place(Base):
    __tablename__ = "places"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))

class Person(Base):
    __tablename__ = "people"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))

class EventPerson(Base):
    __tablename__ = "event_people"

    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), primary_key=True)
    person_id: Mapped[int] = mapped_column(ForeignKey("people.id"), primary_key=True)
