from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()


class Hero(db.Model):
    __tablename__ = 'hero'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    super_name = db.Column(db.String(255), nullable=False)

    hero_powers = db.relationship('HeroPower', back_populates='hero')

    def __init__(self, name, super_name):
        self.name = name
        self.super_name = super_name


class Power(db.Model):
    __tablename__ = 'power'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    power_heroes = db.relationship('HeroPower', back_populates='power')

    @validates('description')
    def validate_description(self, key, value):
        if len(value) < 20:
            raise ValueError(
                "Description must be at least 20 characters long.")
        return value

    def __init__(self, name, description):
        self.name = name
        self.description = description


class HeroPower(db.Model):
    __tablename__ = 'hero_power'
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), primary_key=True)
    power_id = db.Column(db.Integer, db.ForeignKey(
        'power.id'), primary_key=True)
    strength = db.Column(db.String(255), nullable=False)

    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='power_heroes')

    @validates('strength')
    def validate_strength(self, key, value):
        if value not in ['Strong', 'Weak', 'Average']:
            raise ValueError(
                "Strength must be 'Strong', 'Weak', or 'Average'.")
        return value

    def __init__(self, hero, power, strength):
        self.hero = hero
        self.power = power
        self.strength = strength
