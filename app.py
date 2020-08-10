## SQLALCHEMY HOMEWORK APP

# 1. import Flask
from flask import Flask, jsonify

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# 3. Create index/home '/' route and Define the home() method that lists routes on server 
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Jay Sueno's SQLAchemy Homework assignment number 10. </br>"
        f"This is my Climate App that I have created.</br> "
        f"You will find the following ROUTES on this server:</br>"
        f"<ul>"
        f"<li>/api/v1.0/precipitation</li>"
        f"<li>/api/v1.0/stations</li>"
        f"<li>/api/v1.0/tobs</li>"
        f"<li>/api/v1.0/<start></li>"
        f"<li>/api/v1.0/<start>/<end></li>"
        f"</ul>"
    )


# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return(
        f"My name is Jay Sueno. I'm a USCD Data Science student.</br>"
        f"Visit my LinkedIn at https://www.linkedin.com/in/jay-sueno-359a274/"
        # f"To learn more about me visit my <a href="https://www.linkedin.com/in/jay-sueno-359a274/" target="_blank">LinkedIn Profile</a>
    ) 


if __name__ == '__main__':
    app.run(debug=True)

#Jsonify example 
#hello_dict = {"Hello": "World!"}

# @app.route("/normal")
# def normal():
#     return hello_dict


# @app.route("/jsonified")
# def jsonified():
#     return jsonify(hello_dict)

## example of doing a search through the url name and returning a json dict
# @app.route("/api/v1.0/justice-league/<real_name>")
# def justice_league_character(real_name):
#     """Fetch the Justice League character whose real_name matches
#        the path variable supplied by the user, or a 404 if not."""

#     canonicalized = real_name.replace(" ", "").lower()
#     for character in justice_league_members:
#         search_term = character["real_name"].replace(" ", "").lower()

#         if search_term == canonicalized:
#             return jsonify(character)

#     return jsonify({"error": f"Character with real_name {real_name} not found."}), 404
