import imp
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import fdh
import sys

def vertify(signature):
    # signature = b'\x9dB\x91\xde\x9b\xfd\xd2\x0c\x0e\xc6\x85\xe0\xc89K+r\xdb=uyd\x9cN\xb8\x91\xf9\xf7\xd0\x90\xeb\x8a\x18\xd2`\x89\x9e\xcd\xa3\x82\xc0\x8aG\x17*\xd4\xb7J\xaf~\x8c\xfaotk\t\xd9t!\x12z\x051n;\x17\xeb\x7fK\xddq\x1d\xba|\xe0\xd2D\x1d\x8a\x99F\x90\xe1\xb6Zv0F5\x90\x10\x87\x1f\x81\x9d\xc0\xbf\xf7\x95q\xd5y^8\x961:WW,\x0b\x97\xdd~\xa1<\x80\xebv\x0cG\xf5\x0ce\x7fPw\xdc'
    print(f'签名:{signature}')
    message = b'GeeksForGeeks'
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
