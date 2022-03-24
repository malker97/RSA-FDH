import socket
# 这个文件中会发送假的签名信息给Bob，来测试Bob端的验证
UDP_IP = "192.168.0.197"
ALICE_UDP_IP = "192.168.0.163"
BOB_UDP_IP = "192.168.0.163"
ALICE_UDP_PORT = 5005
BOB_UDP_PORT = 5006
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, BOB_UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)
    sock.sendto(data, (BOB_UDP_IP, BOB_UDP_PORT))
