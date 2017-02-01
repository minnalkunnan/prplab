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

def testPad():
   i = 1
   for i in range(15):
      message = "Hello I'm a message"
      print("Padding message " + message + " with length of " + str(len(message)))
      paddedText = pad(message, i)
      paddedTextHex = ascii_to_hex(paddedText)
      print("Padded with blocksize of " + str(i) + " results in\n" + paddedTextHex)

def unpad():
   return None
   
testPad()
print(pad("Message", 8))
