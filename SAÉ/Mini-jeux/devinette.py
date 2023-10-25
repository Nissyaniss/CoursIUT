from colorama import Fore, Back
from os import system, get_terminal_size
from termUtils import setCursorPosition, displayEmptySquare, printAt
import sys
from players import addPoint
from time import sleep

def DisplayMenuMaster() -> None:
	maxSize : tuple[int, int]

	maxSize = displayEmptySquare()

	printAt(6, (maxSize[0] - 32) // 2, "┌──────────────────────────────┐")
	printAt(7, (maxSize[0] - 32) // 2, "│   Quelle est la réponse ?    │")
	printAt(8, (maxSize[0] - 32) // 2, "└──────────────────────────────┘")
	printAt(maxSize[1] + 1, 3, "Appuyer sur \"q\" pour quitter")
	print()

def DisplaySelectedOption(currentSelectedOption : int) -> str:
	optionStr: str
	maxWidth : int

	maxWidth = get_terminal_size().columns - 3

	if currentSelectedOption == 1:
		optionStr = "Plus Grand"
		printAt(12, (maxWidth - 7) // 2, "  Plus Petit")
		printAt(13, (maxWidth - 7) // 2, "  C'est Bon !")
	elif currentSelectedOption == 2:
		printAt(11, (maxWidth - 7) // 2, "  Plus Grand")
		optionStr = "Plus Petit"
		printAt(13, (maxWidth - 7) // 2, "  C'est Bon !")
	elif currentSelectedOption == 3:
		printAt(11, (maxWidth - 7) // 2, "  Plus Grand")
		printAt(12, (maxWidth - 7) // 2, "  Plus Petit")
		optionStr = "C'est Bon !"
	else :
		optionStr = "ERROR"
	print()

	return str(">" + Back.WHITE + Fore.BLACK + optionStr + Back.RESET + Fore.RESET + "  ")

def DisplayMenuPlayer() -> None:
	maxSize : tuple[int, int]

	maxSize = displayEmptySquare()

	printAt(6, (maxSize[0] - 32) // 2, "┌─────────────────────────────────┐")
	printAt(7, (maxSize[0] - 32) // 2, "│   Qui fera deviner a l'autre    │")
	printAt(8, (maxSize[0] - 32) // 2, "└─────────────────────────────────┘")
	printAt(maxSize[1] + 1, 3, "Appuyer sur \"q\" pour quitter")
	print()

def DisplaySelectedPlayer(currentSelectedPlayer : int, player1 : str, player2 : str) -> str:
	playerStr: str
	maxWidth : int

	maxWidth = get_terminal_size().columns - 3

	if currentSelectedPlayer == 1:
		playerStr = player1
		printAt(12, (maxWidth - 7) // 2, "  " + player2)
	elif currentSelectedPlayer == 2:
		printAt(11, (maxWidth - 7) // 2, "  " + player1)
		playerStr = player2
	else :
		playerStr = "ERROR"
	print()

	return str(">" + Back.WHITE + Fore.BLACK + playerStr + Back.RESET + Fore.RESET + "  ")

def DisplayWinMenu(winner : str) -> None:
	"""
	La fonction DisplayWinMenu affiche un menu pour le gagnant d'une partie.
	
	@param winner Le paramètre gagnant est une chaîne qui représente le nom du gagnant.
	"""

	maxSize : tuple[int, int]

	maxSize = displayEmptySquare()

	printAt(maxSize[1] // 2, (maxSize[0] - len(f"{winner} a gagné")) // 2, f"{winner} a gagné")
	print()

def start(player1 : str, player2 : str) -> None:
	solution : str
	guess : str
	currChar : str
	count : int
	currentSelectedOption : int
	maxWidth : int
	strikes : int
	currentSelectedPlayer : int
	master : str
	maxTries : int
	tries : int

	maxWidth = get_terminal_size().columns - 3
	currentSelectedOption = 1
	currentSelectedPlayer = 1
	master = ''
	guesser = ''
	solution = ''
	guess = ''
	currChar = ""
	count = 0
	strikes = 0
	maxTries = 15
	tries = 0

	system("clear")
	displayEmptySquare()
	DisplayMenuPlayer()
	while True:
		printAt(10 + currentSelectedPlayer, (maxWidth - 7) // 2, DisplaySelectedPlayer(currentSelectedPlayer, player1, player2))
		currChar = sys.stdin.read(1)
		if currChar == '\x1b':
			currChar = sys.stdin.read(1)
			currChar = sys.stdin.read(1)
			if currChar == 'A' and currentSelectedPlayer != 1:
				printAt(10 + currentSelectedPlayer - 1, (maxWidth - 7) // 2, DisplaySelectedPlayer(currentSelectedPlayer - 1, player1, player2))
				currentSelectedPlayer -= 1
			if currChar == 'B' and currentSelectedPlayer != 2:
				printAt(10 + currentSelectedPlayer + 1, (maxWidth - 7) // 2, DisplaySelectedPlayer(currentSelectedPlayer + 1, player1, player2))
				currentSelectedPlayer += 1
		if currChar == '\n':
			break
		elif currChar == 'q' or currChar == 'Q':
			return
		print(end='', flush=True)
	if currentSelectedPlayer == 1:
		master = player1
		guesser = player2
	else:
		master = player2
		guesser = player1
	print("\x1b[?25h", end='')
	displayEmptySquare()
	printAt(2, 3, "Nombre : " + Back.BLACK)
	print(Back.RESET ,end='', flush=True)
	while True:
		currChar = sys.stdin.read(1)
		if currChar.isdigit() and count < 3:
			printAt(2, 12 + count, currChar)
			setCursorPosition(2, 13 + count)
			solution = solution + currChar
			count = count + 1
		elif currChar == '\n':
			break
		elif currChar == 'q' or currChar == 'Q':
			return
		elif currChar == '\x7f':
			if count != 0:
				printAt(2, 11 + count, " ")
				count = count - 1
				setCursorPosition(2, 12 + count)
				solution = solution[:-1]
		print(end='', flush=True)
	while guess != solution:
		displayEmptySquare()
		printAt(2, 3, "Devinez : " + count * " ")
		setCursorPosition(2, 14)
		count = 0
		while True:
			currChar = sys.stdin.read(1)
			if currChar.isdigit():
				printAt(2, 13 + count, currChar)
				setCursorPosition(2, 14 + count)
				guess = guess + currChar
				count = count + 1
			elif currChar == '\n' and count > 0:
				break
			elif currChar == 'q' or currChar == 'Q':
				return
			elif currChar == '\x7f':
				if count != 0:
					printAt(2, 12 + count, " ")
					count = count - 1
					setCursorPosition(2, 13 + count)
					solution = solution[:-1]
			print(end='', flush=True)
		DisplayMenuMaster()
		printAt(10 + currentSelectedOption, (maxWidth - 7) // 2, DisplaySelectedOption(currentSelectedOption))
		print("\x1b[?25l", end='', flush=True)
		while True:
			currChar = sys.stdin.read(1)
			if currChar == '\x1b':
				currChar = sys.stdin.read(1)
				currChar = sys.stdin.read(1)
				if currChar == 'A' and currentSelectedOption != 1:
					printAt(10 + currentSelectedOption - 1, (maxWidth - 7) // 2, DisplaySelectedOption(currentSelectedOption - 1))
					currentSelectedOption -= 1
				if currChar == 'B' and currentSelectedOption != 3:
					printAt(10 + currentSelectedOption + 1, (maxWidth - 7) // 2, DisplaySelectedOption(currentSelectedOption + 1))
					currentSelectedOption += 1
				print()
			elif currChar == 'q' or currChar == 'Q':
				return
			elif currChar == '\n':
				print("\x1b[?25h", end='', flush=True)
				break
		tries = tries + 1
		if currentSelectedOption == 1 and guess < solution:
			strikes += 1
		elif currentSelectedOption == 2 and guess > solution:
			strikes =+ 1
		elif (currentSelectedOption == 1 or currentSelectedOption == 2) and guess == solution:
			strikes = 3
		if strikes == 3:
			DisplayWinMenu(guesser)
			sleep(1)
			addPoint(guesser, 1)
			print("\x1b[?25l", end='', flush=True)
			return
		if tries == maxTries:
			DisplayWinMenu(master)
			addPoint(master, 1)
			print("\x1b[?25l", end='', flush=True)
			return
	print("\x1b[?25l", end='', flush=True)


