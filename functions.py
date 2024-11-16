import os

from flask import Flask, flash, redirect, render_template, request, session, url_for, jsonify
from flask_session import Session
from werkzeug.utils import secure_filename
from datetime import datetime
import pytz

def fetch():
    return