#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.

Usage:
    ./0-select_states.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
import sys


def main():
    """Connect to MySQL and print states sorted by id."""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
