import BaseHTTPServer

class RESTRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        return BaseHTTPServer.BaseHTTPRequestHandler.__init__(self, *args, **kwargs)