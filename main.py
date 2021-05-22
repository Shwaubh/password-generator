import random

try:
	print("This Program generates password with combination of Lowercase, Uppercase, Number, Symbols")
	n = int(input("Enter Length of Password Required: (Min Length 4)-(Max Length 20): "))
	if n < 4 or n > 20:
		raise ValueError
	
	password = []
	
	lower = 'abcdefghijklmnopqrstuvwxyz'
	upper = lower.upper()
	number = '0123456789'
	symbol = '@!#$%^&*()'
	overall = lower+upper+number+symbol
	
	each = n//4
	rem = n%4	
	
	lower = random.sample(lower, k=each)
	upper = random.sample(upper, k=each)
	number = random.sample(number, k=each)
	symbol = random.sample(symbol, k=each)
	if rem > 0:
		overall = random.sample(overall, k=rem)
		password.extend(overall)
	password.extend(lower)
	password.extend(upper)
	password.extend(number)
	password.extend(symbol)
	random.shuffle(password)
	random.shuffle(password)
	random.shuffle(password)
		
	password = ''.join(password)
	
	print("Your Generated Password is: ", password, sep='\n')
	ref = input("Enter Reference name to this password to save it to file: ")
	with open('pass.txt', 'a') as passw:
		passw.write("\n")
		passw.write(ref + " :: " + password)
		passw.close()
	print("Password saved successfully")

except ValueError as valerr:
	print("Invalid Entry, Please enter a valid length")

