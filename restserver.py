#! /usr/bin/env python

# IMPORTS
import json
import os
import re
import urllib

import BaseHTTPServer
import urllib2

# List of stored tasks
tasks = {}

# current location path
current_path = os.path.dirname(os.path.realpath(__file__))


# returns list of tasks
def get_tasks(handler):
    return tasks


# returns particular task specified by id
def get_task(handler):
    key = urllib.unquote(handler.path[6:])
    return tasks[key] if key in tasks else None


# add new task
def add_task(handler):
    key = urllib.unquote(handler.path[6:])
    print(key)
    payload = handler.get_payload()
    tasks[key] = payload
    return tasks[key]


# removes particular task specified by id
def remove_task(handler):
    key = urllib.unquote(handler.path[6:])
    del tasks[key]
    return True


def rest_call_json(url, payload=None, with_payload_method='PUT'):
    if payload:
        if not isinstance(payload, basestring):
            payload = json.dumps(payload)
        # PUT or POST
        response = urllib2.urlopen(
            MethodRequest(url, payload, {'Content-Type': 'application/json'}, method=with_payload_method))
    else:
        # GET
        response = urllib2.urlopen(url)
    response = response.read().decode()
    return json.loads(response)


class MethodRequest(urllib2.Request):
    def __init__(self, *args, **kwargs):
        if 'method' in kwargs:
            self._method = kwargs['method']
            del kwargs['method']
        else:
            self._method = None
        return urllib2.Request.__init__(self, *args, **kwargs)

    def get_method(self, *args, **kwargs):
        return self._method if self._method is not None else urllib2.Request.get_method(self, *args, **kwargs)


class RESTRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # routes defined for return list of tasks and single task operations
        self.routes = {
            r'^/tasks': {'GET': get_tasks, 'media_type': 'application/json'},
            r'^/task/': {'GET': get_task, 'PUT': add_task, 'DELETE': remove_task,
                         'media_type': 'application/json'}}

        return BaseHTTPServer.BaseHTTPRequestHandler.__init__(self, *args, **kwargs)

    def do_HEAD(self):
        self.handle_method('HEAD')

    def do_GET(self):
        self.handle_method('GET')

    def do_POST(self):
        self.handle_method('POST')

    def do_PUT(self):
        self.handle_method('PUT')

    def do_DELETE(self):
        self.handle_method('DELETE')

    def get_payload(self):
        payload_len = int(self.headers.getheader('content-length', 0))
        payload = self.rfile.read(payload_len)
        payload = json.loads(payload)
        return payload

    # responsible for handling calls
    def handle_method(self, method):
        route = self.get_route()
        if route is None:
            self.send_response(404)
            self.end_headers()
            self.wfile.write('Route not found\n')
        else:
            if method == 'HEAD':
                self.send_response(200)
                if 'media_type' in route:
                    self.send_header('Content-type', route['media_type'])
                self.end_headers()
            else:
                if method in route:
                    content = route[method](self)
                    if content is not None:
                        self.send_response(200)
                        if 'media_type' in route:
                            self.send_header('Content-type', route['media_type'])
                        self.end_headers()
                        if method != 'DELETE':
                            self.wfile.write(json.dumps(content))
                    else:
                        self.send_response(404)
                        self.end_headers()
                        self.wfile.write('Not found\n')
                else:
                    self.send_response(405)
                    self.end_headers()
                    self.wfile.write(method + ' is not supported\n')

    def get_route(self):
        for path, route in self.routes.iteritems():
            if re.match(path, self.path):
                return route
        return None


# starts and stops REST server
def rest_server(port):
    print('Starts the REST server')
    http_server = BaseHTTPServer.HTTPServer(('', port), RESTRequestHandler)
    print('Starting HTTP server at port %d...' % port)
    print('CTRL + C stops the server')
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        pass
    print('Stopping HTTP server')
    http_server.server_close()
