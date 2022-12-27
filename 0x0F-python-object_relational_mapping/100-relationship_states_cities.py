#!/usr/bin/python3
"""Create a city with a relationship with a state."""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    state = State(name="California", cities=[
        City(name="San Francisco")
    ])
    session.add(state)
    session.commit()
