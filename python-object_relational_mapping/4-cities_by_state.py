#!/usr/bin/python3
"""
script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa where
name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Access database and fetch all states,
    tests with user input as params,
    print results, and close database.
    """
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    # state_name = sys.argv[4]

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

    # Create the query and prepare to have user input
    query = "SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states \
            ON cities.state_id = states.id \
            ORDER by cities.id ASC"

    # Execute the query and fetch results
    cursor.execute(query)
    results = cursor.fetchall()

    # Display the results
    for city in results:
        print(city)

    # close the cursor and database connection
    cursor.close()
    db.close()