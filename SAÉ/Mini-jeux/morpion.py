from colorama import Fore, Back
from time import sleep
from os import get_terminal_size

from termUtils import displayEmptySquare, centerTextAtLine, centerText, printAt, getKey
from players import addPoint

def displayGrid(grid : list[list[str]], currentSelectedCase : int, currentPlayer : int, player1 : str, player2: str):
	displayEmptySquare()
	if currentPlayer == 1:
		centerTextAtLine(13, f"C'est actuellement au tour de : {player1}" + len(player2) * " ")
	elif currentPlayer == 2:
		centerTextAtLine(13, f"C'est actuellement au tour de : {player2}" + len(player1) * " ")
	centerTextAtLine(15, f" {grid[0][0]} │ {grid[0][1]} │ {grid[0][2]} ")
	centerTextAtLine(16, "───┼───┼───")
	centerTextAtLine(17, f" {grid[1][0]} │ {grid[1][1]} │ {grid[1][2]}")
	centerTextAtLine(18, "───┼───┼───")
	centerTextAtLine(19, f" {grid[2][0]} │ {grid[2][1]} │ {grid[2][2]}")

	if currentSelectedCase == 1:
		centerTextAtLine(15, " " + Fore.BLACK + Back.WHITE + f"{grid[0][0]}" + Fore.RESET + Back.RESET + f" │ {grid[0][1]} │ {grid[0][2]} ")
	elif currentSelectedCase == 2:
		centerTextAtLine(15, f" {grid[0][0]} │ " + Fore.BLACK + Back.WHITE +  f"{grid[0][1]}" + Fore.RESET + Back.RESET +f" │ {grid[0][2]} ")
	elif currentSelectedCase == 3:
		centerTextAtLine(15, f" {grid[0][0]} │ {grid[0][1]} │ "+ Fore.BLACK + Back.WHITE + f"{grid[0][2]}" + Fore.RESET + Back.RESET + " ")

	elif currentSelectedCase == 4:
		centerTextAtLine(17, " " + Fore.BLACK + Back.WHITE + f"{grid[1][0]}" + Fore.RESET + Back.RESET + f" │ {grid[1][1]} │ {grid[1][2]} ")
	elif currentSelectedCase == 5:
		centerTextAtLine(17, f" {grid[1][0]} │ " + Fore.BLACK + Back.WHITE +  f"{grid[1][1]}" + Fore.RESET + Back.RESET +f" │ {grid[1][2]} ")
	elif currentSelectedCase == 6:
		centerTextAtLine(17, f" {grid[1][0]} │ {grid[1][1]} │ "+ Fore.BLACK + Back.WHITE + f"{grid[1][2]}" + Fore.RESET + Back.RESET + " ")
	
	elif currentSelectedCase == 7:
		centerTextAtLine(19, " " + Fore.BLACK + Back.WHITE + f"{grid[2][0]}" + Fore.RESET + Back.RESET + f" │ {grid[2][1]} │ {grid[2][2]} ")
	elif currentSelectedCase == 8:
		centerTextAtLine(19, f" {grid[2][0]} │ " + Fore.BLACK + Back.WHITE +  f"{grid[2][1]}" + Fore.RESET + Back.RESET +f" │ {grid[2][2]} ")
	elif currentSelectedCase == 9:
		centerTextAtLine(19, f" {grid[2][0]} │ {grid[2][1]} │ "+ Fore.BLACK + Back.WHITE + f"{grid[2][2]}" + Fore.RESET + Back.RESET + " ")

def checkWin(grid : list[list[str]]) -> bool:
	if grid[0][0] == grid[0][1] == grid[0][2] != ' ': # Horizontal 1
		return True
	elif grid[1][0] == grid[1][1] == grid[1][2] != ' ': # Horizontal 2
		return True
	elif grid[2][0] == grid[2][1] == grid[2][2] != ' ': # Horizontal 3
		return True
	elif grid[0][0] == grid[1][0] == grid[2][0] != ' ': # Vertical 1
		return True
	elif grid[0][1] == grid[1][1] == grid[2][1] != ' ': # Vertical 2
		return True
	elif grid[0][2] == grid[1][2] == grid[2][2] != ' ': # Vertical 3
		return True
	elif grid[0][0] == grid[1][1] == grid[2][2] != ' ': # Diagonal 1
		return True
	elif grid[0][2] == grid[1][1] == grid[2][0] != ' ': # Diagonal 2
		return True
	else:
		return False

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
		centerTextAtLine(13, "| Qui commence ? |")
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


def start(player1 : str, player2: str):
	grid : list[list[str]]
	currentCase : int
	currChar : str
	currentPlayer : int

	grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
	currentCase = 1
	currChar = ''
	currentPlayer = selectPlayer(player1, player2)

	if currentPlayer == 0:
		return
	while True:
		while True:
			displayGrid(grid, currentCase, currentPlayer, player1, player2)
			currChar = getKey()
			if currChar == "UP":
				if currentCase > 3:
					currentCase -= 3
			if currChar == "DOWN":
				if currentCase < 7:
					currentCase += 3
			if currChar == "RIGHT":
				if currentCase != 9:
					currentCase += 1
			if currChar == "LEFT":
				if currentCase != 1:
					currentCase -= 1
			elif currChar == "ENTER" and grid[(currentCase - 1) // 3][(currentCase - 1) % 3] == ' ': 
				if currentPlayer == 1:
					grid[(currentCase - 1) // 3][(currentCase - 1) % 3] = '×'
					currentPlayer = 2
				elif currentPlayer == 2:
					grid[(currentCase - 1) // 3][(currentCase - 1) % 3] = '○'
					currentPlayer = 1
				if checkWin(grid) == True:
					if currentPlayer == 1:
						displayEmptySquare()
						centerText(f"{player2} a gagné")
						addPoint(player2, 3)
						sleep(1)
						return
					elif currentPlayer == 2:
						displayEmptySquare()
						centerText(f"{player1} a gagné")
						addPoint(player1, 3)
						sleep(1)
						return
				elif grid[0][0] != ' ' and grid[0][1] != ' ' and grid[0][2] != ' ' and grid[1][0] != ' ' and grid[1][1] != ' ' and grid[1][2] != ' ' and grid[2][0] != ' ' and grid[2][1] != ' ' and grid[2][2] != ' ':
					displayEmptySquare()
					centerText("Égalité")
					sleep(1)
					return
			elif currChar == "TAB":
				return