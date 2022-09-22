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
            new_movie = crud.create_new_movie(movie_to_add["title"],
                                    movie_to_add["original_title"],
                                    movie_to_add["original_title_romanised"],
                                    movie_to_add["image"],
                                    movie_to_add["movie_banner"],
                                    movie_to_add["description"],
                                    movie_to_add["director"],
                                    movie_to_add["producer"],
                                    movie_to_add["release_date"],
                                    movie_to_add["running_time"],
                                    movie_to_add["rt_score"]
                                    )
            model.db.session.add(new_movie)
    model.db.session.commit()

studio_ghibli = crud.create_new_user("StudioGhibli", "Studio", "Ghibli", "StudioGhibli@StudioGhibli.com", "StudioGhibli")
model.db.session.add(studio_ghibli)
model.db.session.commit()

def get_location():
    """Load location from dataset into database."""
    with open('data/manual_location.json') as r:
        location_data = json.loads(r.read())
        for location in location_data:
            movie_to_edit = crud.get_movie_from_title(location["movie"])
            ghibli_user = crud.get_user_by_username("StudioGhibli")
            new_location = crud.create_new_location(ghibli_user,
                                                    movie_to_edit,
                                                    location["latitude"],
                                                    location["longitude"],
                                                    location["place_movie"],
                                                    location["name_irl"],
                                                    location["description"],
                                                    location["photo"],
                                                    location["movie_still"],
                                                    False, 
                                                    "Approved",
                                                    True)    
            model.db.session.add(new_location)    
    model.db.session.commit()
            


if __name__ == '__main__':
    model.connect_to_db(server.app)
    model.db.create_all()
    get_movies()
    get_location()