# import Flask and other dependencies
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect = True)
# Save references to the tables
Measurement= Base.classes.measurement
Station= Base.classes.station

# Flask Setup
# Create an app, being sure to pass __name__
app = Flask(__name__)
# Define what to do when a user hits the index route
@app.route("/")