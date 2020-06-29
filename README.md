# Restaurant Roulette 

Restaurant Roulette generates a random restaurant based on the location that a usesr inputs 

## Installation 

* Clone the repo to your local machine 
* Create a virtual environment, activate it, and install the project's dependencies from requirements.txt 

```bash
$ virtualenv env
$ source env/bin/activate
(env) $ pip3 install -r requirements.txt
```

* Get an API key from https://www.yelp.com/developers/documentation/v3/get_started, 
in project's main folder, create a secrets.sh file with export YELP_KEY="YOUR_API"in it, insert the API key you received 
* create database 

```bash
createdb restaurant
```


