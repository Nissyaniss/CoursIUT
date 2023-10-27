import sys
from os import system, get_terminal_size
from termUtils import printAt, displayEmptySquare, centerTextAtLine
from colorama import Fore, Back
from typing import Tuple

import main

def DisplayMenu() -> None:
	displayEmptySquare()

	centerTextAtLine(6, "┌─────────────────────────┐")
	centerTextAtLine(7, "│         BONJOUR         │")
	centerTextAtLine(8, "│    Liste des règles     │")
	centerTextAtLine(9, "└─────────────────────────┘")

def DisplayGameSelected(currentSelectedGame : int) -> str:
	gameStr: str
	maxWidth = get_terminal_size().columns - 1

	if currentSelectedGame == 1:
		gameStr = "Devinette"
		printAt(12, (maxWidth - 13) // 2, "  Allumette")
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
	return ">" + Back.WHITE + Fore.BLACK + gameStr + Back.RESET + Fore.RESET + " "

def printRule(gameStr : str, ruleStr : str, currentSelectedGame : int, player1 : str, player2 : str) -> None:
	currChar : str
	
	currChar = ''

	displayEmptySquare()
	centerTextAtLine(2, "┌" + len(gameStr) * "─" + "┐")
	centerTextAtLine(3, "│" + f"{gameStr}" +       "│")
	centerTextAtLine(4, "└" + len(gameStr) * "─" + "┘")
	centerTextAtLine(8, ruleStr)
	while True:
		currChar = sys.stdin.read(1)
		if currChar == 'q' or currChar == 'Q':
			return

def start(currentSelectedGame : int, player1 : str, player2 : str) -> None:
	maxWidth : int

	maxWidth = get_terminal_size().columns - 2

	while True:
		while True:
			DisplayMenu()
			printAt(10 + currentSelectedGame, (maxWidth - 13) // 2, DisplayGameSelected(currentSelectedGame))
			currChar = sys.stdin.read(1)
			if currChar == '\x1b':
				currChar = sys.stdin.read(1)
				currChar = sys.stdin.read(1)
				if currChar == 'A' and currentSelectedGame != 1:
					currentSelectedGame -= 1
				if currChar == 'B' and currentSelectedGame != 4:
					currentSelectedGame += 1
			elif currChar == 'q' or currChar == 'Q':
				return
			elif currChar == '\n':
				system("clear")
				break
		if currentSelectedGame == 1:
			printRule("DEVINETTE", "Le joueur 1 rentre un chiffre et le joueur 2 doit le deviner en moins de temps possible !", 1, player1, player2)
		elif currentSelectedGame == 2:
			printRule("ALLUMETTES", "Chaque joueur retire 1 - 3 allumettes jusqu'a ce qui en ai plus ! Le perdant est celui qui prend la dernière.", 2, player1, player2)
		elif currentSelectedGame == 3:
			printRule("MORPION", "Chacun son tour les joueurs place un pion le premier à en aligner 3 a gagné !", 3, player1, player2)
		elif currentSelectedGame == 4:
			printRule("PUISSANCE 4", "Chacun son tour les joueurs place un pion le premier à en aligner 4 a gagné !", 4, player1, player2)