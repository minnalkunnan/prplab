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
   padding = blocksize - (len(text) % blocksize)

   for i in range(padding):
      text += str(chr(padding))
      
   return text

def unpad(text, blocksize):
   count = 0
   pad = 0
   if len(text) % blocksize != 0:
      print("Invalid Padding")
      return None
   
   for i in range(len(text) - 1, -1, -1):
      if i == len(text) - 1:
         pad = ord(text[i])
         count = pad - 1
      
      if ord(text[i]) == pad:
         count -= 1
      else:
         print("Invalid Padding")
         return None
      
      if count == 0:
         return text[:len(text) - pad]
         
   return None
   
paddedText = pad("Hello I'm a message", 8)
paddedTextHex = ascii_to_hex(paddedText)
print(paddedTextHex)
unpadText = unpad(paddedText, 8)
unpaddedTextHex = ascii_to_hex(unpadText)

print(paddedTextHex)
print(unpadText)
print(unpaddedTextHex)
