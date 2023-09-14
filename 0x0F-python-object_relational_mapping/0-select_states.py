#!/usr/bin/python3
""" a script that lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys


if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(argv[0]))
        exit(1)

    try:

        db_connect = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])


        db_cursor = db_connect.cursor()

        db_cursor.execute("SELECT * FROM states")

        rows_selected = db_cursor.fetchall()

        for row in rows_selected:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        if 'db_cursor' in locals() and db_cursor is not None:
            db_cursor.close()

        if 'db_connect' in locals() and db_connect is not None:
            db_connect.close()
