import requests
import pad
import codecs
import binascii
from Crypto.Cipher import AES

def registerUser(username):
	payload = {'user':username, 'password':'p' }
	r = requests.post("http://localhost:8080/register", data=payload)
	print(r.text)
	return r

def login(username):
	s = requests.session()
	payload = {'user':username, 'password':'p'}
	r = s.post("http://localhost:8080/", data=payload)
	print(r.text)
	print(s.cookies)

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
#   cook = cbc_decrypt(key, eCook, iv)
 #  print(cook)

task3B('8bc0ea7001dab6e513b75d2a620b4e7c4b6911a692260c11f0bcc7d74c2d2a63c5fead5b9d74bfd66e73c5706ebb9e4dafd9a16642f1baf81e4457a90e1e3482')