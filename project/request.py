from __future__ import unicode_literals
from pyramid.decorator import reify
from pyramid.request import Request

class WebRequest(Request):
    @reify
    def db_session(self):
        """Session object for database operations
        """
        settings = self.registry.settings
        return settings['session']
