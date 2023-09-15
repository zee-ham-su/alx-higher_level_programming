#!/usr/bin/python3
"""
This script changes the name of a State object
in the database `hbtn_0e_6_usa`.
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
        state_to_update = session.query(State).filter_by(id=2).first()

        if state_to_update:
            state_to_update.name = "New Mexico"
            session.commit()
        else:
            print("State with id 2 not found.")
