from email.message import Message
from pydoc import plain
import socket
import sys
import signature


UDP_IP = "127.0.0.1"
UDP_PORT = 5005

MESSAGE = sys.argv[1]
plaintext = MESSAGE
plaintext = str.encode(plaintext)
MESSAGE = signature.signature(MESSAGE)
print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("Plaintext:", plaintext)
print("Signature: %s" % MESSAGE)
data_dict = {
  "plaintext": plaintext,
  "signature": MESSAGE,
}

data_string = str(data_dict)
data_bin = str.encode(data_string)

sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
sock.sendto(data_bin, (UDP_IP, UDP_PORT))