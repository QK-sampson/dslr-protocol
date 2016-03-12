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
import os

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
    #os.system("fuser 5555/tcp")
    #s.bind((HOST, PORT))
print 'Listening on port ', PORT
s.listen(1)

while 1:
    conn, addr = s.accept()
    print 'Connected by', addr
    data = conn.recv(1024)
    print data
    
    conn2, addr2 = s.accept()
    print 'Connected by', addr
    data2 = conn2.recv(1024)
    print data2
    
    if not data or not data2: break
    print "Datas: ", data
    print "Datas2: ", data2
    #read request line
    command = data.partition(" ")[0]
    command2 = data2.partition(" ")[0]
    if command == "cam":
        ctrEvent = data2.partition(" ")[2]
        print "PArtition ", ctrEvent, " Whole ", data2
        conn.sendall(ctrEvent)
    elif command2 == "cam":
        ctrEvent = data.partition(" ")[2]
        print "PArtition ", ctrEvent, " Whole ", data
        conn2.sendall(ctrEvent)
    #requestMethod = requestLine.split(' ')[0]
    #requestObject = requestLine.split(' ')[1]
    #httpVersion = requestLine.split(' ')[2]
    
    #conn.sendall('data here')
    conn.close()
