from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format=' %(message)s')



class SimplifiedHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

        response = b'Hello, world!'
        self.wfile.write(response)
    
httpd = HTTPServer(('localhost', 8008), SimplifiedHTTPRequestHandler)
logging.info('\n🚀 Started server on 8008!')

httpd.serve_forever()

