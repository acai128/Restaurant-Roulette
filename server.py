from flask import (Flask, jsonify, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud 

from jinja2 import StrictUndefined 

from model import connect_to_db, Restaurant
import os
import requests 
from pprint import pformat
import json

from random import randint
import random 

app = Flask(__name__)
app.secret_key = 'SECRET!'
app.jinja_env.undefined = StrictUndefined


# API_KEY = os.environ['YELP_KEY']

API_KEY = os.environ.get('YELP_KEY', None)

@app.route('/')
def homepage():
    """Show the homepage."""

    return render_template("index.html")


@app.route('/restaurant_result', methods = ['GET'])
def get_restaurants(): 
    """Show a random restuarnt result"""
   

    location = request.args['location']
    # print(location)
    session['location'] = location
    # print(session)


    url = 'https://api.yelp.com/v3/businesses/search'

    api_key = API_KEY
    headers = {'Authorization': 'Bearer %s' % api_key}
     
    params = {'term':'restaurant',
            'location': location,
            'limit': 50}
 
     
    req = requests.get(url, params=params, headers=headers)
     
    data = req.json()
    print(data) 

    business_list = data['businesses']
    business= random.choice(business_list)

    name = business['name']
    image = business['image_url']
    rating = business['rating']
    address = ' '.join(business['location']['display_address'])
    url = business['url']
    phone = business['display_phone']
    restaurant_id = business['id']

    return render_template('restaurant_result.html', pformat=pformat, 
                            data=business, name=name, image=image, 
                            rating=rating, address=address, url=url, 
                            restaurant_id=restaurant_id,
                            phone=phone)

@app.route('/new_result', methods = ['GET'])
def get_new_restaurants(): 
    """Show a new random restuarnt result after pressing get new result 
    button"""
   
    location = session['location']

    # print(location)

    url = 'https://api.yelp.com/v3/businesses/search'

    api_key = API_KEY
    headers = {'Authorization': 'Bearer %s' % api_key}
     
    params = {'term':'restaurant',
            'location': location,
            'limit': 30}
 
     
    req = requests.get(url, params=params, headers=headers)
     
    data = req.json()
    print(data) 

    business_list = data['businesses']
    business= random.choice(business_list)

    name = business['name']
    image = business['image_url']
    rating = business['rating']
    address = ' '.join(business['location']['display_address'])
    url = business['url']
    phone = business['display_phone']
    restaurant_id = business['id']

    return jsonify({'name': name, 
                    'address': address, 
                    'phone' : phone, 
                    'url': url, 
                    'image_url': image})


@app.route('/users', methods=['POST'])

def register_user():
    email = request.form.get("email")
    password = request.form.get("password")

    result = crud.get_user_by_email(email)
    # print('hello', result)
    if result: 

        flash('Cannot create an account with that email. Try again.')
    else:
        user = crud.create_user(email, password)
        print('created_user', user)
        flash('Account created!')

    return redirect('/')

@app.route('/user_login')

def login_user():
    """Log in user"""
    email = request.args.get("email")
    password = request.args.get("password")

    user = crud.get_user_by_email(email)

    if user.password == password: 
        flash('Logged In Successfully!')
        session['user_id'] = user.user_id
        print(session)

        return redirect('/')
    else:
        flash('Log in fail!')
        return redirect('/')


@app.route('/create_favorite', methods=['POST'])
def add_favorites(): 
    """Add a restaurant to favorites list after pressing favorite button on 
    restaurant_results page"""

    restaurant_id = request.form.get('restaurant_id')
    name = request.form.get('name')
    display_address = request.form.get('address')
    display_phone = request.form.get('phone') 
    url = request.form.get('url')
    image_url = request.form.get('image')

    user_id = session.get('user_id')

    if not user_id: 
        return ("Please log in to add to favorite list")

    user = crud.get_user_by_id(user_id)

    if crud.check_favorite_exists(user, restaurant_id): 
        return("This has already been added to your favorites list!")

    else: 
        restaurant = crud.get_restaurant_by_id(restaurant_id)
        if restaurant: 
            favorite_restaurant = crud.create_favorite(user, restaurant)
            # flash('added!')
        else: 
            restaurant = crud.create_restaurant(restaurant_id=restaurant_id, 
                name = request.form.get('name'), 
                display_address = request.form.get('address'), 
                display_phone = request.form.get('phone'), 
                url = request.form.get('url'), 
                image_url = request.form.get('image'))
            favorite_restaurant = crud.create_favorite(user, restaurant)
            flash('added!')

    return jsonify({'name': name, 
                    'address': display_address, 
                    'phone' : display_phone, 
                    'url': url, 
                    'image_url': image_url})



@app.route('/favorite_restaurants')
def favorite_restaurant(): 
    """Page to display a user's favorite restaurants"""

    user_id = session['user_id']
    favorite_restaurants = crud.get_favorites_by_user_id(user_id)

    return render_template('favorite_restaurants.html', 
                            favorite_restaurants = favorite_restaurants)
    

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)