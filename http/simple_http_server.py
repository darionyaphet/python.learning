import sys
import locale
import http.server
import socketserver

addr = len(sys.argv) < 2 and '127.0.0.1' or sys.argv[1]
port = len(sys.argv) < 3 and 8989 or locale.atoi(sys.argv[2])

handler = http.server.SimpleHTTPRequestHandler
server  = socketserver.TCPServer((addr, port), handler)
print ("HTTP server is at: http://%s:%d/" % (addr, port))
server.serve_forever()
