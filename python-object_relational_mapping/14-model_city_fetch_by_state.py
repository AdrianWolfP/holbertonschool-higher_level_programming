#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Database connection setup
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}',
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and print them
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = session.query(State.name).filter_by(id=city.state_id).scalar()
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    session.close()