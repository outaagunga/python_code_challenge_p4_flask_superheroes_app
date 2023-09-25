from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Hero model


class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Define the many-to-many relationship between Hero and Power through HeroPower
    hero_powers = db.relationship(
        'HeroPower', back_populates='hero', cascade='all, delete-orphan')

    def __init__(self, name):
        self.name = name

# Power model


class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    # Define the many-to-many relationship between Power and Hero through HeroPower
    hero_powers = db.relationship(
        'HeroPower', back_populates='power', cascade='all, delete-orphan')

    def __init__(self, name, description):
        self.name = name
        self.description = description

# HeroPower model (association table for many-to-many relationship)


class HeroPower(db.Model):
    __tablename__ = 'hero_power'

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey(
        'powers.id'), nullable=False)
    strength = db.Column(db.String(20), nullable=False)

    # Define relationships to Hero and Power
    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    def __init__(self, hero, power, strength):
        self.hero = hero
        self.power = power
        self.strength = strength
