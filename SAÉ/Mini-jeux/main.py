from os import system, get_terminal_size
from typing import Tuple
from colorama import Fore, Back
import sys
from time import sleep

import morpion
from termUtils import setTermCursor, setup, restoreTerm, displayEmptySquare
import allumettes
from players import addPlayer, isPlayerExisting, printScoreboard
import rules

def DisplayMenu(currentSelectedGame : int) -> None:
	"""
	La fonction `DisplayMenu` affiche un menu avec un scoreboard, des règles et une liste de
	mini-jeux, avec le jeu actuellement sélectionné en surbrillance.
	
	@param currentSelectedGame Le paramètre `currentSelectedGame` est un entier qui représente le jeu
	actuellement sélectionné dans le menu.
	"""

	maxSize : Tuple[int, int]

	maxSize = displayEmptySquare()

	setTermCursor(2, 5, "┌────────────┐")
	setTermCursor(3, 5, "│ SCOREBOARD │")
	setTermCursor(4, 5, "└────────────┘")
	printScoreboard()
	setTermCursor(2, maxSize[0] - 11, "┌──────────┐")
	setTermCursor(3, maxSize[0] - 11, "│  RÈGLES  │")
	setTermCursor(4, maxSize[0] - 11, "└──────────┘")
	setTermCursor(6, (maxSize[0] - 23) // 2, "┌─────────────────────────┐")
	setTermCursor(7, (maxSize[0] - 23) // 2, "│         BONJOUR         │")
	setTermCursor(8, (maxSize[0] - 23) // 2, "│   Liste des mini-jeux   │")
	setTermCursor(9, (maxSize[0] - 23) // 2, "└─────────────────────────┘")
	setTermCursor(10 + currentSelectedGame, (maxSize[0] - 7) // 2, DisplayGameSelected(currentSelectedGame))
	setTermCursor(maxSize[1] + 1, 3, "Appuyer sur \"q\" pour quitter")
	print()

def DisplayGameSelected(currentSelectedGame : int) -> str:
	"""
	La fonction prend un paramètre entier représentant le jeu actuellement sélectionné et renvoie une
	chaîne qui sera le jeu en surbrillance.
	
	@param currentSelectedGame Un nombre entier représentant le jeu actuellement sélectionné.

	@return La chaîne correctement formater pour être sélectionner.
	"""

	gameStr: str
	maxWidth = get_terminal_size().columns - 3

	if currentSelectedGame == 1:
		gameStr = "Devinette"
		setTermCursor(12, (maxWidth - 7) // 2, "  Allumette")
		setTermCursor(13, (maxWidth - 7) // 2, "  Morpion")
		setTermCursor(14, (maxWidth - 7) // 2, "  Puissance 4")
		setTermCursor(3, maxWidth - 9, " RÈGLES")
	elif currentSelectedGame == 2:
		setTermCursor(11, (maxWidth - 7) // 2, "  Devinette")
		gameStr = "Allumette"
		setTermCursor(13, (maxWidth - 7) // 2, "  Morpion")
		setTermCursor(14, (maxWidth - 7) // 2, "  Puissance 4")
		setTermCursor(3, maxWidth - 9, " RÈGLES")
	elif currentSelectedGame == 3:
		setTermCursor(11, (maxWidth - 7) // 2, "  Devinette")
		setTermCursor(12, (maxWidth - 7) // 2, "  Allumette")
		gameStr = "Morpion"
		setTermCursor(14, (maxWidth - 7) // 2, "  Puissance 4")
		setTermCursor(3, maxWidth - 9, " RÈGLES")
	elif currentSelectedGame == 4:
		setTermCursor(11, (maxWidth - 7) // 2, "  Devinette")
		setTermCursor(12, (maxWidth - 7) // 2, "  Allumette")
		setTermCursor(13, (maxWidth - 7) // 2, "  Morpion")
		gameStr = "Puissance 4" 
		setTermCursor(3, maxWidth - 9, " RÈGLES")
	elif currentSelectedGame == -1:
		setTermCursor(11, (maxWidth - 7) // 2, "  Devinette")
		setTermCursor(12, (maxWidth - 7) // 2, "  Allumette")
		setTermCursor(13, (maxWidth - 7) // 2, "  Morpion")
		setTermCursor(14, (maxWidth - 7) // 2, "  Puissance 4")
		gameStr = "RÈGLES"
	else :
		gameStr = "ERROR"
	print()

	return str(">" + Back.WHITE + Fore.BLACK + gameStr + Back.RESET + Fore.RESET + "  ")

if __name__ == "__main__":
	player1 : str
	player2 : str
	currChar : str
	isOnRules : bool
	maxWidth : int
	original : list[int]
	currentSelectedGame : int

	player1 = ""
	player2 = ""
	isOnRules  = False
	currChar = ""
	maxWidth = get_terminal_size().columns - 3
	currentSelectedGame = 1

	system("clear")
	while player1 == "":
		player1 = input("Joueur 1 : ")
		if isPlayerExisting(player1):
			print(f"{player1} bon retour parmi nous !")
		elif player1 == "":
			system("clear")
			print("Votre pseudo ne peut pas être rien !")
		else:
			addPlayer(player1)
	while player2 == "":
		player2 = input("\nJoueur 2 : ")
		if isPlayerExisting(player2):
			print(f"{player2} bon retour parmi nous !")
			sleep(1)
		elif player2 == "":
			system("clear")
			print("Votre pseudo ne peut pas être rien !")
		else:
			addPlayer(player2)

	original = setup()

	while True:
		DisplayMenu(currentSelectedGame)
		while True:
			currChar = sys.stdin.read(1)
			if currChar == '\x1b':
				currChar = sys.stdin.read(1)
				currChar = sys.stdin.read(1)
				if currChar == 'A' and currentSelectedGame != 1 and isOnRules == False:
					setTermCursor(10 + currentSelectedGame - 1, (maxWidth - 7) // 2, DisplayGameSelected(currentSelectedGame - 1))
					print()
					currentSelectedGame -= 1
				if currChar == 'B' and currentSelectedGame != 4 and isOnRules == False:
					setTermCursor(10 + currentSelectedGame + 1, (maxWidth - 7) // 2, DisplayGameSelected(currentSelectedGame + 1))
					print()
					currentSelectedGame += 1
				if currChar == 'C' and isOnRules == False:
					setTermCursor(3, maxWidth - 9, DisplayGameSelected(-1))
					print()
					isOnRules = True
				if currChar == 'D' and isOnRules:
					setTermCursor(10 + currentSelectedGame, (maxWidth - 7) // 2, DisplayGameSelected(currentSelectedGame))
					print()
					isOnRules = False
			elif currChar == 'q' or currChar == 'Q':
				restoreTerm(original)
			elif currChar == '\n':
				break
		if isOnRules:
			rules.start(1, player1, player2, original)
			isOnRules = False
		elif currentSelectedGame == 2:
			allumettes.start(player1, player2, original)
		elif currentSelectedGame == 3:
			morpion.start(player1, player2, original)