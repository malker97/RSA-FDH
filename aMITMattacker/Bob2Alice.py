import socket

UDP_IP = "192.168.0.197"
ALICE_UDP_IP = "192.168.0.163"
ALICE_UDP_PORT = 5005
BOB_UDP_PORT = 5006
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, ALICE_UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)

    sock.sendto(data, (ALICE_UDP_IP, ALICE_UDP_PORT))
