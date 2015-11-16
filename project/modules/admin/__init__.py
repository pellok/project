from __future__ import unicode_literals
from . import views


def includeme(config):
    config.add_route('admin.home', '/')
    config.add_route('admin.createJson', '/createJson')
    config.add_route('admin.getjson', '/json/{id}')

    config.add_view(
        views.AdminViews, attr='home',
        route_name='admin.home',
        renderer='templates/home.mako',
    )

    config.add_view(
        views.AdminViews, attr='createJson',
        route_name='admin.createJson',
    )

    config.add_view(
        views.AdminViews, attr='getjson',
        route_name='admin.getjson',
    )
