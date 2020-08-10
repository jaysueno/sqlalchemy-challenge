## SQLALCHEMY HOMEWORK APP

# 1. import Flask
from flask import Flask, jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# 2. Setup database and reflect the tables using sqlalchemy
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# 3. Create an app, being sure to pass __name__
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

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

# 5. Create route "/api/v1.0/precipitation" to take the SQL query and return a jsonified dictionary
# Convert the query results to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Servier received request for '/api/v1.0/precipitation'.")
    # Create our session (link) from Python to the DB
    session = Session(engine) 
    # Query date and prcp from database and then turn into a dictionary
    data_prcp = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date.desc())\
    .filter(Measurement.date > '2016-08-23').all()
    # Close session to server to prevent hackers
    session.close()
    # Use list comprehession to create a dictionary
    prcp_dict = {}

    return(

    )

# 6. Create route "/api/v1.0/stations"
# Return a JSON list of stations from the dataset.
def station():
    print("Servier received request for '/api/v1.0/stations'.")
    # Create our session (link) from Python to the DB
    session = Session(engine) 
    # Query date and prcp from database and then turn into a dictionary
    station_names = session.query(Station.name).all()
    # Close session to server to prevent hackers
    session.close()
    # Use list comprehession to create a dictionary
    return jsonify(station_names)

# 7. Create route "<li>/api/v1.0/tobs</li>"
# Query the dates and temperature observations of the most active station for the last year of data.
# Return a JSON list of temperature observations (TOBS) for the previous year.
def temperatures():
    print("Servier received request for '/api/v1.0/tobs'.")
    # Create our session (link) from Python to the DB
    session = Session(engine) 
    # Query date and prcp from database and then turn into a dictionary
    station_12months = session.query(Measurement.station, Measurement.tobs)\
    .filter(Measurement.station == 'USC00519281')\
    .filter(Measurement.date > '2016-08-23')
    # Close session to server to prevent hackers
    session.close()

    return jsonify(station_12months)


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
