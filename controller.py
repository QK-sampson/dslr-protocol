import socket

HOST = 'howtoterminal.com'
PORT = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sendCommmand(command)
  s.connect((HOST, PORT))
  #s.sendall('ctr cap')
  s.sendall(command)
  s.close()