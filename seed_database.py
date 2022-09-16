"""Script to seed database."""

import os
import json

import model
import server
import crud

os.system("dropdb movies")
os.system('createdb movies')

model.connect_to_db(server.app)
model.db.create_all()

#load movie data from JSON file

def get_movies():
    """Load movies from film_info.json into databse."""
    
    with open('data/film_info.json') as f:
        movie_data = json.loads(f.read())
        for movie_to_add in movie_data:
            model.db.session.add(model.Movie(title = movie_to_add["title"], 
                                original_title = movie_to_add["original_title"],
                                original_title_rom = movie_to_add["original_title_romanised"],
                                image = movie_to_add["image"],
                                movie_banner = movie_to_add["movie_banner"],
                                description = movie_to_add["description"],
                                director = movie_to_add["director"],
                                producer = movie_to_add["producer"],
                                release_date = movie_to_add["release_date"],
                                running_time = movie_to_add["running_time"],
                                rt_score = movie_to_add["rt_score"]
                                ))
    model.db.session.commit()


def get_movie_from_title(title):
    """Return a movie from title"""
    return model.Movie.query.filter(model.Movie.title == title).first()

def get_location():
    """Load location from dataset into database."""
    with open('data/manual_location.json') as r:
        location_data = json.loads(r.read())
        for location in location_data:
            movie_to_edit = get_movie_from_title(location["movie"])
            model.db.session.add(model.Location(image = location["image"],
                                    latitude = location["latitude"],
                                    longitude = location["longitude"],
                                    place_movie = location["place_movie"],
                                    name_irl = location["name_irl"],
                                    description = location["description"],
                                    movie = movie_to_edit))    
    model.db.session.commit()
            


if __name__ == '__main__':
    model.connect_to_db(server.app)
    model.db.create_all()
    get_movies()
    get_location()