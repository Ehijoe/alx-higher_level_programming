#!/usr/bin/python3
"""Remove all states with 'a' in them."""
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        for city in session.query(City).order_by(City.id).\
                filter(City.state_id == state.id).all():
            print(f"{state.name}: ({city.id}) {city.name}")
    Base.metadata.create_all(engine)
