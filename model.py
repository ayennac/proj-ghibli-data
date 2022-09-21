"""Models for Ghibli App"""


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    """A movie."""

    __tablename__ = 'movies'

    movie_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key=True)
    title = db.Column(db.String, unique=True)
    original_title = db.Column(db.String, unique=True)
    original_title_rom = db.Column(db.String, unique=True)
    image = db.Column(db.String, unique=True)
    movie_banner = db.Column(db.String, unique=True)
    description = db.Column(db.String, unique=True)
    director = db.Column(db.String)
    producer = db.Column(db.String)
    release_date = db.Column(db.Integer)
    running_time = db.Column(db.Integer)
    rt_score = db.Column(db.Integer)
    
    locations  = db.relationship("Location", back_populates="movie")

    def __repr__(self):
        return f'<Movie movie_id={self.movie_id} title={self.title}>'


class Location(db.Model):
    """A location of a scene."""

    __tablename__ = 'locations'

    location_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    image = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    place_movie = db.Column(db.String)
    name_irl = db.Column(db.String)
    description = db.Column(db.String)

    movie = db.relationship("Movie", back_populates="locations")

    def __repr__(self):
        return f'<Location location_id={self.location_id} place={self.place_movie}>'


def connect_to_db(flask_app, db_uri="postgresql:///movies", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app, echo=False)