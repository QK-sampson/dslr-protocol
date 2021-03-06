import os
import socket
import sys

HOST = 'howtoterminal.com'
PORT = 5555
BUFSIZE = 4096
CAMTYPE = 'dslr' #dslr, webcam, picam
#variables are loaded according to camera type
#arguments are parsed and added before execution
if len(sys.argv) >= 2:
    PORT = int(sys.argv[1])

if len(sys.argv) >= 3:
    HOST = sys.argv[2]

if len(sys.argv) == 4:
    if sys.argv[3] == 'dslr' or sys.argv[3] == 'webcam' or sys.argv[3] == 'picam':
        CAMTYPE = sys.argv[3]

if CAMTYPE == 'dslr':#initializers
    import dslr
    command = dslr
    os.system(command.bin+command.set+command.quality+command.basic)
    os.system(command.bin+command.set+command.shutterspeed+'=20')
    #os.system(command.bin+command.get+command.iso)
    #os.system(command.bin+command.get+command.fstop)
    #os.system(command.bin+command.get+command.shutterspeed)
elif CAMTYPE == 'webcam':
    import webcam
    command = webcam
elif CAMTYPE == 'picam':
    import picam
    command = picam

    print 'PORT: ', PORT, ', HOST: ', HOST, ', CAMTYPE: ', CAMTYPE
while (1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print 'Sending "cam ', CAMTYPE, '"'
    s.sendall('cam '+CAMTYPE)# I am a camera
    data = s.recv(BUFSIZE)
    print 'Received: ', data

    clientType = data.split(' ')[0]
    if (data.count(' ') >= 1):
        action = data.split(' ')[1]
        if (data.count(' ') >= 2):
            value = data.split(' ')[2]
        else:
            value = ''
    else:
        print 'ERROR: not enough args from other client'

    if action == "cap":
        upFile = "pic.jpg"
        os.system(command.bin+command.capture+command.filename+upFile)
        #upload picture
        #compress
        os.system('dpkg -s imagemagick > /dev/null && convert -resize 800x -strip -interlace Plane -quality 50% '+upFile+' '+upFile)
        print 'Sending file: ', upFile
        bytes = open(upFile).read()
        totalBytes =  str(len(bytes))
        print totalBytes
        s.sendall('cam '+totalBytes+' '+'pic')
        s.sendall(bytes)
    elif action == "iso":
        #set ISO
        print 'attempting to set iso to '+value
        os.system(command.bin+command.set+command.iso+command.getISO(int(value)))
        s.sendall('cam iso '+value)
    elif action == "apt":
        #set fstop
        os.system(command.bin+command.set+command.fstop+command.getFstop(float(value)))
        s.sendall('cam apt '+value)
    elif action == "ssp":
        #set shutterspeed
        os.system(command.bin+command.set+command.shutterspeed+command.getShutter(float(value)))
        s.sendall('cam ssp '+value)

    s.close()
