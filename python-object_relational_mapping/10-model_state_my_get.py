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

    # Define the database uri
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    # Create engine and session
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all state objects and sort by states.id
    states = session.query(State).filter(
        State.name == sys.argv[4]).first()

    # Print the result
    if states:
            print(states.id)
    else:
            print("Not found")