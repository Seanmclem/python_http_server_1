from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format=' %(message)s')

# Define routes
def handle_home(handler:BaseHTTPRequestHandler):
    handler.send_response(200)
    handler.end_headers()
    handler.wfile.write(b"Home route")

def handle_home_post(handler:BaseHTTPRequestHandler):
    handler.send_response(200)
    handler.end_headers()
    handler.wfile.write(b"Home route POST")

def handle_about(handler:BaseHTTPRequestHandler):
    handler.send_response(200)
    handler.end_headers()
    handler.wfile.write(b"About route POSTY")

route_handlers = {
    '/': {
        'GET': handle_home,
        'POST': handle_home_post,
    },
    '/about': {
        'POST': handle_about
    }
}
# route_handlers.

class SimplifiedHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.handle_request('GET')
    def do_POST(self):
        self.handle_request('POST')
    
    def handle_request(self, method):
        handler_functions = route_handlers.get(self.path)
        if handler_functions:
            function = handler_functions.get(method)
            if function:
                function(self)
            else:
                self.send_response(405)
                self.end_headers()
                self.wfile.write(b'No Route Found')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Route not found')
    
httpd = HTTPServer(('localhost', 8008), SimplifiedHTTPRequestHandler)
logging.info('\n 🚀 Started Python server on 8008!')

httpd.serve_forever()

