"""CRUD operations"""

from model import db, Movie, Location, connect_to_db


def get_movie_from_title(title):
    """Return a movie from title"""
    return Movie.query.filter(Movie.title == title).first()


def get_all_locations():
    """Return a list of locations"""
    return Location.query.all()

def get_all_movies():
    """Return a list of all movies"""
    return Movie.query.all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)