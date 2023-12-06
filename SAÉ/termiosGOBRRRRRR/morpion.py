from time import sleep
from os import get_terminal_size
from typing import List

from ANSIcolors import inverseColor
from termUtils import displayEmptySquare, centerTextAtLine, centerText, printAt, getKey
from players import addPoint

def displayGrid(grid : List[List[str]], currentSelectedCase : int, currentPlayer : int, player1 : str, player2: str) -> None:
	"""
	Affiche la grille du morpion

	Entrée : grid : list[list[str]]
	grid symbolise la grille du morpion

	Entrée : currentSelectedCase : int
	currentSelectedCase symbolise la case sélectionner

	Entrée : currentPlayer : int
	currentPlayer symbolise le joueur actuel

	Entrée : player1 : str
	player1 symbolise le nom du joueur 1

	Entrée : player2 : str
	player2 symbolise le nom du joueur 2
	"""
	displayEmptySquare()
	if currentPlayer == 1: # Affiche le joueur actuel
		centerTextAtLine(13, f"C'est actuellement au tour de : {player1}" + len(player2) * " ")
	elif currentPlayer == 2:
		centerTextAtLine(13, f"C'est actuellement au tour de : {player2}" + len(player1) * " ")
	centerTextAtLine(15, f" {grid[0][0]} │ {grid[0][1]} │ {grid[0][2]} ") # Affiche la grille
	centerTextAtLine(16, "───┼───┼───")
	centerTextAtLine(17, f" {grid[1][0]} │ {grid[1][1]} │ {grid[1][2]}")
	centerTextAtLine(18, "───┼───┼───")
	centerTextAtLine(19, f" {grid[2][0]} │ {grid[2][1]} │ {grid[2][2]}")

	if currentSelectedCase == 1: # Affiche la case sélectionner
		centerTextAtLine(15, " " + inverseColor(f"{grid[0][0]}") + f" │ {grid[0][1]} │ {grid[0][2]} ")
	elif currentSelectedCase == 2:
		centerTextAtLine(15, f" {grid[0][0]} │ " + inverseColor(f"{grid[0][1]}") + f" │ {grid[0][2]} ")
	elif currentSelectedCase == 3:
		centerTextAtLine(15, f" {grid[0][0]} │ {grid[0][1]} │ "+ inverseColor(f"{grid[0][2]}") + " ")

	elif currentSelectedCase == 4:
		centerTextAtLine(17, " " + inverseColor(f"{grid[1][0]}") + f" │ {grid[1][1]} │ {grid[1][2]} ")
	elif currentSelectedCase == 5:
		centerTextAtLine(17, f" {grid[1][0]} │ " + inverseColor(f"{grid[1][1]}") + f" │ {grid[1][2]} ")
	elif currentSelectedCase == 6:
		centerTextAtLine(17, f" {grid[1][0]} │ {grid[1][1]} │ "+ inverseColor(f"{grid[1][2]}") + " ")
	
	elif currentSelectedCase == 7:
		centerTextAtLine(19, " " + inverseColor(f"{grid[2][0]}") + f" │ {grid[2][1]} │ {grid[2][2]} ")
	elif currentSelectedCase == 8:
		centerTextAtLine(19, f" {grid[2][0]} │ " + inverseColor(f"{grid[2][1]}") + f" │ {grid[2][2]} ")
	elif currentSelectedCase == 9:
		centerTextAtLine(19, f" {grid[2][0]} │ {grid[2][1]} │ " + inverseColor(f"{grid[2][2]}") + " ")

def checkWin(grid : List[List[str]]) -> bool:
	"""
	Vérifie si un joueur a gagné

	Entrée : grid : list[list[str]]
	grid symbolise la grille du morpion

	Sortie : bool
	True si un joueur a gagné, False sinon
	"""
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
	"""
	Affiche le joueur sélectionner

	Entrée : currentPlayer : int
	currentPlayer symbolise le joueur actuel

	Entrée : player1 : str
	player1 symbolise le nom du joueur 1

	Entrée : player2 : str
	player2 symbolise le nom du joueur 2

	Sortie : gameStr : str
	gameStr symbolise le joueur sélectionner formaté
	"""
	maxWidth : int
	maxHeight : int

	maxWidth = get_terminal_size().columns - 3 # Récupère la taille du terminal
	maxHeight = get_terminal_size().lines - 3
	
	
	if currentPlayer == 1: # Affiche le joueur sélectionner
		printAt(maxHeight // 2 - 1, maxWidth // 2 - len(player1) * 2 + 1, " " * len(player2) + player2)
		return str(">" + inverseColor(player1) + len(player1) * " ")
	elif currentPlayer == 2:
		printAt(maxHeight // 2 - 2, maxWidth // 2 - len(player1) * 2 + 1, " " * len(player1) + player1)
		return str(">" + inverseColor(player2) + len(player2) * " ")
	else :
		return "ERROR"

def selectPlayer(player1 : str, player2 : str) -> int:
	"""
	Affiche le menu pour choisir le joueur qui commence

	Entrée : player1 : str
	player1 symbolise le joueur 1

	Entrée : player2 : str
	player2 symbolise le joueur 2

	Sortie : currentPlayer : int
	currentPlayer symbolise le joueur qui commence
	"""
	currentPlayer : int
	maxWidth : int
	maxHeight : int

	maxWidth = get_terminal_size().columns - 3 # Récupère la taille du terminal
	maxHeight = get_terminal_size().lines - 3
	currentPlayer = 1
	
	displayEmptySquare()
	while True:
		centerTextAtLine(12, "┌────────────────┐") # Affiche le menu
		centerTextAtLine(13, "│ Qui commence ? │")
		centerTextAtLine(14, "└────────────────┘")
		printAt((maxHeight // 2) + currentPlayer - 3, maxWidth // 2 - len(player1) - 1, displaySelectedPlayer(currentPlayer, player1, player2))
		currChar = getKey()
		if currChar == "UP" and currentPlayer != 1: # Change le joueur sélectionner
			currentPlayer -= 1
		if currChar == "DOWN" and currentPlayer != 2: # Change le joueur sélectionner
			currentPlayer += 1
		if currChar == "ENTER":
			break
		elif currChar == "TAB":
			return 0
	if currentPlayer == 1: # Retourne le joueur sélectionner
		return 1
	else:
		return 2


def start(player1 : str, player2: str):
	"""
	Démarre le jeu

	Entrée : player1 : str
	player1 symbolise le joueur 1

	Entrée : player2 : str
	player2 symbolise le joueur 2
	"""
	grid : List[List[str]]
	currentCase : int
	currChar : str
	currentPlayer : int

	grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] # Initialise la grille
	currentCase = 1
	currChar = ''
	currentPlayer = selectPlayer(player1, player2)

	if currentPlayer == 0:
		return
	while True:
		while True:
			displayGrid(grid, currentCase, currentPlayer, player1, player2)
			currChar = getKey()
			if currChar == "UP": # Change la case sélectionner
				if currentCase > 3:
					currentCase -= 3
			elif currChar == "DOWN":
				if currentCase < 7:
					currentCase += 3
			elif currChar == "RIGHT":
				if currentCase != 9:
					currentCase += 1
			elif currChar == "LEFT":
				if currentCase != 1:
					currentCase -= 1
			elif currChar == "ENTER" and grid[(currentCase - 1) // 3][(currentCase - 1) % 3] == ' ': # Change le joueur actuel
				if currentPlayer == 1:
					grid[(currentCase - 1) // 3][(currentCase - 1) % 3] = '×' # Ajoute le symbole du joueur actuel
					currentPlayer = 2
				elif currentPlayer == 2:
					grid[(currentCase - 1) // 3][(currentCase - 1) % 3] = '○' # Ajoute le symbole du joueur actuel
					currentPlayer = 1
				if checkWin(grid) == True: # Vérifie si un joueur a gagné
					if currentPlayer == 1:
						displayEmptySquare() # Affiche le gagnant
						centerText(f"{player2} a gagné")
						addPoint(player2, 3)
						sleep(1)
						return
					elif currentPlayer == 2:
						displayEmptySquare() # Affiche le gagnant
						centerText(f"{player1} a gagné")
						addPoint(player1, 3)
						sleep(1)
						return
				elif grid[0][0] != ' ' and grid[0][1] != ' ' and grid[0][2] != ' ' and grid[1][0] != ' ' and grid[1][1] != ' ' and grid[1][2] != ' ' and grid[2][0] != ' ' and grid[2][1] != ' ' and grid[2][2] != ' ': # Vérifie si il y a égalité
					displayEmptySquare() # Affiche l'égalité
					centerText("Égalité")
					sleep(1)
					return
			elif currChar == "TAB":
				return