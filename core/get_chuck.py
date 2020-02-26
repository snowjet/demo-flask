import os
import random
from core.log import logger

quotes = [
    {"name": "Chuck Norris", "quote": "Chuck Norris can pick oranges from an apple tree and make the best lemonade you have ever tasted"},
    {"name": "Chuck Norris", "quote": "Chuck Norris has been to mars thats why there are no signs of life"},
    {"name": "Chuck Norris", "quote": "Chuck Norris can divide by Zero"},
    {"name": "Chuck Norris", "quote": "When Chuck Norris throws exceptions, it’s across the room."},
    {"name": "Chuck Norris", "quote": "All arrays Chuck Norris declares are of infinite size, because Chuck Norris knows no bounds."},
    {"name": "Chuck Norris", "quote": "Chuck Norris doesn’t have disk latency because the hard drive knows to hurry up."},
    {"name": "Chuck Norris", "quote": "Chuck Norris writes code that optimizes itself."},
    {"name": "Chuck Norris", "quote": "Chuck Norris’s first program was kill -9."},
    {"name": "Chuck Norris", "quote": "Chuck Norris can write infinite recursion functions…and have them return."},
    {"name": "Chuck Norris", "quote": "Project managers never ask Chuck Norris for estimations…ever."},
    {"name": "Chuck Norris", "quote": "Chuck Norris’s keyboard doesn’t have a Ctrl key because nothing controls Chuck Norris."},
    {"name": "Chuck Norris", "quote": "'It works on my machine' always holds true for Chuck Norris."},
]


def get_chuck():
    try:
        hostname = os.uname()[1]
        index = int(random.randint(0, len(quotes) - 1))
        return hostname, quotes[index]["name"], quotes[index]["quote"]
    except Exception as err:
        logger.error(f"Other error occurred: {err}")
        return {"hostname": "hostname", "name": "error", "quote": err}

