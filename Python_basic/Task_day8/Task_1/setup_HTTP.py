import time
from http.server import HTTPServer, CGIHTTPRequestHandler

time.sleep(10)
port = 80
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print('Starting simple httpd on port: ' + str(httpd.server_port))
httpd.serve_forever()
