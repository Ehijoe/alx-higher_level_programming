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
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
