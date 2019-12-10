from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_cors import CORS
import logging
from db.db import *
from db.db_functions import *

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config['FLASK_SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db.app = app
db.init_app(app)

logging.basicConfig(level=logging.DEBUG)


@app.route('/', methods=["get", "post"])
def index():
    flash("Welcome home !! " , "info")
    return render_template('index.html')


@app.route('/calculate', methods=['post'])
def calculate():
    try:
        app.logger.info('processing request')
        app.logger.info(request)
        app.logger.debug(request.get_json())
        items = request.get_json()
        amount = calculate_amount(items)
        app.logger.debug("amount is "+ str(amount))
        app.logger.debug(type(int) is type(amount))
        app.logger.debug(type(amount))
        result = { "url": url_for('statement') + "?amount=" + str(amount)}
        return jsonify(result)
    except Exception as e:
        flash("Error occurred: " + str(e), "danger")
        return render_template('errors/404.html'), 400


@app.route('/statement')
def statement():
    flash("Please find your bill ", "info")
    return render_template('statement.html', amount=request.args.get('amount'), currency=app.config['CURRENCY'])


def calculate_amount(items):
    bookTypeCharges = get_book_types_and_charges()
    amount = 0
    for item in items:
        app.logger.debug(item["bookQuantity"])
        app.logger.debug(item["dayDuration"])
        app.logger.debug(item["bookType"])
        app.logger.debug(bookTypeCharges[item["bookType"]])
        amount += ((item["bookQuantity"] * item["dayDuration"]) * bookTypeCharges[item["bookType"]])
    app.logger.debug(amount)
    return amount


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5020, debug=app.debug)