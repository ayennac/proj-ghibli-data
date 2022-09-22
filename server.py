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

@app.route('/')
def show_homepage():
    """Show homepage"""
    return render_template("home.html")

@app.route('/login', methods = ['GET'])
def show_login():
    """Show login page"""
    return render_template("login.html")

@app.route('/user-login', methods=['POST'])
def login_user():
    """Login user"""
    user_name = request.form.get('username')
    password = request.form.get('password')
#get user by username

#if not user
    #user not found
#if password in storage == password
    #put user in the session
    #successful login
#else
    #flash incorect password
    #redirect
    print(f'{user_name} {password}')
    return redirect('/login')

@app.route('/signup', methods=["GET"])
def show_signup():
    """Show sign up"""
    return render_template("signup.html")

@app.route('/user-signup', methods=['POST'])
def signup_user():
    """Sign up user"""

    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    username = request.form.get('username')
    email_address = request.form.get('email')
    password = request.form.get('password')
    if crud.get_user_by_email(email_address):
        flash("Email address already in use. Please log in with your username")
    if crud.get_user_by_username(username):
        flash("Username already in use. Please log in with your username")
    else:
        new_user = crud.create_new_user(username, first_name, last_name, email_address, password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account was made")
    return redirect('/')


@app.route('/maps')
def mapspage():
    """Show maps"""
    movies = crud.get_all_movies()
    return render_template("maps.html", 
                            maps_api_key = maps_api_key,
                            movies=movies)


@app.route('/api/locations')
def location_info():
    """JSON information about bears"""
    locations = [
        {
            "photo": location.photo,
            "movie_still": location.movie_still,
            "location_id": location.location_id,
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
