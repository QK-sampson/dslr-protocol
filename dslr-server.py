#############################################################################
# Program:
#    Lab Final Project, Computer Communication and Networking
#    Brother Jones, CS 460
# Author:
#    Adam Quinton
# Summary:
#    DSLR Protocol Server
#############################################################################
import socket
import sys #command line args

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 5555              # Default port if none specified in args

if len(sys.argv) >= 2:
    PORT = int(sys.argv[1])

if len(sys.argv) == 3:
    HOST = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORT))
except socket.error as e:
    print 'ERROR: Failed to bind on port ', PORT
    
print 'listening on port ', PORT
s.listen(1)

while 1:
    conn, addr = s.accept()
    print 'Connected by', addr
    data = conn.recv(1024)
    print data
    
    if not data: break
    #read request line
    #requestLine = data.partition("\n")[0]
    #requestMethod = requestLine.split(' ')[0]
    #requestObject = requestLine.split(' ')[1]
    #httpVersion = requestLine.split(' ')[2]
    
    conn.sendall('data here')
    conn.close()
