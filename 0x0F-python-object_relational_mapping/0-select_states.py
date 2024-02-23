#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database_name):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=hbtn_0e_0_usa
    )
    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY states.id ASC"
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
