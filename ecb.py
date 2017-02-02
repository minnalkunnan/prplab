import pad
from Crypto.Cipher import AES

def ecb_encrypt(key, plaintext, blocksize):
	encryptor = AES.new(key)

	paddedText = pad(plaintext, blocksize)

def ecb_decrypt():
	return None

ecb_encrypt("California Love!", "Message text", 10)