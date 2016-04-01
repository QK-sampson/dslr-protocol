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
BUFSIZE = 4096
writePath = 'flask/templates/'

def recvPic(conn, data2):
    ctrEvent = data2.partition(" ")[2]
    print " DATA: ", data2
    #conn.sendall(ctrEvent)
    writeFile = open(writePath+'pic.jpg', 'w')
    picData = conn.recv(BUFSIZE)
    writeFile.write(picData)
    writeFile.close()
    conn.sendall('ctr rcv img')
#args
if len(sys.argv) >= 2:
    PORT = int(sys.argv[1])
if len(sys.argv) == 3:
    HOST = int(sys.argv[2])
if len(sys.argv) == 4:
    writePath = sys.argv[3]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORT))
except socket.error as e:
    print 'ERROR: Failed to bind on port ', PORT
    #os.system("fuser 5555/tcp")
    #s.bind((HOST, PORT))
print 'Listening on port ', PORT, 'in', writePath
s.listen(1)

while 1:
    conn, addr = s.accept()
    print 'Connected by', addr
    data = conn.recv(BUFSIZE)
    print 'DATA: ',data
    
    conn2, addr2 = s.accept()
    print 'Connected by', addr2
    data2 = conn2.recv(BUFSIZE)
    print 'DATA2: ',data2
    
    if not data or not data2: break
    #read request line
    #command = data.partition(" ")[0]
    command = data.split(' ')[0]
    #command2 = data2.partition(" ")[0]
    command2 = data2.split(' ')[0]

    if command2 == 'ctr':#two is the ctr
        option2 = data2.split(' ')[1]
        option = data2.split(' ')[1]#cam

        if command2 == 'ctr' and option2 != 'cap':#option given by ctr
            #value2 = data2.split(' ')[2]
            conn.sendall(data2)#send option to cam
        elif command2 == 'ctr' and option2 == 'cap':#take a pictaa
            conn.sendall(data2)
        elif option == 'pic':
            recvPic(conn, data2)
        else:
            print 'not yet implemented'
        result = conn.recv(BUFSIZE)#send cam result to ctr
        print 'RESULT: ', result
        conn2.sendall(result)

    elif command == 'ctr':#one is the ctr
        option = data.split(' ')[1]
        option2 = data2.split(' ')[1]

        if command == 'ctr' and option != 'cap':
            #value =  data.split(' ')[2]
            conn2.sendall(data)
        elif command == 'ctr' and option == 'cap':#take a pictaa
            conn2.sendall(data)
        elif option2 == 'pic':
            recvPic(conn2, data)
        else:
            print 'not yet implemented'
        result = conn2.recv(BUFSIZE)
        conn.sendall(result)
        print 'RESULT: ', result
    
    #conn.sendall('data here')
    conn.close()
