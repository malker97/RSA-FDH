# reference: https://www.geeksforgeeks.org/full-domain-hashing-with-variable-hash-size-in-python/
import binascii
from cmath import sin
from math import ceil
from hashlib import sha256

from numpy import sign
 
# Function to perform Full Domain
# Hash of 'message' using
# SHA512 with a digest of
# N bits
# 预设了hash的长度为2048
def fdh(message, n = 2048):
    result = []
    # Produce enough SHA512 digests
    # to make a composite digest
    # greater than or equal to N bits
    for i in range(ceil(n / 256)):
 
        # Append iteration count
        # to the message
        currentMsg = str(message) + str(i)
 
        # Add current hash to results list
        result.append(sha256((currentMsg).encode()).hexdigest())
 
    # Append all the computed hashes
    result = ''.join(result)
 
    # Obtaining binary representating
    resAsBinary = ''.join(format(ord(x), 'b') for x in result)
 
    # Trimming the hash to the
    # required size by taking
    # only the leading bits
    resAsBinary = resAsBinary[:n]
 
    # Converting back to the
    # ASCII from binary format
    return binascii.unhexlify('00%x' % int(resAsBinary, 2)).hex()
# sign1 = fdh(b'ItsBob', 600)
# sign2 = fdh(b'NGLITSREALBOB', 600)
# sign1 = str.encode(sign1)
# sign2 = str.encode(sign2)
# sign1 =  int.from_bytes(sign1, "big", signed="True")
# sign2 =  int.from_bytes(sign2, "big", signed="True")
# print("ItsBob", sign1)
# print("NGLITSREALBOB", sign2)
# # print(sign1*sign2)
# fake_sign = sign1 * sign2
# fake_sign = str(fake_sign)
# fake_sign = str.encode(fake_sign)
# print(fake_sign)
# # Driver code
# if __name__ == '__main__':
#     # Message to be hashed
#     message = "GeeksForGeeks"
 
#     # Generate a 600 bit
#     # hash using SHA256
#     print(fdh(message, 600))