from . import views

def includeme(config):
	config.add_route('admin.home', '/')

	config.add_view(
		views.AdminViews, attr='home',
		route_name='admin.home',
		renderer='templates/home.mako',
	)
