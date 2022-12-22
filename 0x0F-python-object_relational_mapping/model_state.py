#!/usr/bin/python3
"""Model for the States."""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sys import argv


engine = create_engine(
    f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[4]}"
)
Base = declarative_base()


class State(Base):
    """Model for a state."""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
