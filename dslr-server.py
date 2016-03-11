#############################################################################
# Program:
#    Lab PythonWebServer, Computer Communication and Networking
#    Brother Jones, CS 460
# Author:
#    Adam Quinton
# Summary:
#    Simple HTTP web server
#
#############################################################################
import socket
import sys #command line args
import os

# Return content-type based on file name
def getContentType(filename):
    filename = filename.lower()
    if filename.endswith(".html") or filename.endswith(".htm"):
        return "text/html"
    elif filename.endswith(".css"):
        return "text/css"
    elif filename.endswith(".gif"):
        return "image/gif"
    elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        return "image/jpeg"
    elif filename.endswith(".txt"):
        return "image/txt"
    else:
        return "application/octet-stream"
        
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 6789              # Default port if none specified in args

if len(sys.argv) >= 2:
    PORT = int(sys.argv[1])

if len(sys.argv) == 3:
    HOST = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORT))
except socket.error as e:
    print 'failed to bind on port ', PORT
    PORT += 1 # increment if port failed to bind
    print 'trying higher port ', PORT
    s.bind((HOST, PORT))

print 'listening on port ', PORT
s.listen(1)

while 1:
    conn, addr = s.accept()
    print 'Connected by', addr
    data = conn.recv(1024)
    print data
    
    if not data: break
    #read request line
    requestLine = data.partition("\n")[0]
    requestMethod = requestLine.split(' ')[0]
    requestObject = requestLine.split(' ')[1]
    httpVersion = requestLine.split(' ')[2]
    
    status = "200 OK"
    
    if "/" in requestObject and requestObject[0] == '/' and len(requestObject) > 1: # strip first slash
        filename = requestObject.split('/', 1)[1]
    else: # give file in current directory
        filename = requestObject
        
    if filename[-1] == '/':
        if len(filename) > 1:
            filename += "index.html"
        else:
            filename = "index.html"

    contentType = getContentType(filename)
    
    print 'Opening file: ', filename
    
    page = ""
    try:
        with open(filename) as fn:
            content = fn.read() 
            #page = "".join(str(x) for x in content)
            page = content
    except IOError as e:
        print "I/O Error: ({0}): {1} for {2}".format(e.errno, e.strerror, filename)
        status = "404 Not Found"
    
    conn.sendall('HTTP/1.0 ' + status + '\n'
                 + 'Content-type: ' + contentType + '\r\n\r\n'
                 + page
                 + '\r\n\r\n')
    conn.close()

