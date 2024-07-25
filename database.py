from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

engine = create_engine("postgresql://pizza_g6pm_user:klhvCHdLv22SXpKphttLFSQXaqwk6lno@5432/pizza_g6pm",connect_args={"check_same_thread": False})

Base = declarative_base()

Session = sessionmaker()
