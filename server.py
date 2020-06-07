from flask import (Flask, jsonify, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud 

from jinja2 import StrictUndefined 

#from model import connect_to_db, Restaurant
import os
import requests 

API_KEY = os.environ['YELP_KEY']



app = Flask(__name__)
app.secret_key = 'SECRET!'
app.jinja_env.undefined = StrictUndefined


API_KEY = os.environ['YELP_KEY']


# @app.route("/")
# def homepage():
#     """Show the homepage."""

#     return render_template("index.html")

@app.route("/")
def get_restaurant(): 
    """Show homepage and display random restaurant result"""
    location = request.args.get('location', '')

    YELP_KEY = API_KEY
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
    HEADERS = {'Authorization': 'bearer %s' % YELP_KEY}

    #Define the parameters 
    PARAMETERS = {'location': location}

    #Make the request to the yelp API 

    response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

    #convert JSON string to a dictionary 
    businesss_data = response.json()

    # print(businesss_data)

    # for biz in businesss_data['businesses']: 
    #     print (biz['display_phone'], 
    #         (biz['name'], 
    #         biz['location']['display_address'],
    #         biz['transactions'], 
    #         biz['url'], 
    #         biz['image_url'])
 
    return render_template('index.html')



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)