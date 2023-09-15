#!/usr/bin/python3
"""Script to list all State objects containing
the letter 'a' from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                               format(username, password, database),
                               pool_pre_ping=True)

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        states = (session.query(State)
                  .filter(State.name.like('%a%'))          

        if states is not None:
            for state in states:
                print("{}: {}".format(state.id, state.name))
        else:
            print("Nothing")

        session.close()

    except Exception as e:
            print("Error:", e)
