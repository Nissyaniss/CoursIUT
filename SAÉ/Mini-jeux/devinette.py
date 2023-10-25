from colorama import Fore, Back
from os import system, get_terminal_size
from termUtils import setCursorPosition, displayEmptySquare, printAt
import sys

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

def start(player1 : str, player2 : str) -> None:
	solution : str
	guess : str
	currChar : str
	count : int
	currentSelectedOption : int
	maxWidth : int
	strikes : int

	maxWidth = get_terminal_size().columns - 3
	currentSelectedOption = 1
	solution = ''
	guess = ''
	currChar = ""
	count = 0
	strikes = 0

	system("clear")
	displayEmptySquare()
	while True:
		currChar = sys.stdin.read(1)
		if currChar == 'A' and currentSelectedOption != 1:
			printAt(10 + currentSelectedOption - 1, (maxWidth - 7) // 2, DisplaySelectedOption(currentSelectedOption - 1))
			currentSelectedOption -= 1
		if currChar == 'B' and currentSelectedOption != 3:
			printAt(10 + currentSelectedOption + 1, (maxWidth - 7) // 2, DisplaySelectedOption(currentSelectedOption + 1))
			currentSelectedOption += 1
		if currChar == '\n':
			break
		elif currChar == 'q' or currChar == 'Q':
			return
		print(end='', flush=True)
	print("\x1b[?25h", end='')
	printAt(2, 3, "Nombre : " + Back.BLACK)
	print(Back.RESET ,end='', flush=True)
	while True:
		currChar = sys.stdin.read(1)
		if currChar.isdigit():
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
		print(end='', flush=True)
		count = 0
		while True:
			currChar = sys.stdin.read(1)
			if currChar.isdigit():
				printAt(2, 13 + count, currChar)
				setCursorPosition(2, 14 + count)
				guess = guess + currChar
				count = count + 1
			elif currChar == '\n':
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
		printAt(11, (maxWidth - 7) // 2, DisplaySelectedOption(1))
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
		if currentSelectedOption == 1 and guess < solution:
			strikes = strikes + 1
		elif currentSelectedOption == 2 and guess > solution:
			strikes = strikes + 1
		elif (currentSelectedOption == 1 or currentSelectedOption == 2) and guess == solution:
			strikes = 3
		if strikes == 3:
			break

