from os import system, get_terminal_size
from colorama import Fore, Back
import sys
from time import sleep

import morpion
from termUtils import printAt, setup, restoreTerm, displayEmptySquare, centerTextAtLine
import allumettes
from players import addPlayer, isPlayerExisting, printScoreboard
import rules
import devinette

def DisplayMenu(currentSelectedGame : int) -> None:
	maxWidth : int
	
	maxWidth = get_terminal_size().columns - 3
	
	displayEmptySquare()
	printAt(2, 5, "┌────────────┐")
	printAt(3, 5, "│ SCOREBOARD │")
	printAt(4, 5, "└────────────┘")
	printScoreboard(player1, player2)
	printAt(2, maxWidth - 11, "┌──────────┐")
	printAt(3, maxWidth - 11, "│  RÈGLES  │")
	printAt(4, maxWidth - 11, "└──────────┘")
	centerTextAtLine(6, "┌─────────────────────────┐")
	centerTextAtLine(7, "│         BONJOUR         │")
	centerTextAtLine(8, "│   Liste des mini-jeux   │")
	centerTextAtLine(9, "└─────────────────────────┘")
	printAt(10 + currentSelectedGame, (maxWidth - 11) // 2, DisplayGameSelected(currentSelectedGame))

def DisplayGameSelected(currentSelectedGame : int) -> str:
	gameStr: str
	maxWidth = get_terminal_size().columns - 3

	if currentSelectedGame == 1:
		gameStr = "Devinette"
		printAt(12, (maxWidth - 11) // 2, "  Allumette")
		printAt(13, (maxWidth - 11) // 2, "  Morpion")
		printAt(14, (maxWidth - 11) // 2, "  Puissance 4")
		printAt(3, maxWidth - 9, " RÈGLES")
	elif currentSelectedGame == 2:
		printAt(11, (maxWidth - 11) // 2, "  Devinette")
		gameStr = "Allumette"
		printAt(13, (maxWidth - 11) // 2, "  Morpion")
		printAt(14, (maxWidth - 11) // 2, "  Puissance 4")
		printAt(3, maxWidth - 9, " RÈGLES")
	elif currentSelectedGame == 3:
		printAt(11, (maxWidth - 11) // 2, "  Devinette")
		printAt(12, (maxWidth - 11) // 2, "  Allumette")
		gameStr = "Morpion"
		printAt(14, (maxWidth - 11) // 2, "  Puissance 4")
		printAt(3, maxWidth - 9, " RÈGLES")
	elif currentSelectedGame == 4:
		printAt(11, (maxWidth - 11) // 2, "  Devinette")
		printAt(12, (maxWidth - 11) // 2, "  Allumette")
		printAt(13, (maxWidth - 11) // 2, "  Morpion")
		gameStr = "Puissance 4" 
		printAt(3, maxWidth - 9, " RÈGLES")
	elif currentSelectedGame == -1:
		printAt(11, (maxWidth - 11) // 2, "  Devinette")
		printAt(12, (maxWidth - 11) // 2, "  Allumette")
		printAt(13, (maxWidth - 11) // 2, "  Morpion")
		printAt(14, (maxWidth - 11) // 2, "  Puissance 4")
		gameStr = "RÈGLES"
	else :
		gameStr = "ERROR"

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
					currentSelectedGame -= 1
					printAt(10 + currentSelectedGame, (maxWidth - 11) // 2, DisplayGameSelected(currentSelectedGame))
				if currChar == 'B' and currentSelectedGame != 4 and isOnRules == False:
					currentSelectedGame += 1
					printAt(10 + currentSelectedGame, (maxWidth - 11) // 2, DisplayGameSelected(currentSelectedGame))
				if currChar == 'C' and isOnRules == False:
					printAt(3, maxWidth - 9, DisplayGameSelected(-1))
					isOnRules = True
				if currChar == 'D' and isOnRules:
					printAt(10 + currentSelectedGame, (maxWidth - 11) // 2, DisplayGameSelected(currentSelectedGame))
					isOnRules = False
			elif currChar == 'q' or currChar == 'Q':
				restoreTerm(original)
			elif currChar == '\n':
				break
		if isOnRules:
			rules.start(1, player1, player2)
			isOnRules = False
		elif currentSelectedGame == 1:
			devinette.start(player1, player2)
			print("\x1b[?25l", end='', flush=True)
		elif currentSelectedGame == 2:
			allumettes.start(player1, player2)
		elif currentSelectedGame == 3:
			morpion.start(player1, player2)