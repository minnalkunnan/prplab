import pad
from Crypto.Cipher import AES

def ecb_encrypt(key, plaintext, blocksize):
	encryptor = AES.new(key)
	paddedText = pad.pad(plaintext, blocksize)
	fullText = ""
	for i in range(len(paddedText) / blocksize):
	   #print(pad.ascii_to_hex(paddedText[i * blocksize:blocksize + (i * blocksize)]) + '\n')
	   block = paddedText[i * blocksize:blocksize + (i * blocksize)]
	   ctext = encryptor.encrypt(block)
	   #print(pad.ascii_to_hex(ctext))
	   fullText += ctext
	return fullText

def ecb_decrypt(key, ciphertext, blocksize):
	decryptor = AES.new(key)
	#paddedText = pad.pad(plaintext, blocksize)
	fullText = ""
	
	if len(ciphertext) % blocksize != 0:
	   print("Error: Ciphertext not a multiple of block size")
	   return ciphertext
	
	for i in range(len(ciphertext) / blocksize):
	   #print(pad.ascii_to_hex(paddedText[i * blocksize:blocksize + (i * blocksize)]) + '\n')
	   block = ciphertext[i * blocksize:blocksize + (i * blocksize)]
	   ptext = decryptor.decrypt(block)
	   #print(pad.ascii_to_hex(ctext))
	   fullText += ptext
	
	unpaddedText = pad.unpad(fullText, blocksize)
	if unpaddedText == fullText:
	   print("Error: Unpadding invalid")
	   return ciphertext
	   
	return unpaddedText

#cText = ecb_encrypt("California Love!", "Message text over sixteen bytes", 16)
#print(pad.ascii_to_hex(cText))

#pText = ecb_decrypt("California Love!", cText, 16)
#print(pad.ascii_to_hex(pText))
#print(pText)

#decodedLines = []
with open("Lab2.TaskII.A.txt") as f:
   lines = f.readlines()
   
print(lines)
for line in lines:
   print(pad.base64_to_hex(line.replace("\n", "")))
for line in lines:
   print(ecb_decrypt("CALIFORNIA LOVE!", line.replace("\n", ""), 16))

   
   
   
   
   
