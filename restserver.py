#!/usr/bin/env python

import BaseHTTPServer

from restrequesthandler import RESTRequestHandler

def rest_server(port):
    print 'Starts the REST server'
    http_server = BaseHTTPServer.HTTPServer(('', port), RESTRequestHandler)
    print 'Starting HTTP server at port %d' % port
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        pass
    print 'Stopping HTTP server'
    http_server.server_close()