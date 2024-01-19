from time import sleep
from os import get_terminal_size
from typing import List
from random import randint

from ANSIcolors import inverseColor
from termUtils import displayEmptySquare, centerTextAtLine, centerText, printAt, getKey
from players import addPoint

def displayGrid(grid : List[List[str]], currentSelectedCase : int, currentPlayer : str, player1 : str, player2: str) -> None:
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
	if currentPlayer[0] == "\t" and player1 == currentPlayer: # Affiche le joueur actuel
		centerTextAtLine(13, f"C'est actuellement au tour de : Bot 1" + len(player2 if player2[0] != '\t' else "     ") * " ")
	elif currentPlayer[0] == "\t" and player2 == currentPlayer:
		centerTextAtLine(13, f"C'est actuellement au tour de : Bot 2" + len(player1 if player1[0] != '\t' else "     ") * " ")
	elif currentPlayer[0] != "\t" and player1 == currentPlayer:
		centerTextAtLine(13, f"C'est actuellement au tour de : {player1}" + len(player2 if player2[0] != '\t' else "     ") * " ")
	elif currentPlayer[0] != "\t" and player2 == currentPlayer:
		centerTextAtLine(13, f"C'est actuellement au tour de : {player2}" + len(player1 if player1[0] != '\t' else "     ") * " ")
	centerTextAtLine(15, f" {grid[0][0]} │ {grid[0][1]} │ {grid[0][2]} ") # Affiche la grille
	centerTextAtLine(16, "───┼───┼───")
	centerTextAtLine(17, f" {grid[1][0]} │ {grid[1][1]} │ {grid[1][2]} ")
	centerTextAtLine(18, "───┼───┼───")
	centerTextAtLine(19, f" {grid[2][0]} │ {grid[2][1]} │ {grid[2][2]} ")

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
		
def checkPreWin(grid : List[List[str]], symbol : str) -> tuple[int, int]:
		if grid[0][0] == symbol and grid[0][2] == symbol and grid[0][1] == ' ': # Horizontal 1
			return (0, 1)
		elif grid[0][1] == symbol and grid[0][2] == symbol and grid[0][0] == ' ': # Horizontal 1
			return (0, 0)
		elif grid[0][0] == symbol and grid[0][1] == symbol and grid[0][2] == ' ': # Horizontal 1
			return (0, 2)

		elif grid[1][0] == symbol and grid[1][2] == symbol and grid[1][1] == ' ': # Horizontal 2
			return (1, 1)
		elif grid[1][1] == symbol and grid[1][2] == symbol and grid[1][0] == ' ': # Horizontal 2
			return (1, 0)
		elif grid[1][0] == symbol and grid[1][1] == symbol and grid[1][2] == ' ': # Horizontal 2
			return (1, 2)

		elif grid[2][0] == symbol and grid[2][2] == symbol and grid[2][1] == ' ': # Horizontal 3
			return (2, 1)
		elif grid[2][1] == symbol and grid[2][2] == symbol and grid[2][0] == ' ': # Horizontal 3
			return (2, 0)
		elif grid[2][0] == symbol and grid[2][1] == symbol and grid[2][2] == ' ': # Horizontal 3
			return (2, 2)

		elif grid[0][0] == symbol and grid[2][0] == symbol and grid[1][0] == ' ': # Vertical 1
			return (1, 0)
		elif grid[1][0] == symbol and grid[2][0] == symbol and grid[0][0] == ' ': # Vertical 1
			return (0, 0)
		elif grid[0][0] == symbol and grid[1][0] == symbol and grid[2][0] == ' ': # Vertical 1
			return (2, 0)

		elif grid[0][1] == symbol and grid[2][1] == symbol and grid[1][1] == ' ': # Vertical 2
			return (1, 1)
		elif grid[1][1] == symbol and grid[2][1] == symbol and grid[0][1] == ' ': # Vertical 2
			return (0, 1)
		elif grid[0][1] == symbol and grid[1][1] == symbol and grid[2][1] == ' ': # Vertical 2
			return (2, 1)

		elif grid[0][2] == symbol and grid[2][2] == symbol and grid[1][2] == ' ': # Vertical 3
			return (1, 2)
		elif grid[1][2] == symbol and grid[2][2] == symbol and grid[0][2] == ' ': # Vertical 3
			return (0, 2)
		elif grid[0][2] == symbol and grid[1][2] == symbol and grid[2][2] == ' ': # Vertical 3
			return (2, 2)

		elif grid[0][0] == symbol and grid[2][2] == symbol and grid[1][1] == ' ': # Diagonal 1
			return (1, 1)
		elif grid[1][1] == symbol and grid[2][2] == symbol and grid[0][0] == ' ': # Diagonal 1
			return (0, 0)
		elif grid[0][0] == symbol and grid[1][1] == symbol and grid[2][2] == ' ': # Diagonal 1
			return (2, 2)

		elif grid[0][2] == symbol and grid[2][0] == symbol and grid[1][1] == ' ': # Diagonal 2
			return (1, 1)
		elif grid[1][1] == symbol and grid[2][0] == symbol and grid[0][2] == ' ': # Diagonal 2
			return (0, 2)
		elif grid[0][2] == symbol and grid[1][1] == symbol and grid[2][0] == ' ': # Diagonal 2
			return (2, 0)

		else:
			return (4, 4)

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
	
	
	if currentPlayer == 1:
		if player2[0] == '\t':
			printAt(maxHeight // 2 - 1, maxWidth // 2 - len(player1) * 2 + 1, " " * len(player2) + "Bot 2")
		else:
			printAt(maxHeight // 2 - 1, maxWidth // 2 - len(player1) * 2 + 1, " " * len(player2) + player2) # Affiche les autres joueurs
		if player1[0] == '\t':
			return str(">" + inverseColor("Bot 1") + len("Bot 1") * " ")
		return str(">" + inverseColor(player1) + len(player1) * " ")
	elif currentPlayer == 2:
		if player1[0] == '\t':
			printAt(maxHeight // 2 - 2, maxWidth // 2 - len(player1) * 2 + 1, " " * len(player1) + "Bot 1")
		else:
			printAt(maxHeight // 2 - 2, maxWidth // 2 - len(player1) * 2 + 1, " " * len(player1) + player1)
		if player2[0] == '\t':
			return str(">" + inverseColor("Bot 2") + len("Bot 2") * " ")
		return str(">" + inverseColor(player2) + len(player2) * " ")
	else :
		return "ERROR"

def selectPlayer(player1 : str, player2 : str) -> str:
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
			return "0"
	if currentPlayer == 1: # Retourne le joueur sélectionner
		return player1
	else:
		return player2



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
	currentPlayer : str
	posBlock : tuple[int, int]
	posWin : tuple[int, int]

	grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] # Initialise la grille
	currentCase = 1
	currChar = ''
	if player1[0] == '\t' and player2[0] == '\t':
		currentPlayer = selectPlayer(player1, player2)
	elif player1[0] == '\t':
		currentPlayer = selectPlayer(player1, player2)
	elif player2[0] == '\t':
		currentPlayer = selectPlayer(player1, player2)
	else:
		currentPlayer = selectPlayer(player1, player2)
	posBlock = (0, 0)
	posWin = (0, 0)

	#
	bot1 : int = 0
	bot2 : int = 0
	partie : int = 0
	ega : int = 0
	ehh : str = currentPlayer
	#

	if currentPlayer == "0":
		return
	while partie != 10000:
		displayGrid(grid, currentCase, currentPlayer, player1, player2)
		if currentPlayer == player1 and player1[0] == '\t' and player1[1] == '1':
			currentCase = randint(1, 9)
			while grid[(currentCase - 1) // 3][(currentCase - 1) % 3] != ' ':
				currentCase = randint(1, 9)
			grid[(currentCase - 1) // 3][(currentCase - 1) % 3] = '×' # Ajoute le symbole du joueur actuel
			displayGrid(grid, currentCase, currentPlayer, player1, player2)
			# sleep(1)
			currentPlayer = player2

		elif currentPlayer == player2 and player2[0] == '\t' and player2[1] == '1':
			currentCase = randint(1, 9)
			while grid[(currentCase - 1) // 3][(currentCase - 1) % 3] != ' ':
				currentCase = randint(1, 9)
			grid[(currentCase - 1) // 3][(currentCase - 1) % 3] = '○' # Ajoute le symbole du joueur actuel
			displayGrid(grid, currentCase, currentPlayer, player1, player2)
			# sleep(1)
			currentPlayer = player1

		elif currentPlayer == player1 and player1[0] == '\t' and player1[1] == '2':
			if randint(0, 1):
				currentCase = randint(1, 9)
				while grid[(currentCase - 1) // 3][(currentCase - 1) % 3] != ' ':
					currentCase = randint(1, 9)
				grid[(currentCase - 1) // 3][(currentCase - 1) % 3] = '×' # Ajoute le symbole du joueur actuel
				displayGrid(grid, currentCase, currentPlayer, player1, player2)
				# sleep(1)
			else:
				posWin = checkPreWin(grid, '×')
				if posWin[0] != 4 and grid[posWin[0]][posWin[1]] == ' ':
					currentCase = posWin[0] * 3 + posWin[1] + 1
					grid[posWin[0]][posWin[1]] = '×'
					displayGrid(grid, currentCase, currentPlayer, player1, player2)
					# sleep(1)
				else:
					posBlock = checkPreWin(grid, '○')
					if posBlock[0] != 4 and grid[posBlock[0]][posBlock[1]] == ' ':
						currentCase = posBlock[0] * 3 + posBlock[1] + 1
						grid[posBlock[0]][posBlock[1]] = '×'
						displayGrid(grid, currentCase, currentPlayer, player1, player2)
						# sleep(1)
					else:
						currentCase = randint(1, 9)
						while grid[(currentCase - 1) // 3][(currentCase - 1) % 3] != ' ':
							currentCase = randint(1, 9)
						grid[(currentCase - 1) // 3][(currentCase - 1) % 3] = '×' # Ajoute le symbole du joueur actuel
						displayGrid(grid, currentCase, currentPlayer, player1, player2)
						# sleep(1)
			currentPlayer = player2
		elif currentPlayer == player2 and player2[0] == '\t' and player2[1] == '2':
			if randint(0, 1):
				currentCase = randint(1, 9)
				while grid[(currentCase - 1) // 3][(currentCase - 1) % 3] != ' ':
					currentCase = randint(1, 9)
				grid[(currentCase - 1) // 3][(currentCase - 1) % 3] = '○' # Ajoute le symbole du joueur actuel
				displayGrid(grid, currentCase, currentPlayer, player1, player2)
				# sleep(1)
			else:
				posWin = checkPreWin(grid, '○')
				if posWin[0] != 4 and grid[posWin[0]][posWin[1]] == ' ':
					currentCase = posWin[0] * 3 + posWin[1] + 1
					grid[posWin[0]][posWin[1]] = '○'
					displayGrid(grid, currentCase, currentPlayer, player1, player2)
					# sleep(1)
				else:
					posBlock = checkPreWin(grid, '×')
					if posBlock[0] != 4 and grid[posBlock[0]][posBlock[1]] == ' ':
						currentCase = posBlock[0] * 3 + posBlock[1] + 1
						grid[posBlock[0]][posBlock[1]] = '○'
						displayGrid(grid, currentCase, currentPlayer, player1, player2)
						# sleep(1)
					else:
						currentCase = randint(1, 9)
						while grid[(currentCase - 1) // 3][(currentCase - 1) % 3] != ' ':
							currentCase = randint(1, 9)
						grid[(currentCase - 1) // 3][(currentCase - 1) % 3] = '○' # Ajoute le symbole du joueur actuel
						displayGrid(grid, currentCase, currentPlayer, player1, player2)
						# sleep(1)
			currentPlayer = player1

		elif currentPlayer == player1 and player1[0] == '\t' and player1[1] == '3':
			posWin = checkPreWin(grid, '×')
			if posWin[0] != 4 and grid[posWin[0]][posWin[1]] == ' ':
				currentCase = posWin[0] * 3 + posWin[1] + 1
				grid[posWin[0]][posWin[1]] = '×'
				displayGrid(grid, currentCase, currentPlayer, player1, player2)
				# sleep(1)
			else:
				posBlock = checkPreWin(grid, '○')
				if posBlock[0] != 4 and grid[posBlock[0]][posBlock[1]] == ' ':
					currentCase = posBlock[0] * 3 + posBlock[1] + 1
					grid[posBlock[0]][posBlock[1]] = '×'
					displayGrid(grid, currentCase, currentPlayer, player1, player2)
					# sleep(1)
				else:
					currentCase = randint(1, 9)
					while grid[(currentCase - 1) // 3][(currentCase - 1) % 3] != ' ':
						currentCase = randint(1, 9)
					grid[(currentCase - 1) // 3][(currentCase - 1) % 3] = '×' # Ajoute le symbole du joueur actuel
					displayGrid(grid, currentCase, currentPlayer, player1, player2)
					# sleep(1)
			currentPlayer = player2
		elif currentPlayer == player2 and player2[0] == '\t' and player2[1] == '3':
			posWin = checkPreWin(grid, '○')
			if posWin[0] != 4 and grid[posWin[0]][posWin[1]] == ' ':
				currentCase = posWin[0] * 3 + posWin[1] + 1
				grid[posWin[0]][posWin[1]] = '○'
				displayGrid(grid, currentCase, currentPlayer, player1, player2)
				# sleep(1)
			else:
				posBlock = checkPreWin(grid, '×')
				if posBlock[0] != 4 and grid[posBlock[0]][posBlock[1]] == ' ':
					currentCase = posBlock[0] * 3 + posBlock[1] + 1
					grid[posBlock[0]][posBlock[1]] = '○'
					displayGrid(grid, currentCase, currentPlayer, player1, player2)
					# sleep(1)
				else:
					currentCase = randint(1, 9)
					while grid[(currentCase - 1) // 3][(currentCase - 1) % 3] != ' ':
						currentCase = randint(1, 9)
					grid[(currentCase - 1) // 3][(currentCase - 1) % 3] = '○' # Ajoute le symbole du joueur actuel
					displayGrid(grid, currentCase, currentPlayer, player1, player2)
					# sleep(1)
			currentPlayer = player1

		else:
			while True:
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
					if currentPlayer == player1:
						grid[(currentCase - 1) // 3][(currentCase - 1) % 3] = '×' # Ajoute le symbole du joueur actuel
						currentPlayer = player2
						break
					elif currentPlayer == player2:
						grid[(currentCase - 1) // 3][(currentCase - 1) % 3] = '○' # Ajoute le symbole du joueur actuel
						currentPlayer = player1
						break
				elif currChar == "TAB":
					return
				displayGrid(grid, currentCase, currentPlayer, player1, player2)
		if checkWin(grid) is True: # Vérifie si un joueur a gagné
			displayEmptySquare() # Affiche le gagnant
			if currentPlayer == player2 and player1[0] != '\t':
				centerText(f"{player1} a gagné")
				addPoint(player1, 3)
				sleep(1)
			elif currentPlayer == player1 and player2[0] != '\t':
				centerText(f"{player2} a gagné")
				addPoint(player2, 3)
				sleep(1)
			else:
				if player1[0] == '\t' and currentPlayer == player2:
					centerText(f"Le bot 1 a gagné")
					# 
					bot1 += 1
					partie += 1
					grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] # Initialise la grille
					currentPlayer = ehh
					with open("output.txt", "w") as file:
						file.write(f"Bot 1 : {bot1} Bot 2 : {bot2} Egalité : {ega}")
					#
				elif player2[0] == '\t' and currentPlayer == player1:
					centerText(f"Le bot 2 a gagné")
					#
					bot2 += 1
					partie += 1
					grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] # Initialise la grille
					currentPlayer = ehh
					with open("output.txt", "w") as file:
						file.write(f"Bot 1 : {bot1} Bot 2 : {bot2} Egalité : {ega}")
					#
			# sleep(1)
			# return
		elif grid[0][0] != ' ' and grid[0][1] != ' ' and grid[0][2] != ' ' and grid[1][0] != ' ' and grid[1][1] != ' ' and grid[1][2] != ' ' and grid[2][0] != ' ' and grid[2][1] != ' ' and grid[2][2] != ' ': # Vérifie si il y a égalité
			displayEmptySquare() # Affiche l'égalité
			centerText("Égalité")
			# 
			ega += 1
			partie += 1
			grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] # Initialise la grille
			currentPlayer = ehh
			with open("output.txt", "w") as file:
				file.write(f"Bot 1 : {bot1} Bot 2 : {bot2} Egalité : {ega}")
			# 
			# sleep(1)
			# return
		