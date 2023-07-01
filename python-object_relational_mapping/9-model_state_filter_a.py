#!/usr/bin/python3
"""
Module lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
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
        argv[1], argv[2], argv[3])
    # Create engine and session
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all state objects and sort by states.id
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")