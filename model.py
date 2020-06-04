from flask_sqlalchemy import SQLAlchemy

# Instantiate a SQLAlchemy object. We need this to create our db.Model classes.
db = SQLAlchemy()

#COMPOSE ORM 

class User(db.Model): 

    __table__name = "users"

    user_id = db.Column(db.Integer, 
                autoincrement = True, 
                primary_key = True)
    fname = db.Column(db.String, nullable = False)
    lname = db.Column(db.String, nullable = False)

    def __repr__(self): 

        return f'<User user_id={self.user_id} fname={self.fname}\
            lname={self.lname}>'

class Favorite(db.Model): 

    __table__name = "favorites"

    favorite_id = db.Column(db.Integer, 
                autoincrement = True, 
                primary_key = True)

    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.user_id'))

    restaurant_id = db.Column(db.Integer, 
                    db.ForeignKey('restaurants.restaurant_id'))
    

    user = db.relationship('User', backref='favorites')
    restaurant = db.relationship('Restaurant', backref='favorites')

def __repr__(self): 

    return f'<Favorite favorite_id={self.favorite_id}>'


class Restaurant(db.Model): 

    __table__name = "restaurants"


    restaurant_id = db.Column(db.Integer, 
                autoincrement = True, 
                primary_key = True)
    name = db.Column(db.String, nullable = False)
    address = db.Column(db.String, nullable = False)
    phone = db.Column(db.Integer, nullable = False)
    delivery = db.Column(db.Boolean, nullable = False)

def __repr__(self): 

    return f'<Restaurant restaurant_id={self.restaurant_id} name={self.name}\
    address={self.address} phone={self.phone} delivery={self.delivery}>'

##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///restaurant"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
