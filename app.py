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
        f"<li>/about</li>"
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
    data_prcp = session.query(Measurement.date, Measurement.prcp)\
        .order_by(Measurement.date.desc())\
        .filter(Measurement.date > '2016-08-23').all()
    # Close session to server to prevent hackers
    session.close()
    # Use list comprehession to create a dictionary
    prcp_dict = {}
    for date, prcp in data_prcp:
        if date not in prcp_dict:
            prcp_dict[date] = []
            prcp_dict[date].append(prcp)
        else:
            prcp_dict[date].append(prcp)
    return jsonify(prcp_dict)

# 6. Create route "/api/v1.0/stations"
# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
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
@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for '/api/v1.0/tobs'.")
    # Create our session (link) from Python to the DB
    session = Session(engine) 
    # Query date and prcp from database and then turn into a dictionary
    station_12months = session.query(Measurement.station, Measurement.tobs)\
        .filter(Measurement.station == 'USC00519281')\
        .filter(Measurement.date >= '2016-08-23').all()
    # Close session to server to prevent hackers
    session.close()
    # Print the temp data from the most active station from the last year
    station_list = list(np.ravel(station_12months))
    # station_list = list(np.ravel(results))
    return jsonify(station_list)

# 8. Create route "/api/v1.0/<start>"
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
@app.route("/api/v1.0/<start>")
def date_starts(start):
    print("Server received request for '/api/v1.0/<start>'.")
    # Create our session (link) from Python to the DB
    session = Session(engine) 
    # Query date and prcp from database and then turn into a dictionary
    # Lowest temperature query
    station_low_temp = session.query(func.min(Measurement.tobs))\
        .filter(Measurement.station == 'USC00519281')\
        .filter(Measurement.date >= start).first()
    station_avg_temp = session.query(func.avg(Measurement.tobs))\
        .filter(Measurement.station == 'USC00519281')\
        .filter(Measurement.date >= start).first()
    station_high_temp = session.query(func.max(Measurement.tobs))\
        .filter(Measurement.station == 'USC00519281')\
        .filter(Measurement.date >= start).first()
    # Close session to server to prevent hackers
    session.close()
    temps_dict = {"Low Temp": station_low_temp, "Average Temp": station_avg_temp, "Hi Temp": station_high_temp}
    return jsonify(temps_dict)

# 9. Create route "/api/v1.0/<start>/<end>"
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
@app.route("/api/v1.0/<start>/<end>")
def date_start_end(start, end):
    print("Server received request for '/api/v1.0/<start>/<end>'.")
     # Create our session (link) from Python to the DB
    session = Session(engine) 
    # Query date and prcp from database and then turn into a dictionary
    # Lowest temperature query
    station_low_temp = session.query(func.min(Measurement.tobs))\
        .filter(Measurement.station == 'USC00519281')\
        .filter(Measurement.date <= end)\
        .filter(Measurement.date >= start).first()
    station_avg_temp = session.query(func.avg(Measurement.tobs))\
        .filter(Measurement.station == 'USC00519281')\
        .filter(Measurement.date <= end)\
        .filter(Measurement.date >= start).first()
    station_high_temp = session.query(func.max(Measurement.tobs))\
        .filter(Measurement.station == 'USC00519281')\
        .filter(Measurement.date <= end)\
        .filter(Measurement.date >= start).first()
    # Close session to server to prevent hackers
    session.close()
    temps_dict = {"Low Temp": station_low_temp, "Average Temp": station_avg_temp, "Hi Temp": station_high_temp}
    return jsonify(temps_dict)

if __name__ == '__main__':
    app.run(debug=True)