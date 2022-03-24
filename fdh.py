# reference: https://www.geeksforgeeks.org/full-domain-hashing-with-variable-hash-size-in-python/
import binascii
from math import ceil
from hashlib import sha256
 
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
 
# # Driver code
# if __name__ == '__main__':
#     # Message to be hashed
#     message = "GeeksForGeeks"
 
#     # Generate a 600 bit
#     # hash using SHA256
#     print(fdh(message, 600))