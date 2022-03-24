from email.message import Message
from pydoc import plain
import socket
import sys
import signature

def send(ciphertext):
  UDP_IP = "192.168.0.197"
  UDP_PORT = 5006

  MESSAGE = ciphertext
  plaintext = MESSAGE
  plaintext = str.encode(plaintext)
  MESSAGE = signature.signature(MESSAGE)
  print("UDP target IP: %s" % UDP_IP)
  print("UDP target port: %s" % UDP_PORT)
  print("message: %s" % MESSAGE)
  data_dict = {
    "plaintext": plaintext,
    "signature": MESSAGE,
  }

  data_string = str(data_dict)
  data_bin = str.encode(data_string)
  # data_dict = ast.literal_eval(data_string)

  sock = socket.socket(socket.AF_INET, # Internet
                          socket.SOCK_DGRAM) # UDP
  sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))