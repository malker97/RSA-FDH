import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher

def encrypt(plaintext):
    print("明文: ",plaintext)
    plaintext = str.encode(plaintext)
    key = RSA.import_key(open('public.pem').read())
    cipher = PKCS1_cipher.new(key)
    ciphertext = base64.b64encode(cipher.encrypt(plaintext))
    print("密文:", ciphertext)
    return ciphertext

