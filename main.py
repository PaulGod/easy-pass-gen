import secrets as sc

while True:
	print('Characters in password:')
	try:
		userInput = int(input('> '))
		break
	except:
		print('That is not an integar!')

e = sc.token_hex(userInput)
print(f'This is your password: {e}')
