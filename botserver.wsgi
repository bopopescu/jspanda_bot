import os
import sys
sys.path.insert(0,'/var/www/jspanda_bot')
from appserver import app as application
application.secret_key = os.environ.get('SECRET_KEY')