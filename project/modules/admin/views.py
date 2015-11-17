#code = utf-8
from __future__ import unicode_literals
from project.models.myModelProvider import MyModelProvider


class AdminViews(object):
    def __init__(self, request):
        self.request = request

    def home(self):
        request = self.request
        myModelProvider = MyModelProvider(request.db_session)
        modelLists = myModelProvider.getList()
        # lists = [{'id':'1','value':'{"abc"="123"}'},{'id':'2','value':'{"xyz"="456"}'}]
        lists=[]
        for model in modelLists:
            list={}
            list['id'] = model.id
            list['value'] = model.value
            lists.append(list)

        return dict(title='Json Service', lists=lists)

    def createJson(self):
        request = self.request
        value = request.params['value']
        print value

        myModelProvider = MyModelProvider(request.db_session)
        myModelProvider.create(value, 10)

        modelLists = myModelProvider.getList()
        # lists = [{'id':'1','value':'{"abc"="123"}'},{'id':'2','value':'{"xyz"="456"}'}]
        lists=[]
        for model in modelLists:
            list={}
            list['id'] = model.id
            list['value'] = model.value
            lists.append(list)
        return dict(title='Json Service', lists=lists)

    def getjson(self):
        request = self.request
        myModelProvider = MyModelProvider(request.db_session)
        id = request.matchdict['id']
        json = myModelProvider.getById(id)
        print json
        return {}
