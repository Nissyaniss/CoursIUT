import termios
import tty
from os import system, get_terminal_size
from typing import Any
import sys

def printAt(line : int, column : int, message : str) -> None:
	"""
	La fonction `setTermCursor` définit la position du curseur dans le terminal sur une ligne et une
	colonne spécifiées, et imprime un message à cette position.
	
	@param line Le paramètre line représente le numéro de ligne où vous souhaitez définir la position du
	curseur. C'est une valeur entière.
	@param column Le paramètre `column` représente la position horizontale du curseur sur l'écran du
	terminal. C'est une valeur entière.
	@param message Le paramètre `message` est une chaîne qui représente le texte que vous
	souhaitez afficher sur la ligne et la colonne spécifiées sur le terminal. C'est une chaîne.
	"""

	print(f"\x1b[{line};{column}f" + message, end='', flush=True)

def setCursorPosition(line : int, column : int) -> None:
	print(f"\x1b[{line};{column}f", end='', flush=True)

def restoreTerm(original: list[Any]) -> None:
	"""
	La fonction `restore_term` restore le terminal comme avant le début du programme.
	
	@param original Le paramètre `original` est une liste de n'importe quel type (parce que sinon 
	le type checker comprend pas) qui symbolise l'état du terminal avant le début du programme
	"""

	termios.tcsetattr(1, termios.TCSADRAIN, original)
	print("\x1b[?25h")
	system("clear")
	exit()

def setup() -> list[Any]:
	"""
	La fonction `setup` met en place le terminal pour éviter : l'echo des touches,
	l'affichage du curseur et désactive l'obligation d'appuyer sur entrée pour lire les
	caractère rentrés.

	@return La fonction retourne original un liste de int (forcément)
	"""

	original: list[Any]
	new: list[Any]

	original = termios.tcgetattr(1)
	new = original[:]

	new[tty.LFLAG] &= ~(termios.ECHO | termios.ICANON)

	new[tty.CC][termios.VMIN] = 1
	new[tty.CC][termios.VTIME] = 0

	termios.tcsetattr(1, termios.TCSADRAIN, new)

	print("\x1b[?25l")
	system("clear")

	return original

def displayEmptySquare() -> tuple[int, int]:
	"""
	La fonction `displayEmptySquare` affiche un carré vide de la taille du terminal.

	@return La fonction retourne un tuple de deux int symbolisant respectivement 
	le nombre maximum de column utilisables et le nombre maximum de lignes utilisables
	"""

	maxWidth : int
	maxHeight : int

	maxWidth = get_terminal_size().columns - 3
	maxHeight = get_terminal_size().lines - 3

	system("clear")
	printAt(1, 1, "╔" + "═" * maxWidth +"╗")
	print()
	for i in range(0, maxHeight) :
		print("║"+ " " * maxWidth + "║")
	print("╚" + "═" * maxWidth +"╝")
	printAt(maxHeight + 1, 3, "Appuyer sur \"TAB\" pour quitter")

	return (maxWidth, maxHeight)

def centerTextAtLine(line : int, text : str) -> None:
	width : int
	lenText : int

	width = get_terminal_size().columns - 3
	lenText = len(stripANSIColors(text))

	printAt(line, (width - lenText) // 2, text)

def centerTextAtColumn(column : int, text : str) -> None:
	height : int

	height = get_terminal_size().lines - 3

	printAt(height // 2, column, text)

def centerText(text : str) -> None:
	width : int
	lenText : int
	height : int

	width = get_terminal_size().columns - 3
	height = get_terminal_size().lines - 3
	lenText = len(stripANSIColors(text))

	printAt(height // 2, (width - lenText) // 2, text)

def setCursorPositionCenterAtColumn(column : int) -> None:
	height : int

	height = get_terminal_size().lines - 3

	setCursorPosition(height // 2, column)

def setCursorPositionCenterAtLine(line : int) -> None:
	width : int

	width = get_terminal_size().columns - 3

	setCursorPosition(line, width // 2)

def stripANSIColors(string : str) -> str:
	result : str
	i : int
	j : int

	result = ""
	i = 0
	j = 0

	while i < len(string):
		if string[i] == '\x1B':
			j = i
			while string[j] != 'm':
				j += 1
			i = j + 1
		else:
			result += string[i]
			i += 1
	return result

def getKey() -> str:

	char : str
	result : str

	char = sys.stdin.read(1)
	result = ""

	if char == '\x1b':
		char = sys.stdin.read(1)
		char = sys.stdin.read(1)
		if char == 'A':
			result = "UP"
		elif char == 'B':
			result = "DOWN"
		elif char == 'C':
			result = "RIGHT"
		elif char == 'D':
			result = "LEFT"
		else :
			result = "NONE"
	elif char == '\n':
		result = "ENTER"
	elif char == '\x7f':
		result = "BACKSPACE"
	elif char == '\t':
		result = "TAB"
	else:
		result = char

	return result
