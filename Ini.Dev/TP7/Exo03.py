def CountVoyelles(tab : list[str]):
	count : int

	count = 0
	
	for i in range(0, len(tab)):
		for y in tab[i]:
			if y == "a" or y == "e" or y == "i" or y == "o" or y == "u" or y == "y":
				count += 1
		print(f"Il y a {count} voyelles dans le string")
		count = 0

def isPalindrome(tab : list[str]):
	result : bool

	result = True
	for d in range(0, len(tab)):
		for i in range(0, len(tab[d]) // 2):
			for y in range(len(tab[d]) - 1, len(tab[d]) // 2, -1):
				if tab[d][i] != tab[d][y]:
					result = False
		if result == True:
			print("Le string est un palindrome")
		else:
			print("Le string n'est pas un palindrome")

def menu():
	print("1. Saisir un tableau de nom")
	print("2. Nombre de voyelle par noms du tableau")
	print("3. Quel noms est un palindrome")
	print("4. Quitter")

if __name__ == "__main__":
	choix : int
	choix2 : str
	tab : list[str]
	nom : str

	choix = 0
	choix2 = 'o'
	nom = ""
	tab = []

	while True:
		menu()
		choix = int(input("Choix : "))
		if choix == 1:
			while choix2 == 'o':
				tab.append(input("Entrer un nom : "))
				choix2 = input("Continuer a entrer des nom [o/N]: ")
		elif choix == 2:
			CountVoyelles(tab)
		elif choix == 3:
			isPalindrome(tab)
		elif choix == 4:
			break