import os
import socket

HOST = 'howtoterminal.com'
PORT = 5555

while (1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall('cam')# I am a camera

    data = s.recv(1024)
    print 'Received: ', data

    action = data.split(' ')[0]
    if (data.count(' ') >= 1):
        value = data.split(' ')[1]
    else:
        value = ''
        
    if action == "cap":
        os.system("gphoto2 --capture-image")
    elif action == "ssp":
        os.system("gphoto2 --set-config /main/capturesettings/shutterspeed " + value)

    s.close()

#print subprocess.Popen("gphoto2 --capture-image", shell=True, stdout=subprocess.PIPE)
