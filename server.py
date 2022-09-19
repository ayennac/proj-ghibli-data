"""Server for ghibli data viz ."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)

import os
from jinja2 import StrictUndefined

import crud

from model import connect_to_db, db, Location, Movie

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
maps_api_key = os.environ['MAPS_API_KEY']
#make sure to source secrets.sh to put it into the environment 


@app.route('/maps')
def homepage():
    """Show maps"""

    return render_template("maps.html", maps_api_key = maps_api_key)

@app.route('/api/locations')
def location_info():
    """JSON information about bears"""
    locations = [
        {
            "image": location.image,
            "latitude": location.latitude,
            "longitude": location.longitude,
            "place_movie": location.place_movie,
            "name_irl": location.name_irl,
            "description": location.description,
            "movie": location.movie.title
        }
        for location in crud.get_all_locations()
    ]
    return jsonify(locations)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
