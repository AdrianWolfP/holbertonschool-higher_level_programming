#!/usr/bin/python3
"""
SQL script that lists all states
with a name starting with N (upper N)
from the database hbtn_0e_0_usa:

"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Access database and fetch all states,
    filtered with a name starting with N (upper N)
    print results, and close database.
    """
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to mySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        password=mysql_password,
        db=database_name
    )

    # create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to select all states and fetch results
    query = "SELECT * FROM states \
        WHERE name LIKE BINARY 'N%' \
        ORDER BY states.id ASC"
    cursor.execute(query)
    results = cursor.fetchall()

    # Display the results
    for state in results:
        print(state)

    # close the cursor and database connection
    cursor.close()
    db.close()