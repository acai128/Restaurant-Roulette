from flask import (Flask, jsonify, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud 

from jinja2 import StrictUndefined 

#from model import connect_to_db, Restaurant
import os
import requests 
from pprint import pformat
import json



app = Flask(__name__)
app.secret_key = 'SECRET!'
app.jinja_env.undefined = StrictUndefined


API_KEY = os.environ['YELP_KEY']


@app.route('/')
def homepage():
    """Show the homepage."""

    return render_template("index.html")

@app.route('/restaurant_result', methods = ['GET'])
def get_restaurant(): 
    """Show homepage and display random restaurant result"""
    get_location = request.form.get('location')

    api_key = 'g3qgKeAPXG6wglXFjK6bujzTAb3enURngk2_5rRl48H5tyTEzeC5g71L8n--IEM0lonrF4mEXeOHwaHZizgm-_o_vvABicAxZZZTRDXP9dd0eTxU5tnqPPwkLPveXnYx'
    headers = {'Authorization': 'Bearer %s' % api_key}
     
    url = 'https://api.yelp.com/v3/businesses/search'

    params = {'term':'restaurant',
                'location': 'location'}
     
    req = requests.get(url, params=params, headers=headers)
     
    data = json.loads(req.text)
     
    businesses = data["businesses"]

    return render_template('restaurant_result.html', pformat=pformat, data=data)


# @app.route('/restaurant_result', methods = ['GET'])
# def get_restaurant(): 
    """Show homepage and display random restaurant result"""
    # location = request.form.get('location')
   
    # api_key = API_KEY
    # url = 'https://api.yelp.com/v3/businesses/search'
    # headers = {'Authorization': 'Bearer %s' % API_KEY}

    #Define the parameters 
    # params= {'term': 'restaurant',
    #         'location': location}
            # 'Authorization': Bearer <vGzOs92hxa6YelsbG2GMSe8mpog_T4O4mizIRa7spW06cU_k8ES4UjSTYHmzKHAHjZyNx79p9N2oQ1aOeQ4f6Rzxc_PbjUbpncbQNCo8Tm2jRwS9_FhOhZxKIK3BXnYx>}
    #Make the request to the yelp API 

    # req = requests.get(url, headers=headers, params=params)
   
    # convert JSON string to a dictionary 
    # data = json.loads(req.text)
    # businesses = data['businesses']

    # print(businesss_data)

    # for biz in restaurant_results: 
    #         display_phone = biz['display_phone'], 
    #         name = biz['name'], 
    #         display_address = biz['location']['display_address'],
    #         transactions = biz['transactions'], 
    #         url = biz['url'], 
    #         image_url = biz['image_url']
    #         print(f'{restaurant_results}')
    # return render_template('restaurant_result.html', pformat=pformat, data=data)

# def query_api(term, location):
#     """Queries the API by the input values from the user.
#     Args:
#         term (str): The search term to query.
#         location (str): The location of the business to query.
#     """
#     response = search(API_KEY, term, location)

#     businesses = response.get('businesses')

#     if not businesses:
#         print(u'No businesses for {0} in {1} found.'.format(term, location))
#         return

#     business_id = businesses[0]['id']

#     print(u'{0} businesses found, querying business info ' \
#         'for the top result "{1}" ...'.format(
#             len(businesses), business_id))
#     response = get_business(API_KEY, business_id)

#     print(u'Result for business "{0}" found:'.format(business_id))
#     pprint.pprint(response, indent=2)
 
#     return render_template('restaurant_result.html')


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)