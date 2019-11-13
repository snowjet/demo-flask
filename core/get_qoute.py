import requests
from core.log import logger

from requests.exceptions import HTTPError


def get_quote(url):
    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")  # Python 3.6
    except Exception as err:
        logger.error(f"Other error occurred: {err}")  # Python 3.6
    else:
        logger.info("Success!")
        return response.json()
