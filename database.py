from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

engine = create_engine("postgresql://pizza_g6pm_user:klhvCHdLv22SXpKphttLFSQXaqwk6lno@dpg-cqh31k2ju9rs73ef9okg-a/pizza_g6pm")

Base = declarative_base()

Session = sessionmaker()
