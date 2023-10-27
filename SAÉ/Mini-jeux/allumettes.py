from colorama import Fore, Back
import sys
from time import sleep
from os import get_terminal_size

from players import addPoint
from termUtils import displayEmptySquare, centerTextAtLine, centerText

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
	currentPlayer : str
	maxHeight : int

	maxHeight = get_terminal_size().lines - 3
	currentPlayer = player1
	matchs = 20
	currChar = ""
	currentSelectedNb = 1

	displayEmptySquare()
	while True:
		while True:
			if currentPlayer == player1:
				centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, DisplayMenu(currentSelectedNb, player1, matchs))
			else:
				centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, DisplayMenu(currentSelectedNb, player2, matchs))
			currChar = sys.stdin.read(1)
			if currChar == '\x1b':
				currChar = sys.stdin.read(1)
				currChar = sys.stdin.read(1)
				if currChar == 'A' and currentSelectedNb != 1:
					currentSelectedNb -= 1
				if currChar == 'B' and currentSelectedNb != 3:
					currentSelectedNb += 1
			elif currChar == 'q' or currChar == 'Q':
				return
			elif currChar == '\n':
				matchs = matchs - currentSelectedNb
				if matchs == 0:
					displayEmptySquare()
					if currentPlayer == player1:
						centerText(f"{player2} a gagné")
						addPoint(player2, 2)
					else:
						centerText(f"{player1} a gagné")
						addPoint(player1, 2)
					sleep(1)
					return
				elif matchs < 0:
					matchs = matchs + currentSelectedNb
				else:
					if currentPlayer == player1:
						currentPlayer = player2
					else:
						currentPlayer = player1