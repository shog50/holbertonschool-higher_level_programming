#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.

Usage:
    ./0-select_states.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
import sys


def main():
    """Main function to connect to MySQL and fetch states sorted by id."""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server on localhost:3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()

