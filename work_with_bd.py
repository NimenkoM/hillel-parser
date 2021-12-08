import sqlite3

from flask import Flask, jsonify, request

app = Flask(__name__)


def cursor_create():
    connection = sqlite3.connect('chinook.db')
    return connection


@app.route("/names")
def name():
    with cursor_create() as cursor:
        query = cursor.execute("SELECT DISTINCT (FirstName) FROM customers")
        data = query.fetchall()

    return jsonify(Users=str(len(data)))


@app.route("/customers/")
def customers():
    with cursor_create() as cursor:

        conditions = []

        try:
            customer_id = int(request.args['id'])
            conditions.append(f'CustomerId = {customer_id}')
        except (ValueError, KeyError):
            pass

        country = request.args.getlist('country')
        if country:
            c = ','.join(repr(y) for y in country)
            conditions.append(f'Country IN ({c})')

        fax = {
            'is_null': 'Fax IS NULL',
            'is_not_null': 'Fax IS NOT NULL',
        }

        fax_param = fax.get(request.args.get('fax'))

        if fax_param:
            conditions.append(fax_param)

        if conditions:
            where = ' OR '.join(conditions)  # OR
            query = f'SELECT * FROM customers WHERE {where}'
        else:
            query = 'SELECT * FROM customers'

        customers = cursor.execute(query)

        results = customers.fetchall()

        return jsonify(results)


@app.route("/tracks")
def tracks():
    with cursor_create() as cursor:
        query = cursor.execute("SELECT Count(*) FROM tracks")
        data = query.fetchall()

    return jsonify(data)


@app.route("/tracks-sec")
def tracks_sec():
    with cursor_create() as cursor:
        query = cursor.execute('SELECT Name, Milliseconds/1000 FROM tracks')
        data = query.fetchall()
    return jsonify(data)


if __name__ == '__main__':
    app.run()
