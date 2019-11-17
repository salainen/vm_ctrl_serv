import socket
import keyboard
import time
import argparse
import datetime

# parse command line arguments:
parser = argparse.ArgumentParser(description='CTRL Client')
parser.add_argument('--port', action="store", dest="port", type=int, required=True)
parser.add_argument('--server', action="store", dest="serv_addr", type=str, required=True)
given_args = parser.parse_args()
PORT = given_args.port
HOST = given_args.serv_addr

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
	# main loop:
    timestamp = datetime.datetime.now()
    time.sleep(0.1)
    data = s.recv(1024)
    if not "heartbeat" in data:
        print (str(timestamp) + ": " + repr(data))
    
	# we didn't receive "CTRL PRESSED" from the server, release button:
    if "heartbeat" in data:
        keyboard.release('ctrl')
    
	# server sent us "CTRL PRESSED", press the button on this machine:
    if data == 'CTRL PRESSED':
        keyboard.press('ctrl')
    
    if data == '':
        # server was shutdown, exit gracefully:
        s.close
        print str(timestamp) + ": server closed the connection"
        break
s.close()