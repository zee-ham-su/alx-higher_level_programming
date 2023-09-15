#!/usr/bin/python3
"""
This script retrieves all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(
            sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db_url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        cities = session.query(City).order_by(City.id).all()

        for city in cities:
            state_name = (session.query(State)
                          .filter_by(id=city.state_id).first().name)
            print("{}: ({}) {}".format(state_name, city.id, city.name))
