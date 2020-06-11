#business search URL: https://api.yelp.com/v3/businesses/search

#import the modules 
import requests 
import os 
import random

API_KEY = os.environ['YELP_KEY']

def get_data(location, term):
    api_key = YELP_KEY
    headers = {'Authorization': 'Bearer %s' % api_key}

    url = 'https://api.yelp.com/v3/businesses/search'
    if term!='':
        params = {'term': term, 'location': location}
    else:
        params = {'location': location}
    try:
        req = requests.get(url, params = params, headers = headers)
        parsed = json.loads(req.text)
        businesses = parsed['businesses']
    except:
        return None
    if len(businesses) == 0:
        return None
    elif len(businesses) < 30:
        i = random.randint(0, len(businesses) - 1)
    else:
        i = random.randint(0,30)
    return businesses[i]

    print(businesses)


#Define the parameters 
# PARAMETERS = {'term': 'italian',
#             'limit': 1,
#             'location': 'San Francisco'}

# #Make the request to the yelp API 

# response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

# #convert JSON string to a dictionary 
# businesss_data = response.json()

# print(businesss_data)

# for biz in businesss_data['businesses']: 
#     print(biz['display_phone'], 
#             biz['name'], 
#             biz['location']['display_address'],
#             biz['transactions'], 
#             biz['url'], 
#             biz['image_url'])


# import requests
# import json
# import random

# def get_data(location, term):
#     api_key = '6MqGGOGfbw44AovX18OKlkUjdb1UBAxui9s03uPsZ4HLaJ7Ubru5ov9IUR8xJBYCVohnazSYRM_PUJtq-4a4hvSFbPMpXL9DQpuoBL4b4o9vedDZzJYMd4x4K0TIXXYx'
#     headers = {'Authorization': 'Bearer %s' % api_key}

#     url = 'https://api.yelp.com/v3/businesses/search'
#     if term!='':
#         params = {'term': term, 'location': location}
#     else:
#         params = {'location': location}
#     try:
#         req = requests.get(url, params = params, headers = headers)
#         parsed = json.loads(req.text)
#         businesses = parsed['businesses']
#     except:
#         return None
#     if len(businesses) == 0:
#         return None
#     elif len(businesses) < 30:
#         i = random.randint(0, len(businesses) - 1)
#     else:
#         i = random.randint(0,30)
#     return businesses[i]
