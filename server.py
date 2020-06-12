from flask import (Flask, jsonify, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud 

from jinja2 import StrictUndefined 

from model import connect_to_db, Restaurant
import os
import requests 
from pprint import pformat
import json
# from config import Config
#from forms import SearchForm


from yelp_api import get_data
import urllib.parse 
from random import randint
import random 

app = Flask(__name__)
app.secret_key = 'SECRET!'
app.jinja_env.undefined = StrictUndefined


API_KEY = os.environ['YELP_KEY']

@app.route('/')
def homepage():
    """Show the homepage."""

    return render_template("index.html")


@app.route('/restaurant_result', methods = ['GET'])
def get_restaurants(): 
    """Show restuarnt results"""

    location = request.args['location']
    # print(location)
    # print(type(location))


    url = 'https://api.yelp.com/v3/businesses/search'

    api_key = API_KEY
    headers = {'Authorization': 'Bearer %s' % api_key}
     
    params = {'term':'restaurant',
            'location': location,
            'limit': 10}
 
     
    req = requests.get(url, params=params, headers=headers)
     
    data = req.json()
    print(data) 

    business_list = data['businesses']
    business= random.choice(business_list)
    # business = select.random(business_list)

    name = business['name']
    # print(name)
    image = business['image_url']
    rating = business['rating']
    address = ' '.join(business['location']['display_address'])
    url = business['url']
    phone = business['display_phone']
    transactions = business['transactions']


    # for biz in data['businesses']: 
    #     if len(data) == 0: 
    #         return None
    #     elif len(data) < 30: 
    #         i = random.randint(0, len(data) - 1)
    #     else: 
    #         i = random.randint(0,30)
    #     return data[i]
    #     print(data[i])

    # for biz in data['businesses']: 
    #     display_phone = biz['display_phone'], 
    #     name = biz['name'], 
    #     display_address = biz['location']['display_address'],
    #     transactions = biz['transactions'], 
    #     url = biz['url'], 
    #     image_url = biz['image_url']
    #     print(f'{data}')

    return render_template('restaurant_result.html', pformat=pformat, 
                            data=business, name=name, image=image, 
                            rating=rating, address=address, url=url,
                            transactions=transactions)


@app.route('/users', methods=['POST'])
def register_user():
    email = request.form.get("email")
    password = request.form.get("password")

    result = crud.get_user_by_email(email)
    print('hello', result)
    if result: 

        flash('Cannot create an account with that email. Try again.')
    else:
        user = crud.create_user(email, password)
        print('created_user', user)
        flash('Account created!')

    return redirect('/')

@app.route('/user_login')
def login_user():
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

# @app.route('/restaurant_result/<location>/<term>')
# def results(location = '', term = 'restaurant'):
#     business = get_restaurants(location, term)
#     if business == None:
#         return redirect('/no-results')
#     name = business['name']
#     image = business['image_url']
#     rating = business['rating']
#     address = ' '.join(business['location']['display_address'])
#     url = businesses['url']

#     return render_template('restaurant_result.html', name=name, image=image,
#     rating=rating, address=address, url=url )




if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)