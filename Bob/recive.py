import socket
import verify
import ast

UDP_IP = "192.168.0.163"
UDP_PORT = 5006
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)
    # date 目前是bytes数据类型，所以需要重新转换回dict
    # data = data.decode("utf-8") 
    # data = ast.literal_eval(data)
    verify.vertify(data)
