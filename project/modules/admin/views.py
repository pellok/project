from __future__ import unicode_literals


class AdminViews(object):

    def __init__(self, context, request, logger=None):

        self.request = request
        self.context = context
        self.request.response.headerlist.extend(
            (
                (str('Access-Control-Allow-Origin'), str('*')),
                (str('Content-Type'), str('application/json'))
            )
        )
        self.request.response.charset = str('utf8')

    def home(self):

        return dict()

    def createJson(self):
        
        return dict()

    def getjson(self):
        
        return dict()
