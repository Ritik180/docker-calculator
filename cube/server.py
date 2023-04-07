from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        if self.path == '/cube':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            length = int(self.headers['Content-length'])
            data = self.rfile.read(length).decode('utf-8')
            number = int(cgi.parse_qs(data)['number'][0])
            cube = number ** 3
            self.wfile.write(str(cube).encode('utf-8'))
        else:
            self.send_error(404)

server = HTTPServer(('0.0.0.0', 80), RequestHandler)
server.serve_forever()
