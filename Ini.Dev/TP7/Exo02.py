def CountVoyelles(string : str):
	count : int

	count = 0
	
	for i in string:
		if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "y":
			count += 1
	print(f"Il y a {count} voyelles dans le string")
	start()

def isPalindrome(string : str):
	result : bool

	result = True
	for i in range(0, len(string) // 2):
		for y in range(len(string) - 1, len(string) // 2, -1):
			if string[i] != string[y]:
				result = False

	if result == True:
		print("Le string est un palindrome")
	else:
		print("Le string n'est pas un palindrome")

def menu():
	print("1. Compter les voyelle")
	print("2. Est palindrome")
	print("3. Quitter")

def start():
	end : bool
	choix : int

	end = True
	choix = 0

	menu()
	while end:
		try:
			choix = int(input("Choix : "))
			if choix < 1 or choix > 3:
				end = True
			else:
				end = False
		except ValueError:
			end = True
	if choix == 1:
		CountVoyelles(input("Entrer un string : "))
	elif choix == 2:
		isPalindrome(input("Entrer un string : "))

if __name__ == "__main__":
	start()