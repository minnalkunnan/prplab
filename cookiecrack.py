import requests

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


adminString = 'admin\0\0\0\0\0\0\0\0\0\0' + str(chr(11))
finalString = 'aaaaaaaaaaa' + adminString + adminString
registerUser(finalString)
login(finalString)