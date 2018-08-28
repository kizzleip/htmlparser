import os
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TaskTable(Base):
    __tablename__ = 'zhuge_dichan'
    title = Column(String)
    region = Column(String)
    categary = Column(String)
    floor_area = Column(String)
    orientation = Column(String)
    renovation = Column(String)
    elevator = Column(String)
    floor = Column(String)
    years = Column(String)
    price = Column(String)
    listing_time = Column(String)
    metro = Column(String)
    url = Column(String)
    id = Column(Integer, primary_key=True)
