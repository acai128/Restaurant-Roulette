"""CRUD operations"""

from model import db, User, Favorite, Restaurant, connect_to_db

#Functions start here!

def create_user(fname, lname, password, email):
    """Create and return a new user."""

    user = User(fname=fname, lname=lname, password=password, email=email)

    db.session.add(user)
    db.session.commit()

    return user

def create_favorite(name, address, phone, transaction, url, image_url): 
    """Create and return a new favorite"""

    favorite = Favorite(name=name, 
                address=address, 
                phone=phone, 
                transaction=transaction,
                url=url,
                image_url=image_url)

    db.session.add(favorite)
    db.session.commit()

    return favorite

def get_Favorites(): 
    """Return all favorites on list"""
    return Favorite.query.all()

def get_restaurant(name, address, phone, transaction, url, image_url): 
    """Create and return a new rating"""

    restaurant = Restaurant(name=name, 
                address=address, 
                phone=phone, 
                transaction=transaction,
                url=url,
                image_url=image_url)

    db.session.add(restaurant)
    db.session.commit()

    return restaurant

if __name__ == '__main__':
    from server import app
    connect_to_db(app)