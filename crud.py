"""CRUD operations"""

from model import db, User, Favorite, Restaurant, connect_to_db

# *******************
# USER CRUD FUNCTIONS:
# *******************

def create_user(email, password):
    """Create and return a new user"""

    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def get_user_by_id(user_id):
    """Return a user by id"""
    return db.session.query(User).get(user_id)

# *******************
# FAVORITE CRUD FUNCTIONS:
# *******************

def create_favorite(user, restaurant):
    """Create and return a favorited trail."""

    favorite = Favorite(user = user, restaurant= restaurant)

    db.session.add(favorite)
    db.session.commit()

    return favorite


def get_favorites_by_user_id(user_id): 
    """Return all favorites on list"""
    return db.session.query(Favorite).filter(Favorite.user_id == user_id).all()

def check_favorite_exists(user, restaurant_id):
    return db.session.query(Favorite).filter(Favorite.user == user, 
                            Favorite.restaurant_id == restaurant_id).first()


# *******************
# RESTAURANT CRUD FUNCTIONS:
# *******************

def create_restaurant(restaurant_id,name, display_address, display_phone, url, image_url): 
    """Create and return a new restaurant"""

    restaurant = Restaurant( restaurant_id = restaurant_id, name=name, 
                display_address=display_address, 
                display_phone=display_phone,
                url=url,
                image_url=image_url)

    db.session.add(restaurant)
    db.session.commit()

    return restaurant

def all_restaurants(): 
    """Return all restaurants in db"""
    return db.session.query(Restaurant).all()

def get_restaurant_by_id(restaurant_id): 
    return db.session.query(Restaurant).get(restaurant_id)




if __name__ == '__main__':
    from server import app
    connect_to_db(app)