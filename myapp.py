from flask import Flask, redirect, Markup, render_template
from bs4 import BeautifulSoup       
import requests as req

myapp = Flask(__name__)
myapp.config['SECRET_KEY'] = 'secretkey'

@myapp.route('/')
def index():
    return render_template('index.html')

@myapp.route('/customer')
def customer():
    Data = 'Hello World'
    return render_template('customer.html', data = Data)
if __name__ == "__main__":
    myapp.run('localhost',9000, debug = True)