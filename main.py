from flask import Flask
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from flask import request

from six.moves.urllib.parse import urlencode
from flask_bootstrap import Bootstrap

from core.config import (
    LOG_LEVEL,
    MAP_IMAGE_NAME,
    MAIN_TITLE_NAME,
    MAIN_IMAGE_NAME,
    OPENSHIFT_IMAGE_NAME,
    SECRET_IMAGE_LOCATION,
    src_image_data,
    QUOTE_URL,
)
from core.log import logger
from core.get_qoute import get_quote
from core.get_chuck import get_chuck

logger.info(
    "Config Imported",
    MAIN_TITLE_NAME=MAIN_TITLE_NAME,
    LOG_LEVEL=LOG_LEVEL,
    MAIN_IMAGE_NAME=MAIN_IMAGE_NAME,
    MAP_IMAGE_NAME=MAP_IMAGE_NAME,
    OPENSHIFT_IMAGE_NAME=OPENSHIFT_IMAGE_NAME,
    SECRET_IMAGE_LOCATION=SECRET_IMAGE_LOCATION,
    QUOTE_URL=QUOTE_URL,
)

if LOG_LEVEL == "DEBUG":
    DEBUG = True
else:
    DEBUG = False

app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route("/")
def home():
    return render_template("home.html", title=MAIN_TITLE_NAME, image=MAIN_IMAGE_NAME, nav="home")


@app.route("/openshift")
def redhat():
    return render_template("openshift.html", title=MAIN_TITLE_NAME, image=OPENSHIFT_IMAGE_NAME, nav="openshift")


@app.route("/map")
def map():
    return render_template("map.html", title=MAIN_TITLE_NAME, image=MAP_IMAGE_NAME, nav="map")


@app.route("/secret")
def secret():
    return render_template("secret.html", title=MAIN_TITLE_NAME, src_image=src_image_data, nav="secret")


@app.route("/quote")
def quote():
    quote_json = get_quote(url=QUOTE_URL)

    if "type" in request.args:
        if request.args["type"] == "json":
            return jsonify(name=quote_json['name'], quote=quote_json['quote'])

    return render_template("quote.html", title=MAIN_TITLE_NAME, quote_json=quote_json, nav="quote")


@app.route("/chuck")
def chuck():
    hostname, name, quote = get_chuck()
    logger.info("Returned Quote:", hostname=hostname, name=name, quote=quote)

    return jsonify(hostname=hostname, name=name, quote=quote)



if __name__ == "__main__":
    app.run(debug=DEBUG, host="0.0.0.0", port=8080)
