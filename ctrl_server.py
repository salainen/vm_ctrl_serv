from thread import start_new_thread
import time
import keyboard
import socket
import datetime
import argparse

# parse command line arguments:
parser = argparse.ArgumentParser(description='CTRL Server')
parser.add_argument('--port', action="store", dest="port", type=int, \
					required=True)
parser.add_argument('--server', action="store", dest="bind_addr", \
					type=str, required=True)

given_args = parser.parse_args()
PORT = given_args.port
HOST = given_args.bind_addr
CTRL_PRESSED = ''
DATA_TO_SEND = 'shite' #placeholder value until a client connects

def run_the_server(a):

    global HOST
    global PORT
    global CTRL_PRESSED
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    
    while True:
        time.sleep(0.05)
        conn, addr = s.accept()
        timestamp = datetime.datetime.now()
        print str(timestamp) + ': Client connection accepted ', addr
        while True:
			# main loop of the server
            try:
                DATA_TO_SEND = ''
				# ctrl is pushed:
                if CTRL_PRESSED:
                    DATA_TO_SEND = 'CTRL PRESSED'
				# if there's data (mainly just ctrl pressed,) send it
                if len(DATA_TO_SEND) >= 1:
                    conn.send(DATA_TO_SEND)
                    time.sleep(0.2)
                    DATA_TO_SEND = ''
                else:
					# otherwise just send hearbeat data
                    DATA_TO_SEND = 'heartbeat'
                    conn.send(DATA_TO_SEND)
                    time.sleep(0.01)
                    DATA_TO_SEND = ''
                    #break
            except socket.error, msg:
				# handle client disconnect:
                print str(timestamp) + ': Client connection closed', addr
                break
    conn.close()


def key_press_monitor(a):
        
        
        global CTRL_PRESSED
        while True:
            time.sleep(0.01)
            if CTRL_PRESSED:
                time.sleep(0.1)
                CTRL_PRESSED = False

# could be cleaner, passing a dummy value to the new threads and starting them:
start_new_thread(key_press_monitor,(99,))
start_new_thread(run_the_server,(99,))

while True:
		# main loop:
        timestamp = datetime.datetime.now()
        if keyboard.is_pressed('ctrl'):
            CTRL_PRESSED = True
            print str(timestamp) + ": CTRL_PRESSED"
            time.sleep(0.01)
        time.sleep(0.1)