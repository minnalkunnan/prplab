import pad
import codecs
import binascii
from Crypto.Cipher import AES

def cbc_encrypt(key, plaintext, iv):
	encryptor = AES.new(key)
	paddedText = pad.pad(plaintext, 16)
	fullText = iv
	cText = iv
   
	for i in range(len(paddedText) / 16):
	   block = pad.XOR_text_key(paddedText[i * 16:16 + (i * 16)], cText)
	   cText = encryptor.encrypt(block)
	   fullText += cText
	return fullText

def cbc_decrypt(key, ciphertext, iv):
	decryptor = AES.new(key)
	fullText = ""
	
	if len(ciphertext) % 16 != 0:
	   print(len(ciphertext))
	   print("Error: Ciphertext not a multiple of block size")
	   return ciphertext
	
	for i in range((len(ciphertext) / 16) - 1, 0, -1):
	   block = ciphertext[i * 16:16 + (i * 16)]
	   text = decryptor.decrypt(block)
	   nextBlock = ciphertext[(i - 1) * 16:16 + ((i - 1) * 16)]
	   ptext = pad.XOR_text_key(text, nextBlock)
	   fullText = ptext + fullText
	
	unpaddedText = pad.unpad(fullText, 16)
	if unpaddedText == fullText:
	   print("Error: Unpadding invalid")
	   return ciphertext
	   
	return unpaddedText

def task3A():
   with open("Lab2.TaskIII.A.txt") as f:
      lines = f.readlines()

   fileLine = ""
   for line in lines:
      fileLine += pad.hex_to_ascii(pad.base64_to_hex(line.replace("\n", "")))
   print(cbc_decrypt("MIND ON MY MONEY", fileLine, "MONEY ON MY MIND"))
   #print(pad.hex_to_base64(pad.ascii_to_hex(cbc_encrypt("MIND ON MY MONEY", cbc_decrypt("MIND ON MY MONEY", fileLine, "MONEY ON MY MIND"), "MONEY ON MY MIND"))))

def task3B(cookie):
   dCook = "user=aaaaaaaaaaaa&UID=1&role=user"
   iv = "money on my mind"
   key = "mind on my money"
   
   #eCook = cbc_encrypt(key, dCook, iv)
   eCook = pad.hex_to_ascii(cookie)
   #print(pad.ascii_to_hex(eCook))
   iv = eCook[0:16]
   iv = pad.XOR_text_key(iv, "role=admin&user=")
   iv = pad.XOR_text_key(iv, "user=aaaaaaaaaaa")
   print("Old Cookie: " + pad.ascii_to_hex(eCook) + "\n")
   eCook = iv + eCook[16:len(eCook)]
   print("New Cookie: " + pad.ascii_to_hex(eCook) + "\n")
   cook = cbc_decrypt(key, eCook, iv)
   print(cook)

#task3A()
task3B("6d6f6e6579206f6e206d79206d696e64aaf8ce976310df50feef705b6251bdec7fc36cc1daba3d947eefaeb8d19f884fef7a0c6f58f12b3fbb52a5a5d6884902")
