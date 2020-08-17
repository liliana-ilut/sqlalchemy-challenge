# import Flask and other dependencies
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
import datetime as dt
from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///../Resources/hawaii.sqlite", echo = True)

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect = True)

# Save references to each table
Measurement= Base.classes.measurement
Station= Base.classes.station

#create the session from Pythin to the DB
session = Session(engine)

# Flask Setup
# Create an app, being sure to pass __name__
app = Flask(__name__)

# flask routes: list all available routes
@app.route("/")
def welcome():
    # List all available api routes.
    return (
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )

# precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    session_1 = Session(engine)
    results_1 = session_1.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= "2016-08-23").order_by(Measurement.date).all()
    session_1.close()
    #create dictionary for JSON
    query_1_converted_to_dict = []
    for date, prcp in results_1:
        precipitation_dictionary = {}
        precipitation_dictionary["Date"] = date
        precipitation_dictionary["Precipitation"] = prcp
        query_1_converted_to_dict.append(precipitation_dictionary)
    return jsonify(query_1_converted_to_dict)

#stations route
@app.route("/api/v1.0/stations")
def stations():
    session_2 = Session(engine)
    results_2 = session_2.query(Station.station).all()
    session_2.close()
    #create dictionary for JSON
    query_2_converted_to_dict = []
    for station in results_2:
        station_dictionary = {}
        station_dictionary["station"] = station
        query_2_converted_to_dict.append(station_dictionary)
    return jsonify(query_2_converted_to_dict)

#tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    session_3 = Session(engine)
    results_3 = session_3.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= "2016-08-23").filter(Measurement.station == 'USC00519281').order_by(Measurement.date).all()
    session_3.close()
    # Create a dictionary from the row data and append to a list
    query_3_converted_to_dict = []
    for date, tobs in results_3:
        tobs_dictionary = {}
        tobs_dictionary["Date"] = date
        tobs_dictionary["Temperature"] = tobs
        query_3_converted_to_dict.append(tobs_dictionary)
    return jsonify(query_3_converted_to_dict)


if __name__ == "__main__":
    app.run(debug=True)




