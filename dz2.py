import csv
import requests
import flask


from faker import Faker
from flask import Flask, request,jsonify

fake = Faker()
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/')
def index():
    return "<h1>Hello world</h1>"


def requirements_funcion():
    with open('requirements.txt','r') as r:
        for i in r:
            yield ''.join(map(str.strip, i))
@app.route('/requirements')
def requirements():
    return '<br>'.join(requirements_funcion())


@app.route('/email_generator', methods=['POST', 'GET'])
def email_generator():
    result = []
    n = int(request.args.get('count') or 100)

    for i in range(n):
        name = fake.name()
        email = fake.email()
        result.append({
            "name":f'{name}',
            "email":f"{email}"
        })

    return flask.jsonify(result)


FILENAME = 'hw.csv'


def read_csv():
    with open('hw.csv') as file:
        for row in csv.reader(file, delimiter=','):
            if not row:
                continue

            yield ' - '.join(map(str.strip, row))


@app.route("/weight_and_height")
def csv_content():
    return '<br>'.join(read_csv())

@app.route('/space')
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    result = r.json()
    return str(result['number'])


if __name__ == '__main__':
    app.run(port=5000)
