from os import get_terminal_size
import sys
from colorama import Fore, Back
from time import sleep

from termUtils import displayEmptySquare, centerTextAtLine, printAt, centerText
from players import addPoint

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

	if count < 3:
		count = 0
	i = 1
	while ((posY - i) >= 0) and count < 3:
		if grid[posY - i][posX] != grid[posY][posX]:
			break
		else:
			i += 1
			count += 1
	i = 1
	while ((posY + i) <= 6) and count < 3:
		if grid[posY + i][posX] != grid[posY][posX]:
			break
		else:
			i += 1
			count += 1
	
	if count < 3:
		count = 0
	i = 1
	while ((posY + i) <= 6 and (posX - i) >= 0) and count < 3:
		if grid[posY + i][posX - i] != grid[posY][posX]:
			break
		else:
			i += 1
			count += 1
	i = 1
	while ((posY - i) >= 0 and (posX + i) <= 7) and count < 3:
		if grid[posY - i][posX + i] != grid[posY][posX]:
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
		centerTextAtLine(13, "│ Qui commence ? │")
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

def displayGrid(grid : list[list[str]], currentCase : int):
	maxWidth : int
	maxHeight : int
	i : int
	j : int

	maxWidth = get_terminal_size().columns - 3
	maxHeight = get_terminal_size().lines - 3
	i = 0
	j = 0
	while i < 7:
		while j < 8:
			if currentCase == j and i <= 0:
				printAt(maxHeight // 2 - 3 + i, maxWidth // 2 - 3 + j * 2,"│" + Back.WHITE + Fore.BLACK + grid[i][j] + Back.RESET + Fore.RESET + "│")
			else:
				printAt(maxHeight // 2 - 3 + i, maxWidth // 2 - 3 + j * 2, "│" + grid[i][j] + "│")
			j += 1
		j = 0
		i += 1

def start(player1 : str, player2 : str):
	grid : list[list[str]]
	currentPlayer : int
	currChar : str
	currentCase : int

	grid = [[" " for i in range(8)] for j in range(7)]
	currentPlayer = selectPlayer(player1, player2)
	currChar = ""
	currentCase = 0

	displayEmptySquare()
	while True:
		while True:
			displayGrid(grid, currentCase)
			currChar = sys.stdin.read(1)
			if currChar == '\x1b':
				currChar = sys.stdin.read(1)
				currChar = sys.stdin.read(1)
				if currChar == 'C' and currentCase < 7:
					currentCase += 1
				if currChar == 'D' and currentCase > 0:
					currentCase -= 1
			if currChar == '\n':
				break
			elif currChar == 'q' or currChar == 'Q':
				return
		if currentPlayer == 1 and grid[0][currentCase] == ' ':
			i = 6
			while i >= 0:
				if grid[i][currentCase] == ' ':
					grid[i][currentCase] = Fore.YELLOW + "●" + Fore.RESET
					break
				i -= 1
			if checker(grid, i, currentCase):
				displayEmptySquare()
				centerText(f"{player1} a gagné !")
				addPoint(player1, 4)
				sleep(1)
				return
			currentPlayer = 2
		elif currentPlayer == 2 and grid[0][currentCase] == ' ':
			i = 6
			while i >= 0:
				if grid[i][currentCase] == ' ':
					grid[i][currentCase] = Fore.RED + "●" + Fore.RESET
					break
				i -= 1
			if checker(grid, i, currentCase):
				displayEmptySquare()
				centerText(f"{player2} a gagné !")
				addPoint(player2, 4)
				sleep(1)
				return
			currentPlayer = 1
