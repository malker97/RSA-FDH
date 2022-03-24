from email.message import Message
import socket
import sys
import signature

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
# MESSAGE = b"Hello, World!"

MESSAGE = sys.argv[1]
MESSAGE = signature.signature(MESSAGE)
print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))