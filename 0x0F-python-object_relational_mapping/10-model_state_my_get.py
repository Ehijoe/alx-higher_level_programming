#!/usr/bin/python3
"""Search for a state in the database."""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(
        State.name == argv[4]
    ).order_by(State.id).first()
    if state is None:
        print("Not found")
    else:
        print(f"{state.id}")
    Base.metadata.create_all(engine)
