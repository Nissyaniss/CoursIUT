from random import randint
from os import system
from time import time, sleep
from colorama import Fore

def createTab(tab : list[int]) -> list[int]:
	n : int
	i : int

	i = 0
	n = 0

	while n < 1:
		try:
			n = int(input("Taille du tableau ? "))
			if n < 1:
				print("Erreur de saisie")
		except ValueError:
			print("Erreur de saisie")
			n = 0

	for i in range(0, n):
		tab.append(randint(0, 100))

	return tab

def setCursorPosition(line : int, column : int) -> None:
	print(f"\x1b[{line};{column}f", end='', flush=True)

def sortBubble(tab : list[int]) -> list[int]:
	"""
	Trier un tableau par ordre croissant
	:param tab: Le tableau à trier
	:type tab: list[int]
	:return: Le tableau trié
	"""
	i : int
	timeStart : float
	p : int

	i = 0
	p = len(tab)

	timeStart = time()
	while p > 0:
		for i in range(p - 1):
			if tab[i] > tab[i + 1]:
				tab[i], tab[i + 1] = tab[i + 1], tab[i]
			system("clear")
			setCursorPosition(1, 1)
			print(' '.join(
				Fore.RED + f'{tab[e]:3}' + Fore.RESET
				if e == i + 1
				else
				Fore.GREEN + f'{tab[e]:3}' + Fore.RESET
				if e == i
				else
				f'{tab[e]:3}'
				for e in range(0, min(len(tab) - 1, 35))))
			for y in range (35, len(tab), 35):
				print(' '.join(
					Fore.RED + f'{tab[e]:3}' + Fore.RESET
					if e == i + 1
					else
					Fore.GREEN + f'{tab[e]:3}' + Fore.RESET
					if e == i
					else
					f'{tab[e]:3}'
					for e in range(y, min(len(tab) - 1, y + 35)))
					)
			sleep(0.5)
		p -= 1
		
	print("\nTemps d'exécution : " + str(time() - timeStart) + " secondes")

	return tab

def sortInsertion(tab : list[int]) -> list[int]:
	n : int
	n = len(tab)
	timeStart : float

	timeStart = time()
	for i in range(1, n):
		j : int
		j = i

		while j > 0 and tab[j - 1] > tab[j]:
			tmp = tab[j]
			tab[j] = tab[j - 1]
			tab[j - 1] = tmp
			j -= 1
			system("clear")
			setCursorPosition(1, 1)
			print(' '.join(
				Fore.RED + f'{tab[e]:3}' + Fore.RESET
				if e == j + 1
				else
				Fore.GREEN + f'{tab[e]:3}' + Fore.RESET
				if e == j
				else
				f'{tab[e]:3}'
				for e in range(0, min(len(tab) - 1, 35))))
			for y in range (35, len(tab), 35):
				print(' '.join(
					Fore.RED + f'{tab[e]:3}' + Fore.RESET
					if e == j + 1
					else
					Fore.GREEN + f'{tab[e]:3}' + Fore.RESET
					if e == j	
					else
					f'{tab[e]:3}'
					for e in range(y, min(len(tab) - 1, y + 35)))
					)
			sleep(0.5)
	print("Temps d'exécution : " + str(time() - timeStart) + " secondes")

	return tab

def dichotomie(tab : list[int]):
	lenTab : int
	i : int
	j : int
	toFind : int
	end : bool
	timeStart : float
	k : int

	lenTab = len(tab)
	i = 0
	j = lenTab - 1
	toFind = 0
	end = False

	while not end:
		try:
			toFind = int(input("Nombre à rechercher ? "))
			end = True
		except ValueError:
			print("Erreur de saisie")
			end = False

	timeStart = time()
	while i <= j:
		k = (i + j) // 2

		if tab[k] == toFind:
			print("Nombre trouvé à l'indice " + str(k))
			break
		elif tab[k] < toFind:
			i = k + 1
		else:
			j = k - 1
	print("Temps d'exécution : " + str(time() - timeStart) + " secondes")

def displayTab(tab : list[int]):
	print(f"{' '.join(f'{x:3}' for x in tab[:35])}")

	for i in range (20, len(tab), 20):
		print(f"{' '.join(f'{x:3}' for x in tab[i : i + 35])}")
	

if __name__ == "__main__":
	tab : list[int]
	choix : int
	end : bool

	tab = []
	choix = 0
	end = False

	while choix != 7:
		print("Menu")
		print("1 - Créer un tableau")
		print("2 - Afficher le tableau")
		print("3 - Trier le tableau (triage à bulle)")
		print("4 - Trier le tableau (triage par insertion)")
		print("5 - Rechercher un élément dans le tableau trié")
		print("6 - Les deux tris sur le meme tableau")
		print("7 - Quitter")

		while not end:
			try:
				choix = int(input("Votre choix ? "))
				end = True
				if choix < 1 or choix > 7:
					print("Erreur de saisie")
					end = False
			except ValueError:
				print("Erreur de saisie")
				end = False

		end = False
		match choix:
			case 1:
				system("clear")
				tab = createTab(tab)
			case 2:
				system("clear")
				displayTab(tab)
			case 3:
				tab = sortBubble(tab)
			case 4:
				tab = sortInsertion(tab)
			case 5:
				dichotomie(tab)
			case 6:
				print("Tri à insertion : ", end="")
				sortInsertion(tab)
				print("Tri à bulle : ", end="")
				tab = sortBubble(tab)