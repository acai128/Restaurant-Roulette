# Restaurant Roulette 

Restaurant Roulette generates a random restaurant based on the location that a usesr inputs 

## Installation 

* Clone the repo to your local machine 
* Get an API key from https://www.yelp.com/developers/documentation/v3/get_started, 
in project's main folder, create a secrets.sh file with export YELP_KEY="YOUR_API"in it, "YOUR API" is where you will put the API key you got from the yelp developer page 

```python
export YELP_KEY="YOUR_API"
```

* Create a virtual environment, activate it, and install the project's dependencies from requirements.txt 

```bash
$ virtualenv env
$ source env/bin/activate
(env) $ pip3 install -r requirements.txt
```
* Execute secrets.sh to load YELP_KEY into environment 

```bash
$ source secrets.sh
```

* create database called restaurant 

```bash
createdb restaurant
```

* run python3 server.py to start server and open http://localhost:5000 in your browser

```bash
$ python3 server.py
```

