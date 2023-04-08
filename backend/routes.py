from backend import app
from flask import render_template

@app.route('/')
def index():
    return render_template('home.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error=error), 404