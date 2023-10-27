from colorama import Fore, Back
from os import get_terminal_size
import sys
from time import sleep

from players import addPoint
from termUtils import setCursorPosition, displayEmptySquare, printAt, centerTextAtLine, centerText

def DisplayMenuMaster() -> None:
	displayEmptySquare()
	centerTextAtLine(6, "┌──────────────────────────────┐")
	centerTextAtLine(7, "│    Comment est sa réponse    │")
	centerTextAtLine(8, "└──────────────────────────────┘")

def DisplaySelectedOption(currentSelectedOption : int) -> str:
	optionStr: str

	if currentSelectedOption == 1:
		optionStr = "Plus Grand"
		centerTextAtLine(12, "  Plus Petit ")
		centerTextAtLine(13, "  C'est Bon !")
	elif currentSelectedOption == 2:
		centerTextAtLine(11, "  Plus Grand ")
		optionStr = "Plus Petit"
		centerTextAtLine(13, "  C'est Bon !")
	elif currentSelectedOption == 3:
		centerTextAtLine(11, "  Plus Grand ")
		centerTextAtLine(12, "  Plus Petit ")
		optionStr = "C'est Bon !"
	else :
		optionStr = "ERROR"
	print()

	return ">" + Back.WHITE + Fore.BLACK + optionStr + Back.RESET + Fore.RESET + "  "

def DisplayMenuPlayer() -> None:
	displayEmptySquare()
	centerTextAtLine(6, "┌─────────────────────────────────┐")
	centerTextAtLine(7, "│   Qui fera deviner à l'autre    │")
	centerTextAtLine(8, "└─────────────────────────────────┘")

def DisplaySelectedPlayer(currentSelectedPlayer : int, player1 : str, player2 : str) -> str:
	playerStr: str
	maxWidth : int

	maxWidth = get_terminal_size().columns - 3
	
	if currentSelectedPlayer == 1:
		playerStr = player1
		printAt(12, maxWidth // 2 - len(player1) + 3, "  " + player2)
	elif currentSelectedPlayer == 2:
		printAt(11, maxWidth // 2 - len(player1) + 3, "  " + player1)
		playerStr = player2
	else :
		playerStr = "ERROR"

	return str(">" + Back.WHITE + Fore.BLACK + playerStr + Back.RESET + Fore.RESET + "  ")

def start(player1 : str, player2 : str) -> None:
	solution : str
	guess : str
	currChar : str
	currentSelectedOption : int
	maxWidth : int
	maxHeight : int
	strikes : int
	currentSelectedPlayer : int
	master : str
	maxTries : int
	tries : int

	maxWidth = get_terminal_size().columns - 3
	maxHeight = get_terminal_size().lines - 3
	currentSelectedOption = 1
	currentSelectedPlayer = 1
	master = ''
	guesser = ''
	solution = ''
	guess = ''
	currChar = ""
	strikes = 0
	maxTries = 15
	tries = 0

	displayEmptySquare()
	DisplayMenuPlayer()
	while True:
		printAt(10 + currentSelectedPlayer, maxWidth // 2 - len(player1) + 3, DisplaySelectedPlayer(currentSelectedPlayer, player1, player2))
		currChar = sys.stdin.read(1)
		if currChar == '\x1b':
			currChar = sys.stdin.read(1)
			currChar = sys.stdin.read(1)
			if currChar == 'A' and currentSelectedPlayer != 1:
				currentSelectedPlayer -= 1
			if currChar == 'B' and currentSelectedPlayer != 2:
				currentSelectedPlayer += 1
		if currChar == '\n':
			break
		elif currChar == 'q' or currChar == 'Q':
			return
	if currentSelectedPlayer == 1:
		master = player1
		guesser = player2
	else:
		master = player2
		guesser = player1
	print("\x1b[?25h", end='')
	displayEmptySquare()
	centerText("Nombre : ")
	while True:
		currChar = sys.stdin.read(1)
		if currChar.isdigit() and len(solution) < 3:
			solution += currChar
		elif currChar == '\n':
			break
		elif currChar == 'q' or currChar == 'Q':
			return
		elif currChar == '\x7f':
			if len(solution) != 0:
				solution = solution[:-1]
	while True:
		displayEmptySquare()
		centerText("Devinez : " + len(solution) * " ")
		while True:
			setCursorPosition(maxHeight // 2, (maxWidth // 2 + 4) + len(guess))
			currChar = sys.stdin.read(1)
			if currChar.isdigit():
				printAt(maxHeight // 2, (maxWidth // 2 + 5) - 1 + len(guess), currChar)
				guess += currChar
			elif currChar == '\n' and len(guess) > 0:
				break
			elif currChar == 'q' or currChar == 'Q':
				return
			elif currChar == '\x7f':
				if len(guess) != 0:
					printAt(maxHeight // 2, (maxWidth // 2 + 4) - 1 + len(guess), " ")
					guess = guess[:-1]
		DisplayMenuMaster()
		print("\x1b[?25l", end='', flush=True)
		while True:
			centerTextAtLine(10 + currentSelectedOption, DisplaySelectedOption(currentSelectedOption))
			currChar = sys.stdin.read(1)
			if currChar == '\x1b':
				currChar = sys.stdin.read(1)
				currChar = sys.stdin.read(1)
				if currChar == 'A' and currentSelectedOption != 1:
					currentSelectedOption -= 1
				if currChar == 'B' and currentSelectedOption != 3:
					currentSelectedOption += 1
			elif currChar == 'q' or currChar == 'Q':
				return
			elif currChar == '\n':
				print("\x1b[?25h", end='', flush=True)
				break
		tries = tries + 1
		if currentSelectedOption == 1 and int(guess) < int(solution):
			strikes += 1
		elif currentSelectedOption == 2 and int(guess) > int(solution):
			strikes =+ 1
		elif (currentSelectedOption == 1 or currentSelectedOption == 2) and guess == solution:
			strikes = 3
		if strikes == 3:
			print("\x1b[?25l", end='', flush=True)
			displayEmptySquare()
			centerText(f"{guesser} a gagné car {master} a triché")
			addPoint(guesser, 1)
			sleep(1)
			return
		elif tries == maxTries:
			print("\x1b[?25l", end='', flush=True)
			displayEmptySquare()
			centerText(f"{master} a gagné car {guesser} n'a pas trouvé en {maxTries} essais")
			sleep(1)
			addPoint(master, 1)
			return
		elif currentSelectedOption == 3:
			print("\x1b[?25l", end='', flush=True)
			displayEmptySquare()
			centerText(f"{guesser} a gagné car il a trouvé en {tries}/{maxTries} essais")
			sleep(1)
			addPoint(guesser, 1)
			return