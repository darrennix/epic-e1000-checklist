#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys

class CORSHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow the page to load resources
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

port = 8090
server_address = ('', port)

httpd = HTTPServer(server_address, CORSHandler)
print(f"Server running at http://localhost:{port}")
print(f"View checklist at http://localhost:{port}/preview.html")
print("Press Ctrl+C to stop the server")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped")
    httpd.server_close()
