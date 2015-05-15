"""

Encrypt-Decrypt message with XOR
Proof of concept by Karlheinz Niebuhr

"""
import random
import string


def xor(a,b):
	bits = ''
	if not len(a) == len(b):
		return 'not equal length'

	for i in range(len(a)):
		if a[i] != b[i]:
			bits += '1'
		else:
			bits += '0'
	return bits



def toBin(string):
	return ''.join('{:08b}'.format(ord(c)) for c in string)

def toAsc(bin_text):
	return ''.join(chr(int(bin_text[i:i+8], 2)) for i in xrange(0, len(bin_text), 8))

message = raw_input('--> ')
print("Message: " + message)
message_bit_string = toBin(message)

key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(len(message)))
print("Key:", key)
key_bit_string = toBin(key)

encrypted_message = xor(message_bit_string, key_bit_string)
print("encrypted message in binary = " + encrypted_message + '\n')

print("decrypt message with the password")
decrypted_message = xor(encrypted_message, key_bit_string)
print("message decrypted = " + str(decrypted_message == message_bit_string))
print("message in binary is: " + '"' + str(decrypted_message) + '"\n\n')
print("message in Ascii is: " + '"' + toAsc(str(decrypted_message)) + '"\n\n')
