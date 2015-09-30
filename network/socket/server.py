import socket

if __name__ == '__main__':
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind(('127.0.0.1',8989))
    socket.listen(5)

    while True:
        connect ,address = socket.accept()
        try:
            connect.settimeout(3)
            buf = connect.recv(1024)
            print 'Receive : '+buf
        except socket.timeout:
            print 'connect timeout'
        connect.close()
