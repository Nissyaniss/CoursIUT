import sys
from colorama import Fore, Back

from termUtils import displayEmptySquare, centerTextAtLine

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


def start(player1 : str, player2: str):
	grid : list[list[str]]
	currentSelectedCase : int
	currChar : str

	grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
	currentSelectedCase = 1
	currChar = ''

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
			elif currChar == '\n':
				grid[(currentSelectedCase - 1) // 3][(currentSelectedCase - 1) % 3] = '×'
			elif currChar == 'q' or currChar == 'Q':
				return
			
# ×○