import socket

HOST = 'localhost'
PORT = 5555
BUFSIZE = 4096

if len(sys.argv) >= 2:
    PORT = int(sys.argv[1])

if len(sys.argv) >= 3:
    HOST = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'PORT: ', PORT, ', HOST: ', HOST

def sendCommand(command):
	s.connect((HOST, PORT))
	s.sendall(command)
#	result = s.recv(BUFSIZE)
#	print 'RESULT: ', result
	s.close()

def what():
  print "yo"
