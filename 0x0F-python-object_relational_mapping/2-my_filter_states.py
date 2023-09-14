#!/usr/bin/python3
"""  a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name
matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    try:
        db_connect = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3])

        db_cursor = db_connect.cursor()

        db_cursor.execute(
            "SELECT * FROM states WHERE name LIKE "
            "BINARY %(name)s ORDER BY states.id ASC",
            {'name': argv[4]})

        states = db_cursor.fetchall()

        for state in states:
            print(state)

        db_cursor.close()
        db_connect.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
