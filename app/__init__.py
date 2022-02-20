from flask import Flask
from flask_mail import Mail
from .config import Config

app = Flask(__name__)

app.config.from_object(Config)

# TODO : Remove this for later
app.config['SESSION_TYPE'] = 'filesystem'

mail = Mail(app)
from app import views