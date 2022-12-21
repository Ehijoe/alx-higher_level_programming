#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa."""
import sys
import MySQLdb


def main():
    """List the states in the database."""
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2],
                         db=sys.argv[3],
                         host="localhost",
                         port=3000)
    cur = db.cursor()
    cur.execute(
        "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
    )
    states = cur.fetchall()

    for state in states:
        print(state)


if __name__ == '__main__':
    main()
