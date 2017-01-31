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

def unpad():
   return None
   
paddedText = pad("Hello I'm a message", 8)
paddedTextHex = ascii_to_hex(paddedText)
print(paddedTextHex)
