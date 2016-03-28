import os
import socket

HOST = 'howtoterminal.com'
PORT = 5555
BUFSIZE = 4096
#variables are loaded according to camera type
#arguments are parsed and added before execution

while (1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print 'Connection:', s
    s.sendall('cam')# I am a camera
     
    data = s.recv(BUFSIZE)
    print 'Received: ', data

    action = data.split(' ')[0]
    if (data.count(' ') >= 1):
        value = data.split(' ')[1]
    else:
        value = ''

    if action == "cap":
        os.system("uvccapture -m -x120 -B50 -q30 -opic.jpg")
        #upload picture
        upFile = "pic.jpg"
        #TODO: get huge files working
        bytes = open(upFile).read()
        print len(bytes)
        s.send(bytes)
        #os.system("scp pic.jpg pi@howtoterminal.com:~/public_html/dslr-protocol/pic.jpg")
    elif action == "iso":
        os.system("raspistill --width 200 --height 150 -v --nopreview -o pic.jpg " + value)
    
   # if action == "cap":
   #     os.system("gphoto2 --capture-image")
   # elif action == "ssp":
   #    os.system("gphoto2 --set-config /main/capturesettings/shutterspeed " + value)

    s.close()

#print subprocess.Popen("gphoto2 --capture-image", shell=True, stdout=subprocess.PIPE)
