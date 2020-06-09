#business search URL: https://api.yelp.com/v3/businesses/search

#import the modules 
import requests 
import os 

API_KEY = os.environ['YELP_KEY']

#define business ID
# business_id = ""

#define endpoint and header
YELP_KEY = API_KEY
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % YELP_KEY}

#Define the parameters 
PARAMETERS = {'term': 'italian',
            'limit': 1,
            'location': 'San Francisco'}

#Make the request to the yelp API 

response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

#convert JSON string to a dictionary 
businesss_data = response.json()

# print(businesss_data)

for biz in businesss_data['businesses']: 
    print(biz['display_phone'], 
            biz['name'], 
            biz['location']['display_address'],
            biz['transactions'], 
            biz['url'], 
            biz['image_url'])