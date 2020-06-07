"""Script to seed database."""

import os
import json
from random import choice, randint

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

# Load restaurant data from JSON file
with open('data/restaurants.json') as f:
    restaurant_data = json.loads(f.read())

# Create restaurants, store them in list so we can use them
# to create fake restaurant lists
restaurants_in_db = []
for restaurant in restaurant_data['businesses']:
    name, display_address, display_phone, transactions, url, image_url = \
                                    (restaurant['name'],
                                    restaurant['location']['display_address'],
                                    restaurant['display_phone'],
                                    restaurant['transactions'],
                                    restaurant['url'],
                                    restaurant['image_url'])


    db_restaurant = crud.get_restaurant(name,
                                 display_address,
                                 display_phone,
                                 transactions,
                                 url,
                                 image_url)
    restaurants_in_db.append(db_restaurant)

# Create 10 users; each user will make 10 ratings
for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    user = crud.create_user(email, password)

    for _ in range(10):
        random_restaurant = choice(restaurants_in_db)
        score = randint(1, 5)

        crud.create_rating(user, random_movie, score)
