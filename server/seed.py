#!/usr/bin/env python3
# server/seed.py

from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():

    fake = Faker()

    # Clear out existing pets from the database
    Pet.query.delete()

    # Create an empty list to store pet objects
    pets = []

    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    for _ in range(10):
        pet = Pet(name=fake.first_name(), species=rc(species))
        pets.append(pet)

    # Add all pet objects to the session and commit them to the database
    db.session.add_all(pets)
    db.session.commit()
