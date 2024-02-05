import http.server
import socketserver
import os

from http import HTTPStatus

if 'MESSAGE' in os.environ.keys():
    message = os.environ['MESSAGE']
else:
    message = 'Hello world!'

if "PYTHON_PORT" in os.environ.keys():
    port = int(os.environ['PYTHON_PORT'])
else:
    port = 8000

class SomeHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.close_connection = True

        self.send_response(HTTPStatus.OK)   
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write("<DOCTYPE html>".encode())
        self.wfile.write(f"<html><body>{message}</body></html>".encode())
        self.wfile.flush()
        return
        

with socketserver.TCPServer(("", port), SomeHandler) as httpd:
    print("serving at port", port)
    httpd.serve_forever()