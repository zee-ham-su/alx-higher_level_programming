#!/usr/bin/python3
"""This script creates the State "California" with
the City "San Francisco"
in the database hbtn_0e_100_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cali_State = State(name='California')
    sanfran_City = City(name='San Francisco')
    cali_State.cities.append(sanfran_City)

    session.add(cali_State)
    session.add(san_franCity)
    session.commit()
