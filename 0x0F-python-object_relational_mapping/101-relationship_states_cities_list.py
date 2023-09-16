#!/usr/bin/python3
"""This script lists all State objects and their
corresponding City objects
contained in the database hbtn_0e_101_usa.
"""

from sqlalchemy.orm import relationship
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = (session.query(State)
              .outerjoin(City).order_by(State.id, City.id).all())

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
