import termios
import tty
from os import system, get_terminal_size, path
from typing import Any
import sys

def printAt(line : int, column : int, message : str) -> None:
	"""
	Affiche un message à une position donnée

	Entrée : line : int
	line symbolise la ligne ou l'on veux écrire

	Entrée : column : int
	column symbolise la colonne ou l'on veux écrire

	Entrée : message : str
	message symbolise le message
	"""
	print(f"\x1b[{line};{column}f" + message, end='', flush=True)

def setCursorPosition(line : int, column : int) -> None:
	"""
	Déplace le curseur à une position donnée

	Entrée : line : int
	line symbolise la ligne ou l'on veux déplacer le curseur

	Entrée : column : int
	column symbolise la colonne ou l'on veux déplacer le curseur
	"""
	print(f"\x1b[{line};{column}f", end='', flush=True)

def restoreTerm(original: list[Any]) -> None:
	"""
	Réinitialise le terminal à son état d'origine

	Entrée : original : list[Any]
	original symbolise les paramètres du terminal avant l'initialisation du jeu
	"""
	termios.tcsetattr(1, termios.TCSADRAIN, original)
	print("\x1b[?25h")
	system("clear")
	exit()

def setup() -> list[Any]:
	"""
	Initialise le terminal

	Sortie : original : list[Any]
	original symbolise les paramètres du terminal avant l'initialisation du jeu
	"""
	original: list[Any]
	new: list[Any]
	if not path.exists("players.json"): # Si le fichier n'existe pas
		f = open("players.json", "x+") # Crée le fichier
		f = open("players.json", 'w')
		f.write("{\n}")
		f.close()

	original = termios.tcgetattr(1) # Récupère les paramètres du terminal
	new = original[:] # Copie les paramètres du terminal

	new[tty.LFLAG] &= ~(termios.ECHO | termios.ICANON) # Modifie les paramètres du terminal, pour qu'il n'echo pas les caractères et qu'il n'attende pas d'appuyer sur entrée

	new[tty.CC][termios.VMIN] = 1 # Modifie les paramètres du terminal, pour qu'il n'attende prennent 1 caractère à la fois
	new[tty.CC][termios.VTIME] = 0 # Modifie les paramètres du terminal, pour qu'il n'attende pas de temps

	termios.tcsetattr(1, termios.TCSADRAIN, new) # Met en place les nouveaux paramètres du terminal actuel

	print("\x1b[?25l")
	system("clear")

	return original

def displayEmptySquare() -> None:
	"""
	Affiche un carré vide
	"""
	maxWidth : int
	maxHeight : int

	maxWidth = get_terminal_size().columns - 3 # Récupère la taille du terminal
	maxHeight = get_terminal_size().lines - 3

	system("clear")
	printAt(1, 1, "╔" + "═" * maxWidth +"╗") # Affiche un carré vide
	print()
	for i in range(0, maxHeight) :
		print("║"+ " " * maxWidth + "║")
	print("╚" + "═" * maxWidth +"╝")
	printAt(maxHeight + 1, 3, "Appuyer sur \"TAB\" pour quitter") # Affiche le message pour quitter

def centerTextAtLine(line : int, text : str) -> None:
	"""
	Affiche un message centré à une ligne donnée

	Entrée : line : int
	line symbolise la ligne ou l'on veux écrire

	Entrée : text : str
	text symbolise le message que l'on veux écrire
	"""
	width : int
	lenText : int

	width = get_terminal_size().columns - 3
	lenText = len(StripANSIColors(text)) # Récupère la taille du message sans les couleurs

	printAt(line, (width - lenText) // 2, text)

def centerText(text : str) -> None:
	"""
	Affiche un message centré

	Entrée : text : str
	text symbolise le message que l'on veux écrire
	"""
	width : int
	lenText : int
	height : int

	width = get_terminal_size().columns - 3
	height = get_terminal_size().lines - 3
	lenText = len(StripANSIColors(text)) # Récupère la taille du message sans les couleurs

	printAt(height // 2, (width - lenText) // 2, text)

def StripANSIColors(string : str) -> str:
	"""
	Enlève les couleurs ANSI d'une chaîne de caractères

	Entrée : string : str
	string symbolise la chaîne de caractères ou l'on veux enlever les couleurs
	"""
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
	"""
	Récupère la touche appuyée

	Sortie : str
	La touche appuyée
	"""
	char : str
	result : str

	char = sys.stdin.read(1)
	result = ""

	if char == '\x1b': # Si la touche appuyée est une touche spéciale
		char = sys.stdin.read(1)
		char = sys.stdin.read(1)
		if char == 'A': # Si la touche appuyée est la flèche du haut
			result = "UP"
		elif char == 'B': # Si la touche appuyée est la flèche du bas
			result = "DOWN"
		elif char == 'C': # Si la touche appuyée est la flèche de droite
			result = "RIGHT"
		elif char == 'D': # Si la touche appuyée est la flèche de gauche
			result = "LEFT"
		else : # Si la touche appuyée est une touche spéciale mais qu'elle ne m'intéresse pas
			result = "NONE"
	elif char == '\n': # Si la touche appuyée est entrée
		result = "ENTER"
	elif char == '\x7f': # Si la touche appuyée est backspace
		result = "BACKSPACE"
	elif char == '\t': # Si la touche appuyée est tab
		result = "TAB"
	else: # Si la touche appuyée est quelque chose d'autre
		result = char

	return result
