from os import system, get_terminal_size
from typing import List

from ANSIcolors import inverseColor
from termUtils import printAt, displayEmptySquare, centerTextAtLine, getKey

def displayMenu() -> None:
	"""
	Affiche le menu
	"""

	displayEmptySquare()

	centerTextAtLine(6, "┌─────────────────────────┐")
	centerTextAtLine(7, "│         BONJOUR         │")
	centerTextAtLine(8, "│    Liste des règles     │")
	centerTextAtLine(9, "└─────────────────────────┘")

def displayGameSelected(currentSelectedGame : int) -> str:
	"""
	Affiche le jeu sélectionner

	Entrée : currentSelectedGame : int
	currentSelectedGame symbolise le jeu sélectionner

	Sortie : str
	str symbolise le jeu sélectionner formaté
	"""
	gameStr: str
	maxWidth = get_terminal_size().columns - 1

	if currentSelectedGame == 1:
		gameStr = "Devinette" # Met gameStr à la valeur du jeu sélectionner formaté
		printAt(12, (maxWidth - 13) // 2, "  Allumette") # Affiche les autres jeux
		printAt(13, (maxWidth - 13) // 2, "  Morpion")
		printAt(14, (maxWidth - 13) // 2, "  Puissance 4")
	elif currentSelectedGame == 2:
		printAt(11, (maxWidth - 13) // 2, "  Devinette")
		gameStr = "Allumette"
		printAt(13, (maxWidth - 13) // 2, "  Morpion")
		printAt(14, (maxWidth - 13) // 2, "  Puissance 4")
	elif currentSelectedGame == 3:
		printAt(11, (maxWidth - 13) // 2, "  Devinette")
		printAt(12, (maxWidth - 13) // 2, "  Allumette")
		gameStr = "Morpion"
		printAt(14, (maxWidth - 13) // 2, "  Puissance 4")
	elif currentSelectedGame == 4:
		printAt(11, (maxWidth - 13) // 2, "  Devinette")
		printAt(12, (maxWidth - 13) // 2, "  Allumette")
		printAt(13, (maxWidth - 13) // 2, "  Morpion")
		gameStr = "Puissance 4" 
	else :
		gameStr = "ERROR"

	print()
	return ">" + inverseColor(gameStr) + " "

def printRule(gameStr : str, listStr : List[str]) -> None:
	"""
	Affiche la règle du jeu sélectionner

	Entrée : gameStr : str
	gameStr symbolise le jeu sélectionner

	Entrée : ruleStr : str
	ruleStr symbolise la règle du jeu sélectionner
	"""
	currChar : str
	
	currChar = ''

	displayEmptySquare()
	centerTextAtLine(2, "┌" + len(gameStr) * "─" + "┐") # Affiche le menu des règles du jeu sélectionner
	centerTextAtLine(3, "│" + f"{gameStr}" +       "│")
	centerTextAtLine(4, "└" + len(gameStr) * "─" + "┘")
	for i, line in enumerate(listStr):
		centerTextAtLine(8 + i, line) # Affiche la règle du jeu sélectionner
	while True:
		currChar = getKey()
		if currChar == "TAB":
			return

def start(currentSelectedGame : int) -> None:
	"""
	Lance le menu des règles

	Entrée : currentSelectedGame : int
	currentSelectedGame symbolise le jeu sélectionner
	"""
	maxWidth : int

	maxWidth = get_terminal_size().columns - 3 # Récupère la taille du terminal

	while True:
		while True:
			displayMenu()
			printAt(10 + currentSelectedGame, (maxWidth - 11) // 2, displayGameSelected(currentSelectedGame)) # Affiche le jeu sélectionner
			currChar = getKey()
			if currChar == "UP" and currentSelectedGame != 1: # Change le jeu sélectionner
				currentSelectedGame -= 1
			if currChar == "DOWN" and currentSelectedGame != 4:
				currentSelectedGame += 1
			elif currChar == "TAB": # Quitte au menu
				return
			elif currChar == "ENTER":
				system("clear")
				break
		if currentSelectedGame == 1:
			printRule("DEVINETTE", ["Le joueur 1 rentre un chiffre et le joueur 2 doit le deviner en moins de temps possible !", "Le joueur 1 triche il peut mais il prendra 1 strike au bout de 3 il a perdu.", "Aussi si le joueur 1 ment alors que le joueur 2 a juste alors le joueur 1 perd directement peut importe le nombre de strike."])
		elif currentSelectedGame == 2:
			printRule("ALLUMETTES", ["Chaque joueur retire 1 - 3 allumettes jusqu'a ce qui en ai plus ! Le perdant est celui qui prend la dernière."])
		elif currentSelectedGame == 3:
			printRule("MORPION", ["Chacun son tour les joueurs place un pion le premier à en aligner 3 a gagné !"])
		elif currentSelectedGame == 4:
			printRule("PUISSANCE 4", ["Chacun son tour les joueurs place un pion le premier à en aligner 4 a gagné !"])