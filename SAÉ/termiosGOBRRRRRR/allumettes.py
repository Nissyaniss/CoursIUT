from calendar import c
import random
from time import sleep
from os import get_terminal_size
from random import randint

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
	
	centerTextAtLine(maxHeight // 2 - 1, f" Nombre d'allumettes restantes : {matchs}  ") # Affiche le nombre d'allumettes restantes
	centerText(f"  {player} choisissez combien d'allumette vous allez supprimer :") # Affiche le texte pour choisir le nombre d'allumettes
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
			return "0"
	if currentPlayer == 1:
		return player2
	else:
		return player1

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
	currentPlayer : str
	maxHeight : int
	hasBotPlayed : bool

	maxHeight = get_terminal_size().lines - 3 # Récupère la hauteur du terminal
	if player1[0] == '\t' and player2[0] == '\t':
		currentPlayer = selectPlayer(player1, player2)
	elif player1[0] == '\t':
		currentPlayer = selectPlayer(player1, player2)
	elif player2[0] == '\t':
		currentPlayer = selectPlayer(player1, player2)
	else:
		currentPlayer = selectPlayer(player1, player2)
	matchs = 20
	currChar = ""
	currentSelectedNb = 1
	hasBotPlayed = False

	if currentPlayer == "0":
		return
	displayEmptySquare()
	while True:
		if matchs < 0: # Si il y a moins d'allumettes que le nombre sélectionner
			matchs = matchs + currentSelectedNb
		else: # Change de joueur
			if currentPlayer == player1:
				currentPlayer = player2
			else:
				currentPlayer = player1
			
			if currentPlayer == player1: # Affiche le menu
				if player1[0] == '\t':
					centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, displayMenu(currentSelectedNb, "Bot 1", matchs))
					sleep(1)
				else:
					centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, displayMenu(currentSelectedNb, player1, matchs))
			else:
				if player2[0] == '\t':
					centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, displayMenu(currentSelectedNb, "Bot 2", matchs))
					sleep(1)
				else:
					centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, displayMenu(currentSelectedNb, player2, matchs))
		if (player1[0] == '\t' and player1[1] == '1' and currentPlayer == player1) or (player2[0] == '\t' and player2[1] == '1' and currentPlayer == player2):
			currentSelectedNb = randint(1, 3)
			while matchs - currentSelectedNb < 0:
				currentSelectedNb = randint(1, 3)
			matchs = matchs - currentSelectedNb # Retire le nombre d'allumettes sélectionner
		elif (player1[0] == '\t' and player1[1] == '2' and currentPlayer == player1) or (player2[0] == '\t' and player2[1] == '2' and currentPlayer == player2):
			if random.randint(0, 1) == 1:
				currentSelectedNb = randint(1, 3)
				while matchs - currentSelectedNb < 0:
					currentSelectedNb = randint(1, 3)
			else:
				if matchs <= 4:
					if matchs == 4:
						currentSelectedNb = 3
					elif matchs == 3:
						currentSelectedNb = 2
					elif matchs == 2:
						currentSelectedNb = 1
					elif matchs == 1:
						currentSelectedNb = 1
					hasBotPlayed = True
				if hasBotPlayed == False:
					for i in range(4, 0, -1):
						if matchs > 4 * i + 1 and hasBotPlayed == False:
							currentSelectedNb = matchs - (4 * i + 1)
							if currentSelectedNb == 4:
								currentSelectedNb = 1
							hasBotPlayed = True
			matchs = matchs - currentSelectedNb
			hasBotPlayed = False
		elif (player1[0] == '\t' and player1[1] == '3' and currentPlayer == player1) or (player2[0] == '\t' and player2[1] == '3' and currentPlayer == player2):
			if matchs <= 4:
				if matchs == 4:
					currentSelectedNb = 3
				elif matchs == 3:
					currentSelectedNb = 2
				elif matchs == 2:
					currentSelectedNb = 1
				elif matchs == 1:
					currentSelectedNb = 1
				hasBotPlayed = True
			if hasBotPlayed == False:
				for i in range(4, 0, -1):
					if matchs > 4 * i + 1 and hasBotPlayed == False:
						currentSelectedNb = matchs - (4 * i + 1)
						if currentSelectedNb == 4:
							currentSelectedNb = 1
						hasBotPlayed = True
			matchs = matchs - currentSelectedNb
			hasBotPlayed = False
		else:
			while True:
				if currentPlayer == player1: # Affiche le menu
					if player1[0] == '\t':
						centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, displayMenu(currentSelectedNb, "Bot 1", matchs))
						sleep(1)
					else:
						centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, displayMenu(currentSelectedNb, player1, matchs))
				else:
					if player2[0] == '\t':
						centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, displayMenu(currentSelectedNb, "Bot 2", matchs))
						sleep(1)
					else:
						centerTextAtLine(maxHeight // 2 + 2 + currentSelectedNb, displayMenu(currentSelectedNb, player2, matchs))
				currChar = getKey()
				if currChar == "UP" and currentSelectedNb != 1: # Change le nombre d'allumettes sélectionner
					currentSelectedNb -= 1
				if currChar == "DOWN" and currentSelectedNb != 3: # Change le nombre d'allumettes sélectionner
					currentSelectedNb += 1
				elif currChar == "TAB": # Retourne 0 si le joueur quitte
					return
				elif currChar == "ENTER": # Retourne le nombre d'allumettes sélectionner
					matchs = matchs - currentSelectedNb # Retire le nombre d'allumettes sélectionner
					break

		if matchs == 0: # Vérifie si le joueur a gagné
			displayEmptySquare()
			if currentPlayer == player1 and player2[0] != '\t': # Affiche le gagnant
				centerText(f"{player2} a gagné")
				addPoint(player2, 2)
			elif currentPlayer == player2 and player1[0] != '\t':
				centerText(f"{player1} a gagné")
				addPoint(player1, 2)
			elif currentPlayer == player1 and player2[0] == '\t': # Affiche le gagnant
				centerText(f"Le bot 2 a gagné")
			elif currentPlayer == player2 and player1[0] == '\t':
				centerText(f"Le bot 1 a gagné")
			sleep(1)
			return