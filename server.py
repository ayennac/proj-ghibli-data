"""Server for ghibli data viz ."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)

import os
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
maps_api_key = os.environ['MAPS_API_KEY']

@app.route('/maps')
def homepage():
    """Show maps"""

    return render_template("maps.html", maps_api_key = maps_api_key)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
