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
SELECT name FROM cities
WHERE state_id =
(SELECT id FROM states WHERE name = %s)
ORDER BY id ASC;
""",
        (argv[4],)
    )
    cities = cur.fetchall()

    print(", ".join([city[0] for city in cities]))

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
