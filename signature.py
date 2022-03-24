
import fdh
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import sys

def signature():
    plaintext = sys.argv[1]
    print ('要签名的数据为:', plaintext)
    plaintext = str.encode(plaintext)
    message = fdh.fdh(plaintext, 600)
    print(f'使用FDH获得的hash数据为: {message}')
    message = str.encode(message)
    key = RSA.import_key(open('private.pem').read())
    h = SHA256.new(message)
    signature = pkcs1_15.new(key).sign(h)
    print(f'生成的签名为: {signature}')
signature()