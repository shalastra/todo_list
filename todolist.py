import urllib
from methodrequest import MethodRequest

class TodoList():
    def __init__(self):
        self.todos = {}

    def get_tasks(handler):
        return self.todos

    def get_task(handler):
        key = urllib.unquote(handler.path[8:])
        return self.todos[key] if key in self.todos else None

    def set_task(handler):
        key = urllib.unquote(handler.path[8:])
        payload = handler.get_payload()
        self.todos[key] = payload
        return self.todos[key]

    def delete_task(handler):
        key = urllib.unquote(handler.path[8:])
        del self.todos[key]
        return True  # anything except None shows success

    def rest_call_json(url, payload=None, with_payload_method='PUT'):
        'REST call with JSON decoding of the response and JSON payloads'
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