"""Server for ghibli data viz ."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)

import os
from jinja2 import StrictUndefined

import cloudinary.uploader

import crud

from model import connect_to_db, db, Location, Movie

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
maps_api_key = os.environ['MAPS_API_KEY']

CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']
CLOUD_NAME = "dvrzkwd2m"


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
    username = request.form.get('username')
    password = request.form.get('password')
    potential_user = crud.get_user_by_username(username)

    if potential_user.password == password:
        session['user_id'] = potential_user.user_id
        flash('Logged in!')
    else:
        flash('Not logged in!')
    return redirect("/")


    return redirect('/login')
    
@app.route("/logout")
def process_logout():
    """Log user out."""

    del session["user_id"]
    flash("Logged out.")
    return redirect("/")


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

@app.route('/userprofile')
def show_user_profile():
    """Show user profile"""
    
    user_id = session.get('user_id')
    if not user_id:
        flash("please log in")
        return redirect('/login')

    locations = crud.get_location_by_user(user_id)
    user = crud.get_user_by_userid(user_id)

    return render_template('userprofile.html', user = user, locations = locations)


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

@app.route('/new-location', methods=['POST'])
def newlocation():
    user = crud.get_user_by_userid(session.get('user_id'))
    print(user)
    movie = crud.get_movie_from_title("Princess Mononoke")
    latitude = 35.75408552508377
    longitude = 139.7690024152055
    place_movie = "The Sea"
    name_irl = "Place"
    description = request.form.get("pic-description")
    photo = request.files["inputpic"]

    cloudinary_request = cloudinary.uploader.upload(photo,
                                                    api_key=CLOUDINARY_KEY,
                                                    api_secret=CLOUDINARY_SECRET,
                                                    cloud_name=CLOUD_NAME)
    cloudinary_img_src = cloudinary_request['secure_url']


    movie_still = "/static/sample_bird.jpg"

    new_location = crud.create_new_location(user, 
                                        movie, 
                                        latitude, 
                                        longitude, 
                                        place_movie, 
                                        name_irl, 
                                        description, 
                                        cloudinary_img_src, 
                                        movie_still, 
                                        False, 
                                        "Approved",
                                        True)
    db.session.add(new_location)    
    db.session.commit()
    flash("added new location to database!")
    return redirect("/userprofile")





if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
