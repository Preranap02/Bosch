from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Pass@123@localhost:3306/bosch"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
