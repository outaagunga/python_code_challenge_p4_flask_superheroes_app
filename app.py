# Import required modules
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from models import Hero, Power, db, HeroPower
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

# Initialize the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

migrate = Migrate(app, db)

# Create a Marshmallow instance
ma = Marshmallow(app)

# Define Hero Schema


class HeroSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Hero

# Define Power Schema


class PowerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Power

# Home


@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Superheroes API!"

# GET /heroes


@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    hero_schema = HeroSchema(many=True)
    heroes_data = hero_schema.dump(heroes)
    return jsonify(heroes_data)

# GET /heroes/:id


@app.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    hero = Hero.query.get(hero_id)

    if not hero:
        return jsonify({'error': 'Hero not found'}), 404

    hero_schema = HeroSchema()
    hero_data = hero_schema.dump(hero)
    return jsonify(hero_data)

# GET /powers


@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    power_schema = PowerSchema(many=True)
    powers_data = power_schema.dump(powers)
    return jsonify(powers_data)

# GET /powers/:id


@app.route('/powers/<int:power_id>', methods=['GET'])
def get_power(power_id):
    power = Power.query.get(power_id)

    if not power:
        return jsonify({'error': 'Power not found'}), 404

    power_schema = PowerSchema()
    power_data = power_schema.dump(power)
    return jsonify(power_data)

# PATCH /powers/:id


@app.route('/powers/<int:power_id>', methods=['PATCH'])
def update_power(power_id):
    power = Power.query.get(power_id)

    if not power:
        return jsonify({'error': 'Power not found'}), 404

    data = request.json

    if 'description' not in data or len(data['description']) < 20:
        return jsonify({'errors': ['Description must be at least 20 characters long']}), 400

    power.description = data['description']
    db.session.commit()

    power_schema = PowerSchema()
    power_data = power_schema.dump(power)
    return jsonify(power_data)

# POST /hero_powers


@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.json

    # Check if the required fields are in the request
    if 'power_id' not in data or 'hero_id' not in data or 'strength' not in data:
        return jsonify({'errors': ['Missing required fields']}), 400

    power = Power.query.get(data['power_id'])
    hero = Hero.query.get(data['hero_id'])

    # Check if the power and hero exist
    if not power or not hero:
        return jsonify({'errors': ['Power or Hero not found']}), 404

    # Validate the strength field
    if data['strength'] not in ['Strong', 'Weak', 'Average']:
        return jsonify({'errors': ['Invalid strength value']}), 400

    hero_power = HeroPower(hero=hero, power=power, strength=data['strength'])
    db.session.add(hero_power)
    db.session.commit()

    hero_schema = HeroSchema()
    hero_data = hero_schema.dump(hero)
    return jsonify(hero_data), 201


# Running the server
if __name__ == "__main__":
    app.run(debug=True)
