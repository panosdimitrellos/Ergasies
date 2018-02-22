from string import maketrans 
def rot13_f(string):
	intab  = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	outtab = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
	rot13  = maketrans(intab,outtab)
	return string.translate(rot13)

plainText = raw_input("Dwse mou to munhma:")
cipherText = rot13_f(plainText)
print cipherText