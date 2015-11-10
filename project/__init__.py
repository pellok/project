from pyramid.config import Configurator
from pyramid_beaker import session_factory_from_settings
from .models import setup_database_setting



def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    #setup db
    settings = setup_database_setting(**settings)
    session_factory = session_factory_from_settings(settings)
    config = Configurator(settings=settings,
                          session_factory=session_factory,
                                            )
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
