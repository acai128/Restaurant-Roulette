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


def create_favorite(name, display_address, display_phone, transactions, url, image_url): 
    """Create and return a new favorite"""

    favorite = Favorite(name=name, 
                display_address=display_address, 
                display_phone=display_phone, 
                transactions=transactions,
                url=url,
                image_url=image_url)

    db.session.add(favorite)
    db.session.commit()

    return favorite

def get_Favorites(): 
    """Return all favorites on list"""
    return Favorite.query.all()

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

# def create_user(fname, lname, password, email):
#     """Create and return a new user."""

#     user = User(fname=fname, lname=lname, password=password, email=email)

#     db.session.add(user)
#     db.session.commit()

#     return user


if __name__ == '__main__':
    from server import app
    connect_to_db(app)