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
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
        {"name": "Janet Van Dyne", "super_name": "The Wasp"},
        {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
        {"name": "Carol Danvers", "super_name": "Captain Marvel"},
        {"name": "Jean Grey", "super_name": "Dark Phoenix"},
        {"name": "Ororo Munroe", "super_name": "Storm"},
        {"name": "Kitty Pryde", "super_name": "Shadowcat"},
        {"name": "Elektra Natchios", "super_name": "Elektra"}
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


if __name__ == "__main__":
    seed()
    print("🦸‍♀️ Done seeding!")
