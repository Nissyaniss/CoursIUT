import sys
from colorama import Fore, Back
from time import sleep

from termUtils import displayEmptySquare, centerTextAtLine, centerText
from players import addPoint

def DisplayGrid(grid : list[list[str]], currentSelectedCase : int):
	displayEmptySquare()
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


def start(player1 : str, player2: str):
	grid : list[list[str]]
	currentSelectedCase : int
	currChar : str
	currentPlayer : int

	grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
	currentSelectedCase = 1
	currChar = ''
	currentPlayer = 1

	while True:
		while True:
			DisplayGrid(grid, currentSelectedCase)
			currChar = sys.stdin.read(1)
			if currChar == '\x1b':
				currChar = sys.stdin.read(1)
				currChar = sys.stdin.read(1)
				if currChar == 'A':
					if currentSelectedCase > 3:
						currentSelectedCase -= 3
				if currChar == 'B':
					if currentSelectedCase < 7:
						currentSelectedCase += 3
				if currChar == 'C':
					if currentSelectedCase != 9:
						currentSelectedCase += 1
				if currChar == 'D':
					if currentSelectedCase != 1:
						currentSelectedCase -= 1
			elif currChar == '\n' and grid[(currentSelectedCase - 1) // 3][(currentSelectedCase - 1) % 3] == ' ': 
				if currentPlayer == 1:
					grid[(currentSelectedCase - 1) // 3][(currentSelectedCase - 1) % 3] = '×'
					currentPlayer = 2
				elif currentPlayer == 2:
					grid[(currentSelectedCase - 1) // 3][(currentSelectedCase - 1) % 3] = '○'
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
			elif currChar == 'q' or currChar == 'Q':
				return