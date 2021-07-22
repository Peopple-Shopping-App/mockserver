import json
import os.path

import falcon

from app.__root__ import __path__


class MockServerResource:
    def __init__(self):
        self.__root_path__ = __path__()

    async def on_get(self, req, resp, route: str):
        if not route.endswith(".json"):
            route += ".json"
        filepath = os.path.join(self.__root_path__, "assets", route)
        if not os.path.exists(filepath):
            raise falcon.HTTPNotImplemented("File Requested Not Available")
        with open(filepath, 'r') as fp:
            data = json.load(fp)
        resp.text = json.dumps(data)
