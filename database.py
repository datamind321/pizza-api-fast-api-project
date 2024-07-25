from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

engine = create_engine("mysql+mysqlconnector://root:uxXRGTVXGnuxAwsfNsEFEXJmRiCFmyLA@mysql.railway.internal/railway")

Base = declarative_base()

Session = sessionmaker()
