from sqlalchemy import engine_from_config
from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy.orm import (scoped_session, sessionmaker,)
from zope.sqlalchemy import ZopeTransactionExtension


"""Setup database engine and  session"""
def setup_database_setting(**settings):
	if 'engine' not in settings:
		settings['engine'] = (
			engine_from_config(settings, 'sqlalchemy.')
		)
	if 'session' not in settings:
		settings['session'] =scoped_session(
			sessionmaker(
				extension=ZopeTransactionExtension(keep_session=True),
				bind=settings['engine']
			)
		)
	return settings



