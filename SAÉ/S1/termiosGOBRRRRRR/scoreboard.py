from typing import List, Dict
from players import getPlayers
from ANSIcolors import inverseColor
from termUtils import printAt, get_terminal_size, getKey, centerTextAtLine, displayEmptySquare

from os import system

def displayGameSelected(currentSelectedGame : int) -> str:
	"""
	Affiche le jeu sélectionner

	Entrée : currentSelectedGame : int
	currentSelectedGame symbolise le jeu sélectionner

	Sortie : gameStr : str
	gameStr symbolise le string formaté du jeu sélectionner
	"""
	gameStr: str
	maxWidth = get_terminal_size().columns - 3

	if currentSelectedGame == 1:
		gameStr = "Devinette" # Défini le string du jeu sélectionner
		printAt(12, (maxWidth - 11) // 2, "  Allumette") # Affiche les autres jeux
		printAt(13, (maxWidth - 11) // 2, "  Morpion")
		printAt(14, (maxWidth - 11) // 2, "  Puissance 4")
	elif currentSelectedGame == 2:
		printAt(11, (maxWidth - 11) // 2, "  Devinette")
		gameStr = "Allumette"
		printAt(13, (maxWidth - 11) // 2, "  Morpion")
		printAt(14, (maxWidth - 11) // 2, "  Puissance 4")
	elif currentSelectedGame == 3:
		printAt(11, (maxWidth - 11) // 2, "  Devinette")
		printAt(12, (maxWidth - 11) // 2, "  Allumette")
		gameStr = "Morpion"
		printAt(14, (maxWidth - 11) // 2, "  Puissance 4")
	elif currentSelectedGame == 4:
		printAt(11, (maxWidth - 11) // 2, "  Devinette")
		printAt(12, (maxWidth - 11) // 2, "  Allumette")
		printAt(13, (maxWidth - 11) // 2, "  Morpion")
		gameStr = "Puissance 4" 
	else :
		gameStr = "ERROR"

	return str(">" + inverseColor(gameStr) + "  ") # Retourne le string formaté

def displayMenu(currentSelectedGame : int) -> None:
	"""
	Affiche le menu avec le jeu sélectionner

	Entrée : currentSelectedGame : int
	currentSelectedGame symbolise le jeu sélectionner
	"""
	maxWidth : int
	
	maxWidth = get_terminal_size().columns - 3 # Défini la taille maximal du terminal
	
	displayEmptySquare() # Affiche un carré vide
	centerTextAtLine(6, "┌─────────────────────────┐")
	centerTextAtLine(7, "│         BONJOUR         │") # Affiche un carré avec le titre écrit dedans centré
	centerTextAtLine(8, "│  Liste des scoreboards  │")
	centerTextAtLine(9, "└─────────────────────────┘")
	printAt(10 + currentSelectedGame, (maxWidth - 11) // 2, displayGameSelected(currentSelectedGame)) # Affiche le jeux sélectionner
	return

def displayScoreboard(game : int) -> None:
	"""
	Affiche le scoreboard du jeu sélectionner

	Entrée : game : int
	game symbolise le jeu sélectionner
	"""
	maxWidth : int
	data: Dict[str, tuple[int, int, int, int]]
	i : int
	scores : List[tuple[str, tuple[int, int, int, int]]]
	
	maxWidth = get_terminal_size().columns - 3
	maxHeight = get_terminal_size().lines
	data = getPlayers()
	i = 0
	scores = list(data.items()) # Récupère les données des joueurs
	scores.sort(key=lambda x: x[1][game - 1], reverse=True) # Trie les scores (lambda est une function temporaire et sans nom et x est un paramètre que je ne peut pas typé)

	system("clear")
	printAt(1, 1, "╔" + "═" * maxWidth +"╗\n") # Affiche le début d'un carré vide
	for i in range(1, 9):
		print("║" + " " * maxWidth + "║")

	centerTextAtLine(3, "┌─────────────────────────┐")
	centerTextAtLine(4, "│         BONJOUR         │") # Affiche un carré avec le titre écrit dedans centré
	centerTextAtLine(5, "│     Liste des score     │")
	centerTextAtLine(6, "└─────────────────────────┘")
	print("\n", end="")
	
	for i in range(0, len(scores)): # Affiche les scores
		print("║" + " " * maxWidth + "║", end="")
		centerTextAtLine(9 + i, scores[i][0] + " : " + str(scores[i][1][game - 1]))
		print("\n", end="")
	for i in range(len(scores) + 9, maxHeight - 2): # Affiche le reste du carré si besoin
		print("║" + " " * maxWidth + "║")
	print("║" + maxWidth * " " + "║")
	print("║ Appuyer sur \"TAB\" pour quitter" + (maxWidth - 31) * " " + "║") # Affiche le message pour quitter
	print("╚" + "═" * maxWidth +"╝", end="", flush=True)
	while True:
		currChar = getKey()
		if currChar == "TAB": # Vérifie is la touche pressée est Tab
				return

def start() -> None:
	"""
	Affiche le menu des scoreboards
	"""
	currentSelectedGame: int
	maxWidth: int

	maxWidth = get_terminal_size().columns - 3
	currentSelectedGame = 1

	while True:
		displayMenu(currentSelectedGame) # Affiche le menu avec le premier jeu de sélectionner
		while True:
			currChar = getKey()
			if currChar == "UP" and currentSelectedGame != 1: # Vérifie is la touche pressée est la flèche du haut
				currentSelectedGame -= 1 # Change le jeu
				printAt(10 + currentSelectedGame, (maxWidth - 11) // 2, displayGameSelected(currentSelectedGame)) # Affiche le jeu sélectionner
			if currChar == "DOWN" and currentSelectedGame != 4: # Vérifie is la touche pressée est la flèche du bas
				currentSelectedGame += 1 # Change le jeu
				printAt(10 + currentSelectedGame, (maxWidth - 11) // 2, displayGameSelected(currentSelectedGame)) # Affiche le jeu sélectionner
			elif currChar == "TAB": # Vérifie is la touche pressée est Tab
				return
			elif currChar == "ENTER": # Vérifie is la touche pressée est Entrée
				break
			else:
				continue # Si il y a une autre touche on l'ignore

		displayScoreboard(currentSelectedGame) # Affiche le scoreboard du jeu sélectionner