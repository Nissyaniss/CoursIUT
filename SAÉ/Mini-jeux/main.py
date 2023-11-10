from os import system, get_terminal_size
from colorama import Fore, Back
import sys

from morpion import start as morpion
from allumettes import start as allumettes
from rules import start as rules
from puissance4 import start as puissance4
from devinette import start as devinette
from termUtils import printAt, setup, restoreTerm, displayEmptySquare, centerTextAtLine, setCursorPosition, getKey
from players import addPlayer, isPlayerExisting, printScoreboard

def DisplayMenu(currentSelectedGame : int) -> None:
	maxWidth : int
	
	maxWidth = get_terminal_size().columns - 3
	
	displayEmptySquare()
	printAt(2, 5, "┌────────────┐")
	printAt(3, 5, "│ SCOREBOARD │")
	printAt(4, 5, "└────────────┘")
	printScoreboard(player1, player2)
	printAt(2, maxWidth - 11, "┌──────────┐")
	printAt(3, maxWidth - 11, "│  RÈGLES  │")
	printAt(4, maxWidth - 11, "└──────────┘")
	centerTextAtLine(6, "┌─────────────────────────┐")
	centerTextAtLine(7, "│         BONJOUR         │")
	centerTextAtLine(8, "│   Liste des mini-jeux   │")
	centerTextAtLine(9, "└─────────────────────────┘")
	printAt(10 + currentSelectedGame, (maxWidth - 11) // 2, DisplayGameSelected(currentSelectedGame))

def DisplayGameSelected(currentSelectedGame : int) -> str:
	gameStr: str
	maxWidth = get_terminal_size().columns - 3

	if currentSelectedGame == 1:
		gameStr = "Devinette"
		printAt(12, (maxWidth - 11) // 2, "  Allumette")
		printAt(13, (maxWidth - 11) // 2, "  Morpion")
		printAt(14, (maxWidth - 11) // 2, "  Puissance 4")
		printAt(3, maxWidth - 9, " RÈGLES")
	elif currentSelectedGame == 2:
		printAt(11, (maxWidth - 11) // 2, "  Devinette")
		gameStr = "Allumette"
		printAt(13, (maxWidth - 11) // 2, "  Morpion")
		printAt(14, (maxWidth - 11) // 2, "  Puissance 4")
		printAt(3, maxWidth - 9, " RÈGLES" )
	elif currentSelectedGame == 3:
		printAt(11, (maxWidth - 11) // 2, "  Devinette")
		printAt(12, (maxWidth - 11) // 2, "  Allumette")
		gameStr = "Morpion"
		printAt(14, (maxWidth - 11) // 2, "  Puissance 4")
		printAt(3, maxWidth - 9, " RÈGLES")
	elif currentSelectedGame == 4:
		printAt(11, (maxWidth - 11) // 2, "  Devinette")
		printAt(12, (maxWidth - 11) // 2, "  Allumette")
		printAt(13, (maxWidth - 11) // 2, "  Morpion")
		gameStr = "Puissance 4" 
		printAt(3, maxWidth - 9, " RÈGLES")
	elif currentSelectedGame == -1:
		printAt(11, (maxWidth - 11) // 2, "  Devinette")
		printAt(12, (maxWidth - 11) // 2, "  Allumette")
		printAt(13, (maxWidth - 11) // 2, "  Morpion")
		printAt(14, (maxWidth - 11) // 2, "  Puissance 4")
		gameStr = "RÈGLES"
	else :
		gameStr = "ERROR"

	return str(">" + Back.WHITE + Fore.BLACK + gameStr + Back.RESET + Fore.RESET + "  ")

def DisplayMenuPlayer(player : int) -> None:
	system("clear")
	displayEmptySquare()
	printAt(maxHeight + 1, 3, "Appuyer sur \"TAB\" pour quitter")
	centerTextAtLine(6, "┌──────────────────────────────────┐")
	centerTextAtLine(7, "│              BONJOUR             │")
	centerTextAtLine(8, f"│   Entrez votre pseudo joueur {player}   │")
	centerTextAtLine(9, "└──────────────────────────────────┘")
	centerTextAtLine(11, "Votre pseudo :")

if __name__ == "__main__":
	player1 : str
	player2 : str
	currChar : str
	isOnRules : bool
	maxWidth : int
	maxHeight : int
	original : list[int]
	currentSelectedGame : int

	player1 = ""
	player2 = ""
	isOnRules  = False
	currChar = ""
	maxWidth = get_terminal_size().columns - 3
	maxHeight = get_terminal_size().lines - 3
	currentSelectedGame = 1
	original = setup()

	pseudo = "> "

	DisplayMenuPlayer(1)
	centerTextAtLine(13, pseudo)
	while True:
		setCursorPosition(12, maxWidth // 2 + 4)
		currChar = getKey()
		if len(currChar) == 1 and currChar.isprintable():
			pseudo += currChar
			centerTextAtLine(13, pseudo)
		elif currChar == "ENTER" and len(pseudo) > 2:
			break
		elif currChar == "BACKSPACE" and len(pseudo) > 2:
			centerTextAtLine(13, " " * len(pseudo))
			pseudo = pseudo[:-1]
			centerTextAtLine(13, pseudo)
		elif currChar == "TAB":
			restoreTerm(original)
		else:
			continue
	player1 = pseudo[2:]
	if not isPlayerExisting(player1):
		addPlayer(player1)
	pseudo = "> "
	player2 = player1

	DisplayMenuPlayer(2)
	centerTextAtLine(13, pseudo)
	while player2 == player1:
		setCursorPosition(12, maxWidth // 2 + 4)
		currChar = getKey()
		if len(currChar) == 1 and currChar.isprintable():
			pseudo += currChar
			centerTextAtLine(13, pseudo)
		elif currChar == "ENTER" and len(pseudo) > 0:
			break
		elif currChar == "BACKSPACE" and len(pseudo) > 2:
			centerTextAtLine(13, " " * len(pseudo))
			pseudo = pseudo[:-1]
			centerTextAtLine(13, pseudo)
		elif currChar == "TAB":
			restoreTerm(original)
		elif len(currChar) > 1:
			continue
		else:
			restoreTerm(original)
	player2 = pseudo[2:]
	if not isPlayerExisting(player2):
		addPlayer(player2)

	while True:
		DisplayMenu(currentSelectedGame)
		while True:
			currChar = getKey()
			if currChar == "UP" and currentSelectedGame != 1 and isOnRules == False:
				currentSelectedGame -= 1
				printAt(10 + currentSelectedGame, (maxWidth - 11) // 2, DisplayGameSelected(currentSelectedGame))
			if currChar == "DOWN" and currentSelectedGame != 4 and isOnRules == False:
				currentSelectedGame += 1
				printAt(10 + currentSelectedGame, (maxWidth - 11) // 2, DisplayGameSelected(currentSelectedGame))
			if currChar == "RIGHT" and isOnRules == False:
				printAt(3, maxWidth - 9, DisplayGameSelected(-1))
				isOnRules = True
			if currChar == "LEFT" and isOnRules:
				printAt(10 + currentSelectedGame, (maxWidth - 11) // 2, DisplayGameSelected(currentSelectedGame))
				isOnRules = False
			elif currChar == "TAB":
				restoreTerm(original)
			elif currChar == "ENTER":
				break
			else:
				continue
		if isOnRules:
			rules(1, player1, player2)
			isOnRules = False
		elif currentSelectedGame == 1:
			devinette(player1, player2)
			print("\x1b[?25l", end='', flush=True)
		elif currentSelectedGame == 2:
			allumettes(player1, player2)
		elif currentSelectedGame == 3:
			morpion(player1, player2)
		elif currentSelectedGame == 4:
			puissance4(player1, player2)