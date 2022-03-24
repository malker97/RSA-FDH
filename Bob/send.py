
from pydoc import plain
import socket
import sys
import encrypt

UDP_IP = "192.168.0.197"
UDP_PORT = 5005

MESSAGE = sys.argv[1]
plaintext = MESSAGE
ciphertext = encrypt.encrypt(plaintext)
print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("Message: %s" % MESSAGE)
print("Ciphertext: %s" % ciphertext)


# data_dict = ast.literal_eval(data_string)

sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
sock.sendto(ciphertext, (UDP_IP, UDP_PORT))