import os
import socket

HOST = 'howtoterminal.com'
PORT = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('cam')

data = s.recv(1024)
print data

if data == "cap":
    os.system("gphoto2 --capture-image")

s.close()

#print subprocess.Popen("gphoto2 --capture-image", shell=True, stdout=subprocess.PIPE)
