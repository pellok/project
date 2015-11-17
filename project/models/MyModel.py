from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Index, Integer, Text, )

Base = declarative_base()

"""Table MyModel"""


class MyModel(Base):
    __tablename__ = 't_json'
    id = Column(Integer, primary_key=True)
    value = Column(Text)
    status = Column(Integer)

Index('my_index')
