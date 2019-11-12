from functools import wraps
import json
from os import environ as env
from werkzeug.exceptions import HTTPException

from flask import Flask
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from authlib.flask.client import OAuth
from six.moves.urllib.parse import urlencode

from flask_bootstrap import Bootstrap

from core.config import LOG_LEVEL, IBM_IMAGE_NAME, REDHAT_IMAGE_NAME, SECRET_IMAGE_LOCATION
from core.log import logger

logger.info("Config Imported", LOG_LEVEL=LOG_LEVEL, IBM_IMAGE_NAME=IBM_IMAGE_NAME, REDHAT_IMAGE_NAME=REDHAT_IMAGE_NAME, SECRET_IMAGE_LOCATION=SECRET_IMAGE_LOCATION)

if LOG_LEVEL == "DEBUG":
    DEBUG = True
else:
    DEBUG = False

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/redhat")
def redhat():
    return render_template("redhat.html",
    image=REDHAT_IMAGE_NAME)

@app.route("/ibm")
def ibm():
    return render_template("ibm.html",
    image=IBM_IMAGE_NAME)

@app.route("/secret")
def secret():
    return render_template("secret.html",
    image=SECRET_IMAGE_LOCATION)

if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0')
