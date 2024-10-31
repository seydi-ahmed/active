import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

# Configuration du serveur
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
