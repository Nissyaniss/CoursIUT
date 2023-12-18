from os import get_terminal_size
from time import sleep
from typing import List

from ANSIcolors import inverseColor, stringRed, stringYellow, backStringRed, backStringYellow
from termUtils import displayEmptySquare, centerTextAtLine, printAt, centerText, getKey
from players import addPoint

def checker(grid : List[List[str]], posY : int, posX : int) -> bool:
	"""
	Vérifie si un joueur a gagné

	Entrée : grid : list[list[str]]
	grid symbolise la grille du morpion

	Entrée : posY : int
	posY symbolise la position Y de la case

	Entrée : posX : int
	posX symbolise la position X de la case

	Sortie : bool
	True si un joueur a gagné, False sinon
	"""
	count : int
	
	count = 0
	i = 1

	while ((posX - i) >= 0): # Vérifie si un joueur a gagné en horizontal
		if grid[posY][posX - i] != grid[posY][posX]:
			break
		else:
			i += 1
			count += 1
	i = 1
	while ((posX + i) <= 6):
		if grid[posY][posX + i] != grid[posY][posX]:
			break
		else:
			i += 1
			count += 1

	if count < 3:
		count = 0
	i = 1
	while ((posY - i) >= 0) and count < 3: # Vérifie si un joueur a gagné en vertical
		if grid[posY - i][posX] != grid[posY][posX]:
			break
		else:
			i += 1
			count += 1
	i = 1
	while ((posY + i) <= 5) and count < 3:
		if grid[posY + i][posX] != grid[posY][posX]:
			break
		else:
			i += 1
			count += 1
	
	if count < 3:
		count = 0
	i = 1
	while ((posY + i) <= 5 and (posX - i) >= 0) and count < 3: # Vérifie si un joueur a gagné en diagonal
		if grid[posY + i][posX - i] != grid[posY][posX]:
			break
		else:
			i += 1
			count += 1
	i = 1
	while ((posY - i) >= 0 and (posX + i) <= 6) and count < 3:
		if grid[posY - i][posX + i] != grid[posY][posX]:
			break
		else:
			i += 1
			count += 1

	if count >= 3: # Vérifie si un joueur a gagné
		return True
	else:
		return False

def displaySelectedPlayer(currentPlayer : int, player1 : str, player2: str) -> str:
	"""
	Affiche le joueur sélectionner

	Entrée : currentPlayer : int
	currentPlayer symbolise le joueur actuel

	Entrée : player1 : str
	player1 symbolise le joueur 1

	Entrée : player2 : str
	player2 symbolise le joueur 2

	Sortie : str
	Le joueur sélectionner formaté
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
	Sélectionne le joueur qui commence

	Entrée : player1 : str
	player1 symbolise le joueur 1

	Entrée : player2 : str
	player2 symbolise le joueur 2

	Sortie : int
	Le joueur qui commence
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
		if currChar == "DOWN" and currentPlayer != 2:
			currentPlayer += 1
		if currChar == "ENTER": # Valide le joueur sélectionner
			break
		elif currChar == "TAB": # Retourne au menu
			return 0
	if currentPlayer == 1: # Retourne le joueur sélectionner
		return 1
	else:
		return 2

def displayGrid(grid : List[List[str]], currentCase : int, currentPlayer : int):
	"""
	Affiche la grille du puissance4

	Entrée : grid : list[list[str]]
	grid symbolise la grille du puissance4

	Entrée : currentCase : int
	currentCase symbolise la case sélectionner

	Entrée : currentPlayer : int
	currentPlayer symbolise le joueur actuel
	"""
	maxWidth : int
	maxHeight : int
	i : int
	j : int

	maxWidth = get_terminal_size().columns - 3 # Récupère la taille du terminal
	maxHeight = get_terminal_size().lines - 3
	i = 0
	j = 0

	while i < 6: # Affiche la grille 
		while j < 7:
			if currentCase == j and i <= 0 and currentPlayer == 2: # Affiche la case sélectionner
				printAt(maxHeight // 2 - 3 + i, maxWidth // 2 + j * 2 - 8,"│" + backStringRed(grid[i][currentCase]) + "│")
			elif currentCase == j and i <= 0 and currentPlayer == 1: # Affiche la case sélectionner
				printAt(maxHeight // 2 - 3 + i, maxWidth // 2 + j * 2 - 8,"│" + backStringYellow(grid[i][currentCase]) + "│")
			else:
				printAt(maxHeight // 2 - 3 + i, maxWidth // 2 + j * 2 - 8,"│" + grid[i][j] + "│")
			j += 1
		j = 0
		i += 1

def start(player1 : str, player2 : str):
	grid : List[List[str]]
	currentPlayer : int
	currChar : str
	currentCase : int

	grid = [[" " for i in range(7)] for j in range(6)] # Initialise la grille
	currentPlayer = selectPlayer(player1, player2)
	currChar = ""
	currentCase = 0

	if currentPlayer == 0:
		return
	displayEmptySquare()
	while True:
		while True:
			if currentPlayer == 1: # Affiche le joueur actuel
				centerTextAtLine(10, f"C'est le tour de : {player1}")
			elif currentPlayer == 2:
				centerTextAtLine(10, f"C'est le tour de : {player2}")
			displayGrid(grid, currentCase, currentPlayer)
			currChar = getKey()
			if currChar == "RIGHT" and currentCase < 6: # Change la case sélectionner
				currentCase += 1
			if currChar == "LEFT" and currentCase > 0:
				currentCase -= 1
			if currChar == "ENTER":
				break
			elif currChar == "TAB": # Retourne au menu
				return
		if currentPlayer == 1 and grid[0][currentCase] == ' ':
			i = 5
			while i >= 0:
				if grid[i][currentCase] == ' ': # Ajoute un pion
					grid[i][currentCase] = stringYellow("●")
					break
				i -= 1
			if checker(grid, i, currentCase): # Vérifie si un joueur a gagné
				displayEmptySquare()
				centerText(f"{player1} a gagné !")
				addPoint(player1, 4)
				sleep(1)
				return
			currentPlayer = 2
		elif currentPlayer == 2 and grid[0][currentCase] == ' ':
			i = 5
			while i >= 0:
				if grid[i][currentCase] == ' ': # Ajoute un pion
					grid[i][currentCase] =  stringRed("●")
					break
				i -= 1
			if checker(grid, i, currentCase): # Vérifie si un joueur a gagné
				displayEmptySquare()
				centerText(f"{player2} a gagné !")
				addPoint(player2, 4)
				sleep(1)
				return
			currentPlayer = 1
		i = 0
		for e in grid: # Vérifie si il y a égalité
			for e2 in e:
				if e2 != " ":
					i = i + 1
		if i == 42:
			displayEmptySquare()
			centerText("Égalité")
			sleep(1)
			return
