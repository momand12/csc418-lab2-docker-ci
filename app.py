from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello! This is Hamad's Docker container - BSE7_60")

HTTPServer(("", 8080), Handler).serve_forever()
