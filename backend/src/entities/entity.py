# coding=utf-8
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


print("hello")

DB_URL = 'localhost:5432'
DB_NAME = 'exam'
DB_USER = 'root'
DB_PASS = 'SQLpa$$123'

engine = create_engine(f'mysql://{DB_USER}:{DB_PASS}@{DB_URL}/{DB_NAME}')
Session = sessionmaker(bind = engine)

Base = declarative_base()

#Represents an entity
class Entity():

    id = Column(Integer, primary_key = True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String(255))

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
