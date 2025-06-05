import http.server
import socketserver
import json

PORT = 8000


class MyHandler(http.server.SimpleHTTPRequestHandler):
    """Custom request handler for the API."""

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/":
            self._send_response(200, "text/plain",
                                b"Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_response(
                200, "application/json", json.dumps(data).encode('utf-8')
            )
        elif self.path == "/status":
            self._send_response(200, "text/plain", b"OK")
        else:
            self._send_response(404, "text/plain", b"Endpoint not found")

    def _send_response(self, status_code, content_type, content):
        """Send response with given status, content type, and content."""
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()
        self.wfile.write(content)


def run_server():
    """Start the HTTP server."""
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    run_server()
