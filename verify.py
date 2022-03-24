import imp
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import fdh
import sys

def vertify(data):
    signature = data['signature']
    print(f'签名:{signature}')
    message = data['plaintext']
    print(f'原始数据: {message}')
    message = fdh.fdh(message,600)
    print(f'Hash后的原始数据: {message}')
    message = str.encode(message)
    key = RSA.import_key(open('public.pem').read())
    h = SHA256.new(message)
    try:
        pkcs1_15.new(key).verify(h, signature)
        print ("\033[32mOk\033[0m")
    except:
        print ("\033[31mError\033[0m")
