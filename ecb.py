import pad
import codecs
import binascii
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
	   print(len(ciphertext))
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
def task2A():
   with open("Lab2.TaskII.A.txt") as f:
      lines = f.readlines()

   fileLine = ""
   for line in lines:
      fileLine += pad.hex_to_ascii(pad.base64_to_hex(line.replace("\n", "")))
   print(ecb_decrypt("CALIFORNIA LOVE!", fileLine, 16))
   
   #print(len(fileLine))
   #print(pad.hex_to_base64(pad.ascii_to_hex(ecb_encrypt("CALIFORNIA LOVE!", ecb_decrypt("CALIFORNIA LOVE!", fileLine, 16), 16))))
   

def task2B():
   with open("Lab2.TaskII.B.txt") as f:
      lines = f.readlines()

   fileLine = ""
   maxEqCount = -1
   bestLine = ""
   blocksize = 32
   for line in lines:
      curEqCount = 0
      trimLine = line[108:]
      lineBlocks = []
      for i in range(0, len(trimLine) / blocksize):
         lineBlocks.append(trimLine[i * blocksize:(i*blocksize) + blocksize])
      for i in range(0, len(lineBlocks)):
         for j in range(i + 1, len(lineBlocks)):
            if lineBlocks[i] == lineBlocks[j]:
               curEqCount += 1
      
      #print(curEqCount)
      if curEqCount > maxEqCount:
         maxEqCount = curEqCount
         bestLine = line
      #print(line[108:])
   
   #print(maxEqCount)
   #print(bestLine)
   asciiLine = pad.hex_to_ascii(bestLine.replace("\n",""))
   
   #print(bestLine)
   #print(asciiLine.decode("cp852"))
   image = open("OutputImage.bmp", "wb")
   image.write(binascii.unhexlify(bestLine.replace("\n", "")))
   image.close()
   
   #f = open('OutputImage.txt', 'r')
   #print(f.read())
   #f.close()
   #print(binascii.unhexlify(bestLine.replace("\n", "")))

   #fo = codecs.open('OutputImage.jpg', 'r', 'ascii')
   #lines = fo.readlines()
   #for line in lines:
      #print(line)
#task2A()
task2B()
