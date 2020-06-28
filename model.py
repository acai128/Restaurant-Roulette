from flask_sqlalchemy import SQLAlchemy

# Instantiate a SQLAlchemy object. We need this to create our db.Model classes.
db = SQLAlchemy()

#COMPOSE ORM 


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Favorite(db.Model): 

    __tablename__ = "favorites"

    favorite_id = db.Column(db.Integer, 
                autoincrement = True, 
                primary_key = True)

    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.user_id'), nullable = False)

    restaurant_id = db.Column(db.String, 
                    db.ForeignKey('restaurants.restaurant_id'), nullable = False)
    

    user = db.relationship('User', backref='favorites')
    restaurant = db.relationship('Restaurant', backref='favorites')

def __repr__(self): 

    return f'<Favorite favorite_id={self.favorite_id} user_id={self.user_id}\
            trail_id={self.trail_id}>'

class Restaurant(db.Model): 

    __tablename__ = "restaurants"


    restaurant_id = db.Column(db.String, 
                primary_key = True)
    name = db.Column(db.String, nullable = False)
    display_address = db.Column(db.String, nullable = False)
    display_phone = db.Column(db.String, nullable = False)
    # transactions = db.Column(db.Boolean, nullable = False)
    url = db.Column(db.String, nullable = False)
    image_url = db.Column(db.String, nullable = False)

def __repr__(self): 

    return f'<Restaurant restaurant_id={self.restaurant_id} name={self.name}\
    display_address={self.display_address} display_phone={self.display_phone} \
    url={self.url} image_url={self.image_url}>'




##############################################################################
# Helper functions

def connect_to_db(flask_app, db_uri='postgresql:///restaurant', echo=True):

    """Connect the database to our Flask app."""

    # Configure to use our database

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = False
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = flask_app
    db.init_app(flask_app)

    #db.create_all()
    print('connected to db')

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
