from flask import Flask
from flask import request, render_template
import os
import socket
import datetime
import controller

app = Flask(__name__)
HOST = 'howtoterminal.com'
PORT = 5555

print "STARTED connection on PORT ", PORT

@app.route("/") # what URL should trigger the function
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title' : 'DSLR PROTOCOL',
        'time': timeString
    }
    return render_template('main.html', **templateData)

@app.route('/dslr', methods=['POST', 'GET'])
def sendCommand():
    print "SENDCOMMAND"
    if request.method == 'POST':
        action = request.form['action']
        print action
        reload(controller)
        controller.sendCommand(action)
        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.connect((HOST, PORT))
        #s.sendall('ctr cap')
        #s.close()
        return hello()
    else:
        print "not post"
        return 'NOT POST'
    
if __name__ == "__main__": # only run if not used as an import
    app.run(host='0.0.0.0', port=5000, debug=True) # all 0s means listen on all public IPs     
