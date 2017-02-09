def ascii_to_hex ( ascii_text ):
   hex_text = ascii_text.encode("hex");
   #print(hex_text)
   return hex_text
   
def hex_to_ascii ( hex_text ):
   ascii_text = hex_text.decode("hex");
   #print(ascii_text)
   return ascii_text
   
def hex_to_base64 ( hex_text ):
   base64_text = hex_text.decode("hex").encode("base64");
   #print(base64_text)
   return base64_text
   
def base64_to_hex ( base64_text ):
   hex_text = base64_text.decode("base64").encode("hex");
   #print(hex_text)
   return hex_text
   
def pad(text, blocksize):
   if blocksize > 1:
      padding = blocksize - (len(text) % blocksize)
      for i in range(padding):
        text += str(chr(padding))
      
   return text

def XOR_text_key ( text , key ):
   main_key = key
   new_text = ""
   while len(main_key) < len(text):
      main_key += key
   main_key = main_key[:len(text)]
   
   hex_text = ascii_to_hex(text)
   hex_key = ascii_to_hex(main_key)
   
   hex_new_text = hex(int(hex_text, 16) ^ int(hex_key, 16))
   hex_new_text = hex_new_text[2:len(hex_new_text)-1]

   if len(hex_new_text) % 2 != 0:
      hex_new_text = "0" + hex_new_text
      
   new_text = hex_to_ascii(hex_new_text)
   return new_text
   
def testPad():
   i = 1
   for i in range(15):
      message = "Hello I'm a message"
      print("Padding message " + message + " with length of " + str(len(message)))
      paddedText = pad(message, i)
      paddedTextHex = ascii_to_hex(paddedText)
      print("Padded with blocksize of " + str(i) + " results in\n" + paddedTextHex)

def unpad(text, blocksize):
   count = 0
   pad = 0
   if len(text) % blocksize != 0:
      print("Invalid Padding")
      return text
   
   for i in range(len(text) - 1, -1, -1):
      if i == len(text) - 1:
         pad = ord(text[i])
         count = pad - 1
         #print(count)
      elif ord(text[i]) == pad:
         count -= 1
      else:
         print(ord(text[i]))
         print("Invalid Padding")
         return text
      
      if count == 0:
         return text[:len(text) - pad]
         
   return text
   
def unpadANSI(text, blocksize):
   count = 0
   pad = 0
   if len(text) % blocksize != 0:
      print("Invalid Padding")
      return text
   
   for i in range(len(text) - 1, -1, -1):
      if i == len(text) - 1:
         pad = ord(text[i])
         count = pad - 1
         #print(count)
      elif ord(text[i]) == 0:
         count -= 1
      else:
         print(ord(text[i]))
         print("Invalid Padding")
         return text
      
      if count == 0:
         return text[:len(text) - pad]
         
   return text
   
def padANSI(text, blocksize):
   if blocksize > 1:
      padding = blocksize - (len(text) % blocksize)
      for i in range(padding - 1):
        text += str(chr(0))
      text += str(chr(padding))
   return text
   
"""   
paddedText = pad("Hello I'm a message!", 10)
paddedTextHex = ascii_to_hex(paddedText)
print(paddedTextHex)
unpadText = unpad(paddedText, 10)
unpaddedTextHex = ascii_to_hex(unpadText)

print(paddedTextHex)
print(unpadText)
print(unpaddedTextHex)
"""

"""
paddedText = padANSI("Hello I'm a message!", 10)
paddedTextHex = ascii_to_hex(paddedText)
print(paddedTextHex)
unpadText = unpadANSI(paddedText, 10)
unpaddedTextHex = ascii_to_hex(unpadText)

print(paddedTextHex)
print(unpadText)
print(unpaddedTextHex)
"""
