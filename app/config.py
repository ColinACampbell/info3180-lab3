import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'localhost')
    MAIL_PORT = os.environ.get('MAIL_PORT', '25')
    MAIL_USERNAME = os.environ.get('91f2845ed29e2f')
    MAIL_PASSWORD = os.environ.get('70c3aca93dfad5')