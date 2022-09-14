"""Script to seed database."""

import os
import json

import model
import server

model.connect_to_db(server.app)
model.db.create_all()

#load movie data from JSON file

with open('/data/film_info.json') as f:
    movie_data = json.loads(f.read())

#load dummy location data from JSON file

with open('/data/manual_location.json') as r:
    location_data = json.loads(r.read())

