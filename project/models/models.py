from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Index, Integer, Text, )

Base = declarative_base()

"""Table MyModel"""
class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)