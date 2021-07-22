import falcon.asgi

from app.api.mock_server import MockServerResource

msr = MockServerResource()

app = falcon.asgi.App()

app.add_route(uri_template='/{route}', resource=msr)
