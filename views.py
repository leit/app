__author__ = 'root'
from app import app

@app.route('/Hello')
#@app.route('/index')
def hello1():
    return "Hello,World1"
