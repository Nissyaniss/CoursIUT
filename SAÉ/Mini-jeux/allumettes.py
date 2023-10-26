from os import system
from colorama import Fore, Back
from termUtils import printAt
import sys
from time import sleep
from os import get_terminal_size

from players import addPoint
from termUtils import displayEmptySquare, printAt, centerTextAtLine, centerText, centerTextAtColumn, setCursorPositionCenterAtColumn

def DisplayMenu(currentSelectedNb : int, player : str, matchs : int) -> str:
	maxHeight : int

	maxHeight = get_terminal_size().lines - 3
	
	centerTextAtLine(maxHeight // 2 - 1, f"Nombre d'allumettes restantes : {matchs}  ")
	centerText(f"{player} choisissez combien d'allumette vous allez supprimer :")
	if currentSelectedNb == 1:
		centerTextAtLine(maxHeight // 2 + 4, " 2")
		centerTextAtLine(maxHeight // 2 + 5, " 3")
	elif currentSelectedNb == 2:
		centerTextAtLine(maxHeight // 2 + 3, " 1")
		centerTextAtLine(maxHeight // 2 + 5, " 3")
	elif currentSelectedNb == 3:
		centerTextAtLine(maxHeight // 2 + 3, " 1")
		centerTextAtLine(maxHeight // 2 + 4, " 2")

	return str(">" + Back.WHITE + Fore.BLACK + f'{currentSelectedNb}' + Back.RESET + Fore.RESET)

def start(player1 : str, player2 : str) -> None:
	matchs : int
	currChar : str
	currentSelectedNb : int
	currentPlayer : int
	maxHeight : int

	maxHeight = get_terminal_size().lines - 3
	currentPlayer = 1
	matchs = 20
	currChar = ""
	currentSelectedNb = 1

	displayEmptySquare()
	centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, DisplayMenu(currentSelectedNb, player1, matchs))
	while True:
		while True:
			currChar = sys.stdin.read(1)
			if currChar == '\x1b':
				currChar = sys.stdin.read(1)
				currChar = sys.stdin.read(1)
				if currChar == 'A' and currentSelectedNb != 1:
					currentSelectedNb -= 1
					if currentPlayer == 1:
						centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, DisplayMenu(currentSelectedNb, player1, matchs))
					else:
						centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, DisplayMenu(currentSelectedNb, player2, matchs))
				if currChar == 'B' and currentSelectedNb != 3:
					currentSelectedNb += 1
					if currentPlayer == 1:
						centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb,DisplayMenu(currentSelectedNb, player1, matchs))
					else:
						centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb,DisplayMenu(currentSelectedNb, player2, matchs))
			elif currChar == 'q' or currChar == 'Q':
				return
			elif currChar == '\n':
				matchs = matchs - currentSelectedNb
				if matchs == 0:
					if currentPlayer == 1:
						displayEmptySquare()
						centerText(f"{player2} a gagné")
						addPoint(player2, 2)
					else:
						displayEmptySquare()
						centerText(f"{player1} a gagné")
						addPoint(player1, 2)
					sleep(1)
					return
				elif matchs < 0:
					matchs = matchs + currentSelectedNb
				else:
					if currentPlayer == 1:
						currentPlayer = 2
						centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, DisplayMenu(currentSelectedNb, player2, matchs))
					else:
						currentPlayer = 1
						centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, DisplayMenu(currentSelectedNb, player1, matchs))
