#!/usr/bin/python3
"""
Module lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    # get the command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Define the database uri
    db_uri = f"mysql+mysqldb://{mysql_username}: \
    {mysql_password}@localhost:3306/{database_name}"

    # Create engine and session
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all state objects and sort by states.id
    states = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states:
        print(f"{states.id}: {states.name}")