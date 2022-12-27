#!/usr/bin/python3
"""List all the cities and their corresponding states."""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from sys import argv


if __name__ == '__main__':
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(City)\
            .options(joinedload(City.state)).\
            order_by(City.id).all():
        print(f"{city.id}: {city.name} -> {city.state.name}")
    Base.metadata.create_all(engine)
