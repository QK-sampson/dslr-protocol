import socket
import sys

HOST = 'howtoterminal.com'
PORT = 5555
BUFSIZE = 4096

def sendCommand(command, HOST, PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'PORT: ', PORT, ', HOST: ', HOST
    s.connect((HOST, PORT))
    s.sendall(command)
    s.close()
