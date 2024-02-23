#!/usr/bin/python3
"""All states from the database hbtn_0e_0-usa"""

import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
    cities INNER JOIN states ON states.id=cities.state_id""")
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()
