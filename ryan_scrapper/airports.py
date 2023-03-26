import requests

import json

from .constants import ACTIVE_AIRPORTS


def get_airports():
    return json.loads(requests.get(ACTIVE_AIRPORTS).text)
