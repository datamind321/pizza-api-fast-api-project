from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

engine = create_engine("mysql+mysqlconnector://root:12345678@localhost/pizza")

Base = declarative_base()

Session = sessionmaker()