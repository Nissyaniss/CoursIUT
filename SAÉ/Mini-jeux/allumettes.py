from colorama import Fore, Back
from time import sleep
from os import get_terminal_size

from players import addPoint
from termUtils import displayEmptySquare, centerTextAtLine, centerText, printAt, getKey

def displayMenu(currentSelectedNb : int, player : str, matchs : int) -> str:
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

def displaySelectedPlayer(currentPlayer : int, player1 : str, player2: str) -> str:
	maxWidth : int
	maxHeight : int

	maxWidth = get_terminal_size().columns - 3
	maxHeight = get_terminal_size().lines - 3
	
	if currentPlayer == 1:
		printAt(maxHeight // 2 - 1, maxWidth // 2 - len(player1) * 2 + 1, " " * len(player2) + player2)
		return str(">" + Fore.BLACK + Back.WHITE + player1 + Fore.RESET + Back.RESET + len(player1) * " ")
	elif currentPlayer == 2:
		printAt(maxHeight // 2 - 2, maxWidth // 2 - len(player1) * 2 + 1, " " * len(player1) + player1)
		return str(">" + Fore.BLACK + Back.WHITE + player2 + Fore.RESET + Back.RESET + len(player2) * " ")
	else :
		return "ERROR"

def selectPlayer(player1 : str, player2 : str) -> int:
	currentPlayer : int
	maxWidth : int
	maxHeight : int

	maxWidth = get_terminal_size().columns - 3
	maxHeight = get_terminal_size().lines - 3
	currentPlayer = 1
	
	displayEmptySquare()
	while True:
		centerTextAtLine(12, "┌────────────────┐")
		centerTextAtLine(13, "│ Qui commence ? │")
		centerTextAtLine(14, "└────────────────┘")
		printAt((maxHeight // 2) + currentPlayer - 3, maxWidth // 2 - len(player1) - 1, displaySelectedPlayer(currentPlayer, player1, player2))
		currChar = getKey()
		if currChar == "UP" and currentPlayer != 1:
			currentPlayer -= 1
		if currChar == "DOWN" and currentPlayer != 2:
			currentPlayer += 1
		if currChar == "ENTER":
			break
		elif currChar == "TAB":
			return 0
	if currentPlayer == 1:
		return 1
	else:
		return 2

def start(player1 : str, player2 : str) -> None:
	matchs : int
	currChar : str
	currentSelectedNb : int
	currentPlayer : int
	maxHeight : int

	maxHeight = get_terminal_size().lines - 3
	currentPlayer = selectPlayer(player1, player2)
	matchs = 20
	currChar = ""
	currentSelectedNb = 1

	if currentPlayer == 0:
		return
	displayEmptySquare()
	while True:
		while True:
			if currentPlayer == 1:
				centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, displayMenu(currentSelectedNb, player1, matchs))
			else:
				centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, displayMenu(currentSelectedNb, player2, matchs))
			currChar = getKey()
			if currChar == "UP" and currentSelectedNb != 1:
				currentSelectedNb -= 1
			if currChar == "UP" and currentSelectedNb != 3:
				currentSelectedNb += 1
			elif currChar == "TAB":
				return
			elif currChar == "ENTER":
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
					if currentPlayer == 1:
						currentPlayer = 2
					else:
						currentPlayer = 1