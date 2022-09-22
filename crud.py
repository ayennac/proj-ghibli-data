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


def create_new_user(username, first_name, last_name, email_address, password):
    """Return a new User object"""
    user = User(username=username, first_name=first_name, email_address =email_address, password=password)
    return user
    

def get_user_by_username(username):
    """Return a user from username"""
    return User.query.get(username)


def create_new_movie(title, original_title , original_title_rom, image, movie_banner, description, director, producers, release_date, running_time, rt_score):
    """Return a new movie"""

    movie = Movie(title=title,                 original_title=original_title,
                    original_title_rom=original_title_rom,
                    image=image, movie_banner=movie_banner,
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