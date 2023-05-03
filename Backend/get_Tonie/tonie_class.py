from dataclasses import dataclass

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    create_engine,
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()
engine = create_engine("sqlite:///Tonies.db")
Session = sessionmaker(bind=engine)


@dataclass
class Tonie(Base):
    __tablename__ = "Tonies"

    tonie_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    figure = Column(String)
    description = Column(Text)
    titlelist = relationship("Titlelist")
    runtime = Column(String, nullable=True)
    age_recommendation = Column(String, nullable=True)
    image = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


class Titlelist(Base):
    __tablename__ = "Titlelist"
    tonie = relationship("Tonie", back_populates="titlelist")

    list_id = Column(Integer, primary_key=True, autoincrement=True)
    tonie_id = Column(Integer, ForeignKey("Tonies.tonie_id"))
    title_nr = Column(Integer)
    title = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
