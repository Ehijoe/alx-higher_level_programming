#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa."""
from sys import argv
import MySQLdb


def main():
    """List the states in the database."""
    db = MySQLdb.connect(user=argv[1],
                         password=argv[2],
                         db=argv[3],
                         host="localhost",
                         port=3306)
    cur = db.cursor()
    cur.execute(
        """
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON state_id = states.id
ORDER BY id ASC;
"""
    )
    states = cur.fetchall()

    for state in states:
        print(state)

    db.close()


if __name__ == '__main__':
    main()
