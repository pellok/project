import os
import sys
import transaction
import getpass

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import setup_database_setting
from ..models import models
from ..models.models import MyModel


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

"""
getpass_func=getpass : Portable password input
https://docs.python.org/2/library/getpass.html
input_func=raw_input
https://docs.python.org/2/library/functions.html#raw%5Finput

"""
def main(argv=sys.argv, input_func=raw_input, getpass_func=getpass.getpass):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    """Setup DB engine and Sesstion"""
    settings = setup_database_setting(**settings)
    engine = settings['engine']
    session = settings['session']
    
    """Init DB Table"""
    models.Base.metadata.create_all(engine, checkfirst=True)
    

    """Init DB Data"""
    with transaction.manager:
        model = MyModel(name='one', value=1)
        session.add(model)
