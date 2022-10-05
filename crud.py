"""CRUD operations"""

from model import db, Movie, Location, connect_to_db, User

from random import choice

def get_movie_from_title(title):
    """Return a movie from title"""
    return Movie.query.filter(Movie.title == title).first()


def get_all_locations():
    """Return a list of locations"""
    return Location.query.all()

def get_all_movies():
    """Return a list of all movies"""
    return Movie.query.all()


def get_location_by_user(user_id):
    """Return a list of locations"""

    return Location.query.filter(User.user_id == user_id).all()

def get_random_location():
    locations = get_all_locations()
    location_chosen = choice(locations)
    return Location.query.filter(Location.location_id == location_chosen.location_id).first()


def create_new_user(username, first_name, last_name, email_address, password):
    """Return a new User object"""
    user = User(username=username, first_name=first_name, last_name =last_name, email_address =email_address, password=password)
    return user
    

def get_user_by_userid(userid):
    """Return a user from userid"""
    return User.query.get(userid)

def get_user_by_username(username):
    """Return a user from email"""
    return User.query.filter(User.username == username).first()

def get_user_by_email(email_address):
    """Return a user from email"""
    return User.query.filter(User.email_address == email_address).first()


def create_new_movie(title, original_title , original_title_rom, image, movie_banner, description, director, producer, release_date, running_time, rt_score):
    """Return a new movie"""

    movie = Movie(title=title,                 
                    original_title=original_title,
                    original_title_rom=original_title_rom,
                    image=image, 
                    movie_banner=movie_banner,
                    description=description,
                    director=director,
                    producer=producer,
                    release_date=release_date,
                    running_time=running_time,
                    rt_score=rt_score)
    return movie

def create_new_location(user, movie, latitude, longitude, place_movie, name_irl, description, photo, movie_still, submitted, submission_status, public):
    location = Location(user=user,
                        movie=movie,
                        latitude=latitude,
                        longitude=longitude,
                        place_movie=place_movie,
                        name_irl=name_irl,
                        description=description,
                        photo=photo,
                        movie_still=movie_still,
                        submitted=submitted,
                        submission_status=submission_status,
                        public=public)
    
    return location


if __name__ == '__main__':
    from server import app
    connect_to_db(app)