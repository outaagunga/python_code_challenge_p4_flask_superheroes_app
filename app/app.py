# app.py

from flask import Flask, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from models import Hero, Power, HeroPower, hero_power_association


# Initing my app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy()
db.init_app(app)

Migrate = Migrate(app, db)
ma = Marshmallow(app)


@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'Hello World am trying it'})


# Running the server
if __name__ == "__main__":
    app.run(port=5555)
