# A cipher has a:
# - message
# - key
# - cypher text
#
# To be valid the following condition must be true:
#
#   E(k, D(k, c)) = m

import random
import string
import binascii
import uu

## XOR by Kenny Meyer

# Define a message
message = "Python is so snaky and nice and cozy"
# Define a random key with the same length
key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(len(message)))
print "Message:", message
print "Key:", key

# Convert the message and key to binary
# Shamelessly stolen from Karl ;)
def toBin(string):
	return ''.join('{:08b}'.format(ord(c)) for c in string)

def toAsc(bin_text):
	return ''.join(chr(int(bin_text[i:i+8], 2)) for i in xrange(0, len(bin_text), 8))

key = toBin(key)
message = toBin(message)
# For debugging purposes
#print toBin(message)
#print toBin(key)
#print "Same length: ", len(toBin(message)) == len(toBin(key))

# XOR the message and key
# Exclusive disjunction or exclusive or is a logical operation that outputs true whenever both inputs differ (one is true, the other is false)
# http://en.wikipedia.org/wiki/Exclusive_or
def xor(message, key):
    if len(message) != len(key):
        return "don't match in size"

    bits = ''

    for i in range(len(message)):
        if message[i] != key[i]:
            bits += '1'
        else:
            bits += '0'

    return bits

# The output is the cypher text
cypher = xor(message, key)

# Proof that cypher is valid
print "Cypher:", cypher
print xor(cypher, key) == message
