# Local server chalao:  python run.py   ->  http://localhost:8000
import http.server, socketserver, webbrowser
PORT = 8000
class H(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map, ".task": "application/octet-stream", ".mjs": "text/javascript"}
with socketserver.TCPServer(("", PORT), H) as s:
    print(f"Open: http://localhost:{PORT}  (band karne ke liye Ctrl+C)")
    webbrowser.open(f"http://localhost:{PORT}")
    s.serve_forever()
