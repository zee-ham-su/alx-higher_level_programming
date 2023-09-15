#!/usr/bin/python3
"""
This script adds the State object
`Louisiana` to the database `hbtn_0e_6_usa`.
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
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()

        print(new_state.id)
