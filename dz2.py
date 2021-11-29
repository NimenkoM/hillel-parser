import json
import random
import string

import flask
from faker import Faker
from flask import Flask,request

fake = Faker()
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def index():
    return  "<h1>Hello world</h1>"

@app.route('/email_generator', methods = ['POST','GET'])
def email_generator():
    result = []
    n = 100
    for i in range(n):
        name = fake.name()
        email = fake.email()
        result.append(f'\n{name} {email}')


    return ''.join(result)

@app.route('/test')
def test():
    with open('hw.csv','r') as f:
        return ''.join(f)








if __name__ == '__main__':
    app.run(port=5000)
