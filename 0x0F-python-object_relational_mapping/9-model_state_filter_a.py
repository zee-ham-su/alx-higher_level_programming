#!/usr/bin/python3
"""Script to list all State objects containing
the letter 'a' from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(
            sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                               format(username, password, database),
                               pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        states = (session.query(State)
                  .filter(State.name.like('%a%'))
                  .order_by(State.id)
                  .all())

        if states:
            for state in states:
                print("{}: {}".format(state.id, state.name))
        else:
            print("Nothing")

        session.close()

    except Exception as e:
        print("Error:", e)
