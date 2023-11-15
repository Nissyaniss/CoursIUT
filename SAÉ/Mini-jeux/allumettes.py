from time import sleep
from os import get_terminal_size

from players import addPoint
from termUtils import displayEmptySquare, centerTextAtLine, centerText, printAt, getKey
from ANSIcolors import inverseColor

def displayMenu(currentSelectedNb : int, player : str, matchs : int) -> str:
	"""
	Affiche le menu avec le nombre d'allumettes sélectionner

	Entrée : currentSelectedNb : int
	currentSelectedNb symbolise le nombre d'allumettes sélectionner

	Sortie : gameStr : str
	gameStr symbolise le string formaté du nombre d'allumettes sélectionner
	"""
	maxHeight : int

	maxHeight = get_terminal_size().lines - 3 # Récupère la hauteur du terminal
	
	centerTextAtLine(maxHeight // 2 - 1, f"Nombre d'allumettes restantes : {matchs}  ") # Affiche le nombre d'allumettes restantes
	centerText(f"{player} choisissez combien d'allumette vous allez supprimer :") # Affiche le texte pour choisir le nombre d'allumettes
	if currentSelectedNb == 1: # Affiche les autres choix
		centerTextAtLine(maxHeight // 2 + 4, " 2")
		centerTextAtLine(maxHeight // 2 + 5, " 3")
	elif currentSelectedNb == 2:
		centerTextAtLine(maxHeight // 2 + 3, " 1")
		centerTextAtLine(maxHeight // 2 + 5, " 3")
	elif currentSelectedNb == 3:
		centerTextAtLine(maxHeight // 2 + 3, " 1")
		centerTextAtLine(maxHeight // 2 + 4, " 2")

	return str(">" + inverseColor(f'{currentSelectedNb}')) # Retourne le string formaté

def displaySelectedPlayer(currentPlayer : int, player1 : str, player2: str) -> str:
	"""
	Affiche le menu avec le joueur sélectionner

	Entrée : currentPlayer : int
	currentPlayer symbolise le joueur sélectionner

	Sortie : gameStr : str
	gameStr symbolise le string formaté du joueur sélectionner
	"""
	maxWidth : int
	maxHeight : int

	maxWidth = get_terminal_size().columns - 3 # Récupère la largeur du terminal
	maxHeight = get_terminal_size().lines - 3 # Récupère la hauteur du terminal
	
	if currentPlayer == 1:
		printAt(maxHeight // 2 - 1, maxWidth // 2 - len(player1) * 2 + 1, " " * len(player2) + player2) # Affiche les autres joueurs
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

	maxWidth = get_terminal_size().columns - 3 # Récupère la largeur du terminal
	maxHeight = get_terminal_size().lines - 3 # Récupère la hauteur du terminal
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
		if currChar == "ENTER": # Retourne le joueur sélectionner
			break
		elif currChar == "TAB": # Retourne 0 si le joueur quitte
			return 0
	if currentPlayer == 1:
		return 1
	else:
		return 2

def start(player1 : str, player2 : str) -> None:
	"""
	Démarre le jeu

	Entrée : player1 : str
	player1 symbolise le joueur 1

	Entrée : player2 : str
	player2 symbolise le joueur 2
	"""
	matchs : int
	currChar : str
	currentSelectedNb : int
	currentPlayer : int
	maxHeight : int

	maxHeight = get_terminal_size().lines - 3 # Récupère la hauteur du terminal
	currentPlayer = selectPlayer(player1, player2)
	matchs = 20
	currChar = ""
	currentSelectedNb = 1

	if currentPlayer == 0:
		return
	displayEmptySquare()
	while True:
		while True:
			if currentPlayer == 1: # Affiche le menu
				centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, displayMenu(currentSelectedNb, player1, matchs))
			else:
				centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, displayMenu(currentSelectedNb, player2, matchs))
			currChar = getKey()
			if currChar == "UP" and currentSelectedNb != 1: # Change le nombre d'allumettes sélectionner
				currentSelectedNb -= 1
			if currChar == "UP" and currentSelectedNb != 3: # Change le nombre d'allumettes sélectionner
				currentSelectedNb += 1
			elif currChar == "TAB": # Retourne 0 si le joueur quitte
				return
			elif currChar == "ENTER": # Retourne le nombre d'allumettes sélectionner
				matchs = matchs - currentSelectedNb # Retire le nombre d'allumettes sélectionner
				if matchs == 0: # Vérifie si le joueur a gagné
					displayEmptySquare()
					if currentPlayer == player1: # Affiche le gagnant
						centerText(f"{player2} a gagné")
						addPoint(player2, 2)
					else:
						centerText(f"{player1} a gagné")
						addPoint(player1, 2)
					sleep(1)
					return
				elif matchs < 0: # Si il y a moins d'allumettes que le nombre sélectionner
					matchs = matchs + currentSelectedNb
				else: # Change de joueur
					if currentPlayer == 1:
						currentPlayer = 2
					else:
						currentPlayer = 1