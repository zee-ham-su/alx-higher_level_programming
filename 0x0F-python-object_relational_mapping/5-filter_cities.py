#!/usr/bin/python3
"""
This script lists all cities of a specified state
from the database `hbtn_0e_4_usa`.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    try:
        db_connect = MySQLdb.connect(
            host="localhost", user=sys.argv[1], port=3306,
            passwd=sys.argv[2], db=sys.argv[3])

        db_cursor = db_connect.cursor()

        db_cursor.execute(
            "SELECT cities.name FROM cities "
            "INNER JOIN states ON states.id = cities.state_id "
            "WHERE states.name = %s", (sys.argv[4],)
        )

        states = db_cursor.fetchall()

        for state in states:
            print(state[0])

        db_cursor.close()
        db_connect.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
