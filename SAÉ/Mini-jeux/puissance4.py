from os import get_terminal_size
import sys
from colorama import Fore, Back

from termUtils import displayEmptySquare, centerTextAtLine, printAt

def checker(grid : list[list[str]],  posY : int, posX : int) -> bool:
	count : int
	
	count = 0
	i = 1

	while ((posX - i) >= 0):
		if grid[posY][posX - i] != grid[posY][posX]:
			break
		else:
			i += 1
			count += 1
	i = 1
	while ((posX + i) <= 7):
		if grid[posY][posX + i] != grid[posY][posX]:
			break
		else:
			i += 1
			count += 1

	i = 1
	while ((posY - i) >= 0):
		if grid[posY - i][posX] != grid[posY][posX]:
			break
		else:
			i += 1
			count += 1
	i = 1
	while ((posY + i) <= 6):
		if grid[posY + i][posX] != grid[posY][posX]:
			break
		else:
			i += 1
			count += 1
	
	i = 1
	while ((posY - i) >= 0 and (posX - i) >= 0):
		if grid[posY - i][posX - i] != grid[posY][posX]:
			break
		else:
			i += 1
			count += 1
	i = 1
	while ((posY + i) <= 6 and (posX + i) <= 7):
		if grid[posY + i][posX + i] != grid[posY][posX]:
			break
		else:
			i += 1
			count += 1

	if count >= 3:
		return True
	else:
		return False

def DisplaySelectedPlayer(currentPlayer : int, player1 : str, player2: str) -> str:
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
		centerTextAtLine(13, "| Qui commence ? |")
		centerTextAtLine(14, "└────────────────┘")
		printAt((maxHeight // 2) + currentPlayer - 3, maxWidth // 2 - len(player1) - 1, DisplaySelectedPlayer(currentPlayer, player1, player2))
		currChar = sys.stdin.read(1)
		if currChar == '\x1b':
			currChar = sys.stdin.read(1)
			currChar = sys.stdin.read(1)
			if currChar == 'A' and currentPlayer != 1:
				currentPlayer -= 1
			if currChar == 'B' and currentPlayer != 2:
				currentPlayer += 1
		if currChar == '\n':
			break
		elif currChar == 'q' or currChar == 'Q':
			return 0
	if currentPlayer == 1:
		return 1
	else:
		return 2

def start(player1 : str, player2 : str):
	grid : list[list[str]]

	grid = [[" " for i in range(8)] for j in range(7)]
	currentPlayer = selectPlayer(player1, player2)
	

