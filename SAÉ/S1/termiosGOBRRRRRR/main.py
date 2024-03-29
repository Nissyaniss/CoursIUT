from os import system, get_terminal_size

from morpion import start as morpion
from allumettes import start as allumettes
from rules import start as rules
from puissance4 import start as puissance4
from devinette import start as devinette
from scoreboard import start as scoreboard
from termUtils import printAt, setup, restoreTerm, displayEmptySquare, centerTextAtLine, setCursorPosition, getKey
from players import addPlayer, isPlayerExisting, printScoreboard
from ANSIcolors import inverseColor

def displayMenu(currentSelectedGame : int, player1 : str, player2 : str) -> None:
	"""
	Affiche le menu avec le jeu sélectionner

	Entrée : currentSelectedGame : int
	currentSelectedGame symbolise le jeu sélectionner
	"""
	maxWidth : int
	
	maxWidth = get_terminal_size().columns - 3 # Défini la taille maximal du terminal
	
	displayEmptySquare() # Affiche un carré vide
	printAt(2, 5, "┌────────────────┐") # Affiche un carré avec Scoreboard écrit dedans au coordonnées 2 et 5
	printAt(3, 5, "│   SCOREBOARD   │")
	printAt(4, 5, "└────────────────┘")
	printScoreboard(player1, player2) # Affiche le scoreboard des deux joueur courant
	printAt(2, maxWidth - 11, "┌──────────┐") # Affiche un carré avec Règles écrit dedans au coordonnées 2 et max - 11
	printAt(3, maxWidth - 11, "│  RÈGLES  │")
	printAt(4, maxWidth - 11, "└──────────┘")
	centerTextAtLine(6, "┌─────────────────────────┐")
	centerTextAtLine(7, "│         BONJOUR         │") # Affiche un carré avec le titre écrit dedans centré
	centerTextAtLine(8, "│   Liste des mini-jeux   │")
	centerTextAtLine(9, "└─────────────────────────┘")
	printAt(10 + currentSelectedGame, (maxWidth - 11) // 2, displayGameSelected(currentSelectedGame)) # Affiche le jeux sélectionner

def displayGameSelected(currentSelectedGame : int) -> str:
	"""
	Affiche le jeu sélectionner

	Entrée : currentSelectedGame : int
	currentSelectedGame symbolise le jeu sélectionner

	Sortie : gameStr : str
	gameStr symbolise le string formaté du jeu sélectionner
	"""
	gameStr: str
	maxWidth = get_terminal_size().columns - 3

	if currentSelectedGame == 1:
		gameStr = "Devinette" # Défini le string du jeu sélectionner
		printAt(12, (maxWidth - 11) // 2, "  Allumette") # Affiche les autres jeux
		printAt(13, (maxWidth - 11) // 2, "  Morpion")
		printAt(14, (maxWidth - 11) // 2, "  Puissance 4")
		printAt(3, 8, " SCOREBOARD")
		printAt(3, maxWidth - 9, " RÈGLES")
	elif currentSelectedGame == 2:
		printAt(11, (maxWidth - 11) // 2, "  Devinette")
		gameStr = "Allumette"
		printAt(13, (maxWidth - 11) // 2, "  Morpion")
		printAt(14, (maxWidth - 11) // 2, "  Puissance 4")
		printAt(3, 8, " SCOREBOARD")
		printAt(3, maxWidth - 9, " RÈGLES" )
	elif currentSelectedGame == 3:
		printAt(11, (maxWidth - 11) // 2, "  Devinette")
		printAt(12, (maxWidth - 11) // 2, "  Allumette")
		gameStr = "Morpion"
		printAt(14, (maxWidth - 11) // 2, "  Puissance 4")
		printAt(3, 8, " SCOREBOARD")
		printAt(3, maxWidth - 9, " RÈGLES")
	elif currentSelectedGame == 4:
		printAt(11, (maxWidth - 11) // 2, "  Devinette")
		printAt(12, (maxWidth - 11) // 2, "  Allumette")
		printAt(13, (maxWidth - 11) // 2, "  Morpion")
		gameStr = "Puissance 4" 
		printAt(3, 8, " SCOREBOARD")
		printAt(3, maxWidth - 9, " RÈGLES")
	elif currentSelectedGame == -1:
		printAt(11, (maxWidth - 11) // 2, "  Devinette")
		printAt(12, (maxWidth - 11) // 2, "  Allumette")
		printAt(13, (maxWidth - 11) // 2, "  Morpion")
		printAt(14, (maxWidth - 11) // 2, "  Puissance 4")
		gameStr = "SCOREBOARD"
		printAt(3, maxWidth - 9, " RÈGLES")
	elif currentSelectedGame == -2:
		printAt(11, (maxWidth - 11) // 2, "  Devinette")
		printAt(12, (maxWidth - 11) // 2, "  Allumette")
		printAt(13, (maxWidth - 11) // 2, "  Morpion")
		printAt(14, (maxWidth - 11) // 2, "  Puissance 4")
		gameStr = "RÈGLES"
		printAt(3, 8, " SCOREBOARD")
	else :
		gameStr = "ERROR"

	return str(">" + inverseColor(gameStr) + "  ") # Retourne le string formaté

def selectDifficulty(currentSelectedDifficulty : int) -> None:
	"""
	Affiche le menu des difficulté de bot

	Entrée : currentSelectedDifficulty : int
	currentSelectedDifficulty symbolise la difficulté sélectionnée
	"""
	maxWidth : int
	
	maxWidth = get_terminal_size().columns - 3 # Défini la taille maximal du terminal
	
	displayEmptySquare() # Affiche un carré vide
	centerTextAtLine(6, "┌───────────────────────────────────┐")
	centerTextAtLine(7, "│         Difficulté du bot         │") # Affiche un carré avec le titre écrit dedans centré
	centerTextAtLine(8, "└───────────────────────────────────┘")
	printAt(10 + currentSelectedDifficulty, (maxWidth) // 2, displayDifficultySelected(currentSelectedDifficulty)) # Affiche le jeux sélectionner

def displayDifficultySelected(currentSelectedDifficulty : int) -> str:
	"""
	Affiche le jeu sélectionner

	Entrée : currentSelectedDifficulty : int
	currentSelectedDifficulty symbolise la difficulté sélectionnée

	Sortie : difficultyStr : str
	difficultyStr symbolise le string formaté de la difficulté sélectionner
	"""
	difficultyStr: str
	maxWidth = get_terminal_size().columns - 3

	if currentSelectedDifficulty == 1:
		difficultyStr = "1" # Défini le string de la difficulté sélectionnée
		printAt(12, (maxWidth) // 2, "  2") # Affiche les autres difficultés
		printAt(13, (maxWidth) // 2, "  3")
	elif currentSelectedDifficulty == 2:
		printAt(11, (maxWidth) // 2, "  1")
		difficultyStr = "2"
		printAt(13, (maxWidth) // 2, "  3")
	elif currentSelectedDifficulty == 3:
		printAt(11, (maxWidth) // 2, "  1")
		printAt(12, (maxWidth) // 2, "  2")
		difficultyStr = "3"
	else :
		difficultyStr = "ERROR"

	return str(">" + inverseColor(difficultyStr) + "  ") # Retourne le string formaté

def displayMenuPlayer(player : int) -> None:
	"""
	Affiche le menu pour entrer le pseudo du joueur

	Entrée : player : int
	player symbolise joueur actuel
	"""
	maxHeight : int

	maxHeight = get_terminal_size().lines - 3

	system("clear")
	displayEmptySquare()
	printAt(maxHeight + 1, 3, "Appuyer sur \"TAB\" pour quitter")
	centerTextAtLine(6, "┌──────────────────────────────────┐")
	centerTextAtLine(7, "│              BONJOUR             │")
	centerTextAtLine(8, f"│   Entrez votre pseudo joueur {player}   │")
	centerTextAtLine(9, "│   ou appuyez sur entrée si       │")
	centerTextAtLine(10, f"│   vous voulez que le joueur {player}    │")
	centerTextAtLine(11, "│   soit un bot.                   │")
	centerTextAtLine(12, "└──────────────────────────────────┘")
	centerTextAtLine(14, "Votre pseudo :")

def main() -> None:
	player1 : str
	player2 : str
	currChar : str
	isOnRules : bool
	isOnScoreboard : bool
	maxWidth : int
	original : list[int]
	currentSelectedGame : int
	player1IsBot : bool
	player2IsBot : bool
	currentSelectedDifficulty : int

	player1 = ""
	player2 = ""
	isOnRules  = False
	isOnScoreboard = False
	currChar = ""
	maxWidth = get_terminal_size().columns - 3 # Défini la taille maximal du terminal
	currentSelectedGame = 1
	original = setup() # Défini la configuration du terminal original
	player1IsBot = False
	player2IsBot = False
	currentSelectedDifficulty = 1

	pseudo = "> "

	displayMenuPlayer(1)
	centerTextAtLine(16, pseudo)
	while True:
		setCursorPosition(16, maxWidth // 2 + 4) # Défini la position du curseur
		currChar = getKey() # Récupère la touche pressée
		if len(currChar) == 1 and currChar.isprintable(): # Vérifie si la touche pressée est un caractère imprimable
			pseudo += currChar # Ajoute le caractère au pseudo
			centerTextAtLine(16, pseudo) # Affiche le pseudo
		elif currChar == "ENTER":
			break # Si la touche pressée est Entrée et que le pseudo est plus grand que 2 on sort de la boucle
		elif currChar == "BACKSPACE" and len(pseudo) > 2: # Vérifie si la touche pressée est Backspace
			centerTextAtLine(16, " " * len(pseudo)) # Affiche des espaces pour effacer le pseudo
			pseudo = pseudo[:-1] # Enlève le dernier caractère du pseudo
			centerTextAtLine(16, pseudo)
		elif currChar == "TAB": # Vérifie si la touche pressée est Tab
			restoreTerm(original) # Restore le terminal de base
		else:
			continue
	if len(pseudo) - 2 == 0:
		player1IsBot = True
		while True:
			selectDifficulty(currentSelectedDifficulty)
			currChar = getKey()
			if currChar == "UP" and currentSelectedDifficulty != 1 :
				currentSelectedDifficulty -= 1 # Change la difficulté
				printAt(10 + currentSelectedDifficulty, (maxWidth) // 2, displayDifficultySelected(currentSelectedDifficulty)) # Affiche la difficulté sélectionnée
			if currChar == "DOWN" and currentSelectedDifficulty != 3 : # Vérifie is la touche pressée est la flèche du bas
				currentSelectedDifficulty += 1 # Change la difficulté
				printAt(10 + currentSelectedDifficulty, (maxWidth) // 2, displayDifficultySelected(currentSelectedDifficulty)) # Affiche la difficulté sélectionnée
			elif currChar == "TAB": # Vérifie is la touche pressée est Tab
				restoreTerm(original) # Restore le terminal de base
			elif currChar == "ENTER": # Vérifie is la touche pressée est Entrée
				break
			else:
				continue # Si il y a une autre touche on l'ignore
		player1 = '\t' + str(currentSelectedDifficulty)
	elif player1IsBot is False:
		player1 = pseudo[2:] # Enlève le "> " du pseudo
		if not isPlayerExisting(player1): # Vérifie si le joueur existe
			addPlayer(player1) # Ajoute le joueur
		pseudo = "> " # Réinitialise le pseudo
	player2 = player1 # Défini le joueur 2 comme le joueur 1 pour éviter les mêmes pseudos

	displayMenuPlayer(2)
	centerTextAtLine(16, pseudo)
	while player2 == player1:
		setCursorPosition(16, maxWidth // 2 + 4)
		currChar = getKey()
		if len(currChar) == 1 and currChar.isprintable():
			pseudo += currChar
			centerTextAtLine(16, pseudo)
		elif currChar == "ENTER" and len(pseudo) > 0:
			break
		elif currChar == "BACKSPACE" and len(pseudo) > 2:
			centerTextAtLine(16, " " * len(pseudo))
			pseudo = pseudo[:-1]
			centerTextAtLine(16, pseudo)
		elif currChar == "TAB":
			restoreTerm(original)
		elif len(currChar) > 1:
			continue
		else:
			restoreTerm(original)
	if len(pseudo) - 2 == 0:
		player2IsBot = True
		while True:
			selectDifficulty(currentSelectedDifficulty)
			currChar = getKey()
			if currChar == "UP" and currentSelectedDifficulty != 1 :
				currentSelectedDifficulty -= 1 # Change la difficulté
				printAt(10 + currentSelectedDifficulty, (maxWidth - 11) // 2, displayDifficultySelected(currentSelectedDifficulty)) # Affiche la difficulté sélectionnée
			if currChar == "DOWN" and currentSelectedDifficulty != 3: # Vérifie is la touche pressée est la flèche du bas
				currentSelectedDifficulty += 1 # Change la difficulté
				printAt(10 + currentSelectedDifficulty, (maxWidth - 11) // 2, displayDifficultySelected(currentSelectedDifficulty)) # Affiche la difficulté sélectionnée
			elif currChar == "TAB": # Vérifie is la touche pressée est Tab
				restoreTerm(original) # Restore le terminal de base
			elif currChar == "ENTER": # Vérifie is la touche pressée est Entrée
				break
			else:
				continue # Si il y a une autre touche on l'ignore
		player2 = '\t' + str(currentSelectedDifficulty)
		if player2 == player1: # Vérifie si le joueur 2 est le même que le joueur 1
			player2 = '\t' + str(currentSelectedDifficulty) + "2" # Ajoute un 2 au pseudo du joueur 2 pour éviter les mêmes pseudos
	elif player2IsBot is False :
		player2 = pseudo[2:]
		if not isPlayerExisting(player2) :
			addPlayer(player2)

	while True:
		displayMenu(currentSelectedGame, player1, player2) # Affiche le menu avec le premier jeu de sélectionner
		while True:
			currChar = getKey()
			if currChar == "UP" and currentSelectedGame != 1 and isOnRules is False and isOnScoreboard is False: # Vérifie is la touche pressée est la flèche du haut
				currentSelectedGame -= 1 # Change le jeu
				printAt(10 + currentSelectedGame, (maxWidth - 11) // 2, displayGameSelected(currentSelectedGame)) # Affiche le jeu sélectionner
			if currChar == "DOWN" and currentSelectedGame != 4 and isOnRules is False and isOnScoreboard is False: # Vérifie is la touche pressée est la flèche du bas
				currentSelectedGame += 1 # Change le jeu
				printAt(10 + currentSelectedGame, (maxWidth - 11) // 2, displayGameSelected(currentSelectedGame)) # Affiche le jeu sélectionner
			if currChar == "RIGHT" and isOnRules is False and isOnScoreboard is False: # Vérifie is la touche pressée est la flèche de droite
				printAt(3, maxWidth - 9, displayGameSelected(-2)) # Affiche le button règles qui est sélectionner
				isOnRules = True
			elif currChar == "RIGHT" and isOnScoreboard is True: # Vérifie is la touche pressée est la flèche de droite
				printAt(10 + currentSelectedGame, (maxWidth - 11) // 2, displayGameSelected(currentSelectedGame)) # Affiche les règles qui sont sélectionner
				isOnScoreboard = False # Affiche le button scoreboard qui est sélectionner
			if currChar == "LEFT" and isOnRules: # Vérifie is la touche pressée est la flèche de gauche
				printAt(10 + currentSelectedGame, (maxWidth - 11) // 2, displayGameSelected(currentSelectedGame)) # Affiche le jeu sélectionner
				isOnRules = False
			elif currChar == "LEFT": # Vérifie is la touche pressée est la flèche de gauche
				printAt(3, 8, displayGameSelected(-1)) # Affiche le jeu sélectionner
				isOnScoreboard = True
			elif currChar == "TAB": # Vérifie is la touche pressée est Tab
				restoreTerm(original) # Restore le terminal de base
			elif currChar == "ENTER": # Vérifie is la touche pressée est Entrée
				break
			else:
				continue # Si il y a une autre touche on l'ignore
		if isOnRules: # Si il est sur le bouton règles
			rules(1)
			isOnRules = False
		elif isOnScoreboard: # Si il est sur le bouton scoreboard
			scoreboard()
			isOnScoreboard = False
		elif currentSelectedGame == 1: # Si le jeu 1 est sélectionner (devinette)
			devinette(player1, player2)
			print("\x1b[?25l", end='', flush=True)
		elif currentSelectedGame == 2: # Si le jeu 2 est sélectionner (allumettes)
			allumettes(player1, player2)
		elif currentSelectedGame == 3: # Si le jeu 3 est sélectionner (morpion)
			morpion(player1, player2)
		elif currentSelectedGame == 4: # Si le jeu 4 est sélectionner (puissance 4)
			puissance4(player1, player2)

if __name__ == "__main__":
	main()