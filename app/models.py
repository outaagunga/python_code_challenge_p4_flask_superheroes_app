# Models.py

from flask_sqlalchemy import SQLAlchemy
from app import db


# This is the association table
hero_power_association = db.Table(
    'hero_power_association',
    db.Column('hero_id', db.Integer, db.ForeignKey(
        'heroes.id'), primary_key=True),
    db.Column('power_id', db.Integer, db.ForeignKey(
        'powers.id'), primary_key=True),
    db.Column('strength', db.String(20), nullable=False)
)

# This is the Hero Model


class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    powers = db.relationship(
        'HeroPower', secondary=hero_power_association, back_populates='heroes')

# This is  validation
    @db.validates('description')
    def validate_description(self, key, description):
        if len(description) < 20:
            raise ValueError(
                "Description must be at least 20 characters long.")
        return description

    def __str__(self):
        return self.name

# This is power model


class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    heroes = db.relationship(
        'Hero', secondary=hero_power_association, back_populates='powers')

# Validation

    @db.validates('description')
    def validate_description(self, key, description):
        if len(description) < 20:
            raise ValueError(
                "Description must be at least 20 characters long.")
        return description

    def __str__(self):
        return self.name

# This is power model


class HeroPower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey(
        'powers.id'), nullable=False)
    strength = db.Column(db.String(20), nullable=False)

    hero = db.relationship('Hero', back_populates='powers')
    power = db.relationship('Power', back_populates='heroes')
