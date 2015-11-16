# coding=utf-8
from __future__ import unicode_literals
from .models import MyModel

"""Table Provider"""
class MyModelProvider(object):

	def __init__(self, session):
        self.session = session

    def create(self, name, value):
        myModel = MyModel(name=name, value=value)
        self.session.add(myModel)
        self.session.flush()
        return user

    def getById(self, id):
        myModel = (
            self.session
            .query(MyModel)
            .filter_by(id=id)
            .first()
        )
        return myModel