import socket

HOST = 'localhost'
PORT = 5555
BUFSIZE = 4096
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sendCommand(command):
	s.connect((HOST, PORT))
	#s.sendall('ctr cap')
	s.sendall(command)
#	result = s.recv(BUFSIZE)
#	print 'RESULT: ', result
	s.close()

def what():
  print "yo"
