dslr-protocol
=============
Python protocol for controlling DSLR cameras over TCP

BYU-Idaho, CS-460, Networking Final Project </br>

How To
======
(ignoring Flask and assuming you have a DSLR camera)
Requirements:
DSLR Camera (only tested with Nikon D3100) *NOTE: If you use a webcam you must have uvccapture installed and only capture will work (for now)*
USB cord
Linux computer with gphoto2
Python

1) Open 3 terminals in project directory
2) Terminal 1, Server: `python dslr-server.py 5555 $(hostname) /path/to/download/pic/`
3) Terminal 2, Camera Client: `python camera.py 5555 $(hostname) dslr` (or change dslr to webcam or picam)
4) Terminal 3, Controller Client (using Idle): `python`
<br>Load Module: `import controller`
<br>Take Picture: `reload(controller); controller.sendCommand("ctr cap")`
<br>Change f-stop: `reload(controller); controller.sendCommand("ctr apt 4")`
<br>Change ISO: `reload(controller); controller.sendCommand("ctr iso 1600")`
<br>Change Shutterspeed: `reload(controller); controller.sendCommand("ctr ssp 1")`

<br>Flask Screenshot (server currently off)
![Action Screenshot](/screenshot/screenshot.png?raw=true "Action Screenshot")
