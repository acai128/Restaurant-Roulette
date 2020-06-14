"""CRUD operations"""

from model import db, User, Favorite, Restaurant, connect_to_db

#Functions start here!



def create_user(email, password):

    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def get_user_by_id(user_id):
    return db.session.query(User).get(user_id)


def create_favorite(user, restaurant):
    """Create and return a favorited trail."""

    favorite = Favorite(user = user, restaurant = restaurant)

    db.session.add(favorite)
    db.session.commit()

    return favorite


def get_favorites_by_user_id(user_id): 
    """Return all favorites on list"""
    return db.session.query(Favorite).filter(Favorite.user_id == user_id).all()

def check_favorite_exists(user, restaurant):
    return db.session.query(Favorite).filter(Favorite.user == user, 
                            Favorite.restaurant == restaurant).first()

def get_restaurant(name, display_address, display_phone, transactions, url, image_url): 
    """Create and return a new rating"""

    restaurant = Restaurant(name=name, 
                display_address=display_address, 
                display_phone=display_phone, 
                transactions=transactions,
                url=url,
                image_url=image_url)

    db.session.add(restaurant)
    db.session.commit()

    return restaurant

def get_restaurant_by_id(restaurant_id): 
    return db.session.query(Restaurant).get(restaurant_id)

# def create_user(fname, lname, password, email):
#     """Create and return a new user."""

#     user = User(fname=fname, lname=lname, password=password, email=email)

#     db.session.add(user)
#     db.session.commit()

#     return user

# def create_favorite(name, display_address, display_phone, transactions, url, image_url): 
#     """Create and return a new favorite"""

#     favorite = Favorite(name=name, 
#                 display_address=display_address, 
#                 display_phone=display_phone, 
#                 transactions=transactions,
#                 url=url,
#                 image_url=image_url)

#     db.session.add(favorite)
#     db.session.commit()

#     return favorite


if __name__ == '__main__':
    from server import app
    connect_to_db(app)