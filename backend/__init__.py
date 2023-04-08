from flask import Flask

app = Flask(__name__)

# load configuration
app.config.from_object('config')

# import routes
from backend import routes