from os import system
from colorama import Fore, Back
from termUtils import printAt
import sys
from time import sleep
from os import get_terminal_size

import main
from players import addPoint
from termUtils import displayEmptySquare

def DisplayMenu(currentSelectedNb : int, matchs : int, player : str) -> None:
	"""
	La fonction `DisplayMenu` affiche un menu avec un numéro actuellement sélectionné.
	
	@param currentSelectedNb Le numéro actuellement sélectionné dans le menu.
	@param matchs Le paramètre "matchs" représente le nombre d'allumettes restantes.
	@param player Le paramètre "player" est une chaîne qui représente le joueur actuel.
	"""

	maxSize : tuple[int, int]

	maxSize = displayEmptySquare()

	printAt(maxSize[1] // 2 + 3 + currentSelectedNb, maxSize[0] // 2 - 1,update(currentSelectedNb, player, matchs))
	print()

def DisplayWinMenu(winner : str) -> None:
	"""
	La fonction DisplayWinMenu affiche un menu pour le gagnant d'une partie.
	
	@param winner Le paramètre gagnant est une chaîne qui représente le nom du gagnant.
	"""

	maxSize : tuple[int, int]

	maxSize = displayEmptySquare()

	printAt(maxSize[1] // 2, (maxSize[0] - len(f"{winner} a gagné")) // 2, f"{winner} a gagné")
	print()

def update(currentSelectedNb : int, player : str, matchs : int) -> str:
	"""
	La fonction "update" prend en compte le numéro actuellement sélectionné, le nom du joueur et le
	nombre de matchs à supprimer, et met a jour le menu avec le nouveau nombre d'allumettes, le nouveau 
	nom du joueur et met a jour le jeux sélectionner.
	
	@param currentSelectedNb Un nombre entier représentant le numéro actuellement sélectionné.
	@param player Une chaîne représentant le nom du joueur.
	@param matchs Le paramètre "matchs" représente le nombre de d'allumettes restantes.

	@return La chaîne correctement formater pour être sélectionner.
	"""

	maxWidth : int
	maxHeight : int

	maxWidth = get_terminal_size().columns - 3
	maxHeight = get_terminal_size().lines - 3

	printAt(maxHeight // 2, 1, f"║" + " " * maxWidth + "║")
	printAt(maxHeight // 2, (maxWidth - len(f"Nombre d'allumettes restantes : {matchs}")) // 2 , f"Nombre d'allumettes restantes : {matchs}")
	printAt(maxHeight // 2 + 2, 1, f"║" + " " * maxWidth + "║")
	printAt(maxHeight // 2 + 2, (maxWidth - len(f"{player} choisissez combien d'allumette vous allez supprimer :")) // 2, f"{player} choisissez combien d'allumette vous allez supprimer :")

	if currentSelectedNb == 1:
		printAt(maxHeight // 2 + 5, maxWidth // 2 - 1, " 2")
		printAt(maxHeight // 2 + 6, maxWidth // 2 - 1, " 3")
	elif currentSelectedNb == 2:
		printAt(maxHeight // 2 + 4, maxWidth // 2 - 1, " 1")
		printAt(maxHeight // 2 + 6, maxWidth // 2 - 1, " 3")
	elif currentSelectedNb == 3:
		printAt(maxHeight // 2 + 4, maxWidth // 2 - 1, " 1")
		printAt(maxHeight // 2 + 5, maxWidth // 2 - 1, " 2")

	print()

	return str(">" + Back.WHITE + Fore.BLACK + f'{currentSelectedNb}' + Back.RESET + Fore.RESET)

def start(player1 : str, player2 : str) -> None:
	"""
	La fonction "start" prend trois paramètres: player1 (une chaîne), player2 (une chaîne) et original
	(une liste d'entiers) et met en place les piliers du jeu pour ensuite enregistre les inputs 
	utilisateur et réagit en fonction.
	
	@param player1 Une chaîne représentant le nom du joueur 1.
	@param player2 Une chaîne représentant le nom du joueur 2.
	@param original Le paramètre "original" est une liste d'entiers qui représente l'état du terminal la base.
	"""

	matchs : int
	currChar : str
	currentSelectedNb : int
	currentPlayer : int
	maxWidth : int
	maxHeight : int

	maxWidth = get_terminal_size().columns - 3
	maxHeight = get_terminal_size().lines - 3
	currentPlayer = 1
	matchs = 20
	currChar = ""
	currentSelectedNb = 3

	DisplayMenu(currentSelectedNb, matchs, player1)
	while True:
		while True:
			currChar = sys.stdin.read(1)
			if currChar == '\x1b':
				currChar = sys.stdin.read(1)
				currChar = sys.stdin.read(1)
				if currChar == 'A' and currentSelectedNb != 1:
					currentSelectedNb -= 1
					if currentPlayer == 1:
						printAt(maxHeight // 2 + 3 + currentSelectedNb, maxWidth // 2 - 1,update(currentSelectedNb, player1, matchs))
						print()
					else:
						printAt(maxHeight // 2 + 3 + currentSelectedNb, maxWidth // 2 - 1,update(currentSelectedNb, player2, matchs))
						print()
				if currChar == 'B' and currentSelectedNb != 3:
					currentSelectedNb += 1
					if currentPlayer == 1:
						printAt(maxHeight // 2 + 3 + currentSelectedNb, maxWidth // 2 - 1,update(currentSelectedNb, player1, matchs))
						print()
					else:
						printAt(maxHeight // 2 + 3 + currentSelectedNb, maxWidth // 2 - 1,update(currentSelectedNb, player2, matchs))
						print()
			elif currChar == 'q' or currChar == 'Q':
				return
			elif currChar == '\n':
				matchs = matchs - currentSelectedNb
				if matchs == 0:
					if currentPlayer == 1:
						DisplayWinMenu(player2)
						addPoint(player2, 2)
					else:
						DisplayWinMenu(player1)
						addPoint(player1, 2)
					sleep(1)
					return
				elif matchs < 0:
					matchs = matchs + currentSelectedNb
				else:
					if currentPlayer == 1:
						currentPlayer = 2
						printAt(maxHeight // 2 + 3 + currentSelectedNb, maxWidth // 2 - 1,update(currentSelectedNb, player2, matchs))
						print()
					else:
						currentPlayer = 1
						printAt(maxHeight // 2 + 3 + currentSelectedNb, maxWidth // 2 - 1,update(currentSelectedNb, player1, matchs))
						print()
