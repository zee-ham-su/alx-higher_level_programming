#!/usr/bin/python3
"""
This script deletes State objects with names containing 'a'
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(argv[0]))
        exit(1)

    username, password, db_name = argv[1], argv[2], argv[3]

    db_url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        states_to_delete = (session.query(State)
                            .filter(State.name.like('%a%')).all())

        if states_to_delete:
            for state in states_to_delete:
                session.delete(state)
            session.commit()
