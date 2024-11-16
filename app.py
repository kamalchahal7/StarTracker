import os

from flask import Flask, flash, redirect, render_template, request, session, url_for, jsonify
from flask_session import Session
from werkzeug.utils import secure_filename
from functions import fetch
from datetime import datetime
import pytz

# Set timezone
utc_time = datetime.now(pytz.timezone('UTC'))
est_time = utc_time.astimezone(pytz.timezone('US/Eastern'))

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set the path for the images folder
app.config['IMAGES_FOLDER'] = 'static/images'

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    """Home Page"""
    return jsonify("Welcome to the home page!"), 200