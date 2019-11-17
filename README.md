# vm_ctrl_serv
Simple client/server written in python in order to send a keypress from a server to a client (virtual machine host to guest or vice versa)

Requirements:
pip install keyboard

Usage:
Run *ctrl_server.py* on a host/guest (virtual) machine from where you want your keypress to be sent to another machine.

Run *client.py* on a guest/host (virtual) machine where you'd like to the keypress being sent to.

Server example:
*python ctrl_server.py --port 50505 --server 0.0.0.0*

--port is the port where on the server machine the server side software is listening for incoming connections, --server specifies the network interface to bind to.

Client example:
*client.py --port 50505 --server 192.168.100.1*

--port is the listening port on the server machine, --server is the server address.

Currently supports only sending Control keypress. I initially wrote this tool for running a VoIP software (TeamSpeak / Discord) on a virtual machine, so there's a bit of isolation with regards the host machine.
