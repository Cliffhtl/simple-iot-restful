
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from settings import MYSQL_URI

Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=create_engine(MYSQL_URI))
session = scoped_session(Session)

