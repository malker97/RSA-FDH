import socket
# 这个文件会生成假的ciphertext，明文内容为NGLITSREALBOB

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
    fake_data = b'Qbi9R2AjTa07/G1Xna6rgI6VD/NrToI6O43nA2kEq1SyYeDF6/G2U04jvqZINk1nl/9AD7oGBIGjkRtTmYDwyMRTkSMg9JO9CByrJhel4WgLRJWipjEiihIe3Pl+QQGUuI16n+Hu84BxLfh7zd49HdtboFRP27Q2y2NPquzt1gM=GsCeSaUtweA07I7cUUKxJ22TB3+hQWaS72lSChEie7csPigioCmeKJ5CmeDsjWzgRtcuP3zm9l63w4QFQ/62pzICEgTiZJ0Cdf9OmTj7esTcBDJAojtHxwl0oWjD4HyzMU+a17GsjAdDbNDi9hMLdTPUJHFOVNRljNqAdZag9nk='
    sock.sendto(fake_data, (ALICE_UDP_IP, ALICE_UDP_PORT))
