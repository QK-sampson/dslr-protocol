from flask import Flask
from flask import request
import os
import socket

app = Flask(__name__)
HOST = 'howtoterminal.com'
PORT = 5555

print "STARTED connection on PORT ", PORT

@app.route("/") # what URL should trigger the function
def hello():
    return "Hello World!"

@app.route('/dslr', methods=['POST', 'GET'])
def sendCommand():
    print "SENDCOMMAND"
    if request.method == 'POST':
        action = request.form['action']
        print action
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.sendall('ctr cap')
        s.close()
        return hello()
    else:
        print "not post"
        return 'NOT POST'
    
    if __name__ == "__main__": # only run if not used as an import
        app.run(host='0.0.0.0', port=5000, debug=True) # all 0s means listen on all public IPs     
