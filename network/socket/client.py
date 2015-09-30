import socket
import time

if __name__ == '__main__':
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    socket.connect(('127.0.0.1',8989))
    time.sleep(3)
    socket.send(str(time.time()))
    socket.close()
