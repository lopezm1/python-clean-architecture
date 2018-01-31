import os
from .common.constants import INSTANCE_FOLDER_PATH

class BaseConfig(object):

   PROJECT = "app"

   # Get app root path, also can use flask.root_path.
   PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


   ADMINS = ['youremail@yourdomain.com']

   # http://flask.pocoo.org/docs/quickstart/#sessions
   SECRET_KEY = 'secret key'

class DefaultConfig(BaseConfig):

   # Statement for enabling the development environment
   TESTING = True
   DEBUG = True
   
   # Secret key for signing cookies
   SECRET_KEY = 'development key'

class TestConfig(DefaultConfig):
   """Test configuration."""
   ENV = 'test'
   TESTING = True
   DEBUG = True

def get_config(MODE):
   SWITCH = {
      'TEST'     : TestConfig,
      'DEFAULT'   : DefaultConfig
   }
   return SWITCH[MODE]