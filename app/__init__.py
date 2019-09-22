from flask import Flask
from config import Config
from dbconnect import connection
from jinja2 import Environment, select_autoescape
env = Environment(autoescape=select_autoescape(
    enabled_extensions=('html', 'xml', 'js', 'min.js'),
    default_for_string=True,
))


app = Flask(__name__)
app.config.from_object(Config)





from app import routes
