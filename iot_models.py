#!/usr/bin/env python

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

Base = declarative_base()

class practice1(Base):
    __tablename__ = 'practice1'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    sensorid = Column(String(10), nullable=False)
    temperature = Column(String(5))
    humidity = Column(String(5))
    dt = Column(DateTime, default=datetime.now)

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from settings import MYSQL_URI
    engine = create_engine(MYSQL_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
