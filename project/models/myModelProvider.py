# coding=utf-8
from __future__ import unicode_literals
from .MyModel import MyModel

"""Table Provider"""
class MyModelProvider(object):

    def __init__(self, session, logger=None):
        self.session = session

    def create(self, value , status):
        myModel = MyModel(value=value, status=status)
        self.session.add(myModel)
        self.session.flush()
        return myModel

    def getById(self, id):
        myModel = (
            self.session
            .query(MyModel)
            .filter_by(id=id)
            .first()
        )
        return myModel

    def getList(self):
        myModel = (
            self.session
            .query(MyModel)
            .all()
        )
        return myModel