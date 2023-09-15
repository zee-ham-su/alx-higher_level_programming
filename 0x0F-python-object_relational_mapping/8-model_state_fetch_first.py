#!/usr/bin/python3
"""Script to print the first State object from the
database hbtn_0e_6_usa.
"""

import MySQLdb
import sys
from model_state import Base, State

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(
            sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db_connect = MySQLdb.connect(
            host="localhost", user=username, passwd=password, db=database
        )

        db_cursor = db_connect.cursor()

        db_cursor.execute("SELECT * FROM states ORDER BY id ASC LIMIT 1")
        first_state = db_cursor.fetchone()

        if first_state is None:
            print("Nothing")
        else:
            state = State(id=first_state[0], name=first_state[1])
            print("{}: {}".format(state.id, state.name))

        db_cursor.close()
        db_connect.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
