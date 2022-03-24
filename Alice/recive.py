import socket
import decrypt
import send

UDP_IP = "192.168.0.163"
UDP_PORT = 5005
BOB_UDP_PORT = 5006
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)
    ciphertext = decrypt.decrypt(data)
    plaintext = ciphertext.decode('utf-8')
    print(f"\033[32mPlaintext:{plaintext}\033[0m")
    send.send(plaintext)
