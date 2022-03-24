import socket
import decrypt
import send

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
BOB_UDP_PORT = 5006
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)
    ciphertext = decrypt.decrypt(data)
    ciphertext = ciphertext.decode('utf-8')
    print("Ciphertext: ",ciphertext)
    send.send(ciphertext)
