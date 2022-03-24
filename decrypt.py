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