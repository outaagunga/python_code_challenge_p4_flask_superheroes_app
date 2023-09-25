from app import app, db
from models import Power, Hero, HeroPower
import random

# Seed powers


def seed_powers():
    powers_data = [
        {"name": "super strength",
            "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses",
            "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
    ]

    for data in powers_data:
        power = Power(**data)
        db.session.add(power)

# Seed heroes


def seed_heroes():
    heroes_data = [
        {"name": "Kamala Khan"},
        {"name": "Doreen Green"},
        {"name": "Gwen Stacy"},
        {"name": "Janet Van Dyne"},
        {"name": "Wanda Maximoff"},
        {"name": "Carol Danvers"},
        {"name": "Jean Grey"},
        {"name": "Ororo Munroe"},
        {"name": "Kitty Pryde"},
        {"name": "Elektra Natchios"}
    ]

    for data in heroes_data:
        hero = Hero(**data)
        db.session.add(hero)

# Seed hero powers


def seed_hero_powers():
    strengths = ["Strong", "Weak", "Average"]
    heroes = Hero.query.all()
    powers = Power.query.all()

    for hero in heroes:
        num_powers = random.randint(1, 3)
        selected_powers = random.sample(powers, num_powers)

        for power in selected_powers:
            strength = random.choice(strengths)
            hero_power = HeroPower(hero=hero, power=power, strength=strength)
            db.session.add(hero_power)

# Main seeding function


def seed():
    with app.app_context():
        seed_powers()
        seed_heroes()
        seed_hero_powers()
        db.session.commit()
        print("🦸‍♀️ Done seeding!")


if __name__ == "__main__":
    seed()
