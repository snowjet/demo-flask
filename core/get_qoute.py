import requests
from core.log import logger

from requests.exceptions import HTTPError


def get_quote(url):
    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        return {"name": "error", "quote": http_err}
    except Exception as err:
        logger.error(f"Other error occurred: {err}")
        return {"name": "error", "quote": err}
    else:
        try:
            json_object = response.json()
            logger.info("Success!")
            return response.json()
        except ValueError as e:
            logger.info("Not Valid JSON")
            return {"name": "error", "quote": "Not Valid JSON"}
