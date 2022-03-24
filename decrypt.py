import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher

def decrypt(ciphertext):
    ciphertext = ciphertext.decode('utf-8')
    key = RSA.import_key(open('private.pem').read())
    cipher = PKCS1_cipher.new(key)
    plaintext = cipher.decrypt(base64.b64decode(ciphertext), 0)
    return plaintext
#  print(decrypt(b'Qbi9R2AjTa07/G1Xna6rgI6VD/NrToI6O43nA2kEq1SyYeDF6/G2U04jvqZINk1nl/9AD7oGBIGjkRtTmYDwyMRTkSMg9JO9CByrJhel4WgLRJWipjEiihIe3Pl+QQGUuI16n+Hu84BxLfh7zd49HdtboFRP27Q2y2NPquzt1gM=GsCeSaUtweA07I7cUUKxJ22TB3+hQWaS72lSChEie7csPigioCmeKJ5CmeDsjWzgRtcuP3zm9l63w4QFQ/62pzICEgTiZJ0Cdf9OmTj7esTcBDJAojtHxwl0oWjD4HyzMU+a17GsjAdDbNDi9hMLdTPUJHFOVNRljNqAdZag9nk='))