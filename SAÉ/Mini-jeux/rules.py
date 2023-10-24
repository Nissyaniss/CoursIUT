import sys
from os import system, get_terminal_size
from termUtils import setTermCursor, displayEmptySquare
from colorama import Fore, Back
from typing import Tuple

import main

def DisplayMenu() -> None:
	"""
	La fonction `DisplayMenu` affiche le menu des règles.
	"""

	maxSize : Tuple[int, int]

	maxSize = displayEmptySquare()

	setTermCursor(6, (maxSize[0] - 23) // 2, "┌─────────────────────────┐")
	setTermCursor(7, (maxSize[0] - 23) // 2, "│         BONJOUR         │")
	setTermCursor(8, (maxSize[0] - 23) // 2, "│    Liste des règles     │")
	setTermCursor(9, (maxSize[0] - 23) // 2, "└─────────────────────────┘")
	setTermCursor(maxSize[1] + 1, 3, "Appuyer sur \"q\" pour quitter")

def DisplayGameSelected(currentSelectedGame : int) -> str:
	"""
	La fonction "DisplayGameSelected" prend le jeu actuellement sélectionné et met a jour l'affichage
	et retourne un chaîne correctement formater pour être sélectionné.
	
	@param currentSelectedGame Un nombre entier représentant le jeu actuellement sélectionné.

	@return La chaîne correctement formater pour être sélectionner.
	"""

	gameStr: str
	maxWidth = get_terminal_size().columns - 1

	if currentSelectedGame == 1:
		gameStr = "Devinette"
		setTermCursor(12, (maxWidth - 9) // 2, "  Allumette")
		setTermCursor(13, (maxWidth - 9) // 2, "  Morpion")
		setTermCursor(14, (maxWidth - 9) // 2, "  Puissance 4")
	elif currentSelectedGame == 2:
		setTermCursor(11, (maxWidth - 9) // 2, "  Devinette")
		gameStr = "Allumette"
		setTermCursor(13, (maxWidth - 9) // 2, "  Morpion")
		setTermCursor(14, (maxWidth - 9) // 2, "  Puissance 4")
	elif currentSelectedGame == 3:
		setTermCursor(11, (maxWidth - 9) // 2, "  Devinette")
		setTermCursor(12, (maxWidth - 9) // 2, "  Allumette")
		gameStr = "Morpion"
		setTermCursor(14, (maxWidth - 9) // 2, "  Puissance 4")
	elif currentSelectedGame == 4:
		setTermCursor(11, (maxWidth - 9) // 2, "  Devinette")
		setTermCursor(12, (maxWidth - 9) // 2, "  Allumette")
		setTermCursor(13, (maxWidth - 9) // 2, "  Morpion")
		gameStr = "Puissance 4" 
	else :
		gameStr = "ERROR"

	return str(">" + Back.WHITE + Fore.BLACK + gameStr + Back.RESET + Fore.RESET + " ")

def DisplayRulesTitle(maxWidth : int, maxHeight : int, gameStr : str) -> None:
	"""
	La fonction DisplayRulesTitle prend trois paramètres - maxWidth, maxHeight et gameStr - et affiche le titre
	du jeu ou les règles sont actuellement affiché.
	
	@param maxWidth La largeur maximale de la zone d'affichage du titre des règles.
	@param maxHeight La hauteur maximale de la zone d'affichage du titre des règles du jeu.
	@param gameStr Le paramètre gameStr est une chaîne qui représente le titre du jeu.
	"""

	system("clear")
	setTermCursor(2, (maxWidth - 10) // 2,  "┌" + len(gameStr) * "─" + "┐")
	setTermCursor(3, (maxWidth - 10) // 2,  "│" + f"{gameStr}" +       "│")
	setTermCursor(4, (maxWidth - 10) // 2,  "└" + len(gameStr) * "─" + "┘")
	setTermCursor(maxHeight + 1, 3, "Appuyer sur \"q\" pour quitter")

def printRule(gameStr : str, ruleStr : str, currentSelectedGame : int, original : list[int], player1 : str, player2 : str) -> None:
	"""
	La fonction prend en compte divers paramètres et imprime une règle pour un jeu basée sur la chaîne
	de jeu et la chaîne de règles données.
	
	@param gameStr Une chaîne représentant le jeu.
	@param ruleStr Le paramètre `ruleStr` est une chaîne qui représente la règle du jeu. Il fournit une
	description de la façon dont le jeu est joué.
	@param currentSelectedGame Le paramètre currentSelectedGame est un entier qui représente l'index du
	jeu en actuel.
	@param original Le paramètre «original» est une liste d'entiers représentant l'état original du
	terminal.
	@param player1 Le nom du premier joueur.
	@param player2 Le nom du deuxième joueur.
	"""

	maxHeight = get_terminal_size().lines - 3
	maxWidth = get_terminal_size().columns - 3

	DisplayRulesTitle(maxWidth, maxHeight, gameStr)
	setTermCursor(8, (maxWidth - 77) // 2, ruleStr)
	while True:
		currChar = sys.stdin.read(1)
		if currChar == 'q' or currChar == 'Q':
			start(currentSelectedGame, player1, player2, original)

def start(currentSelectedGame : int, player1 : str, player2 : str, original : list[int]) -> None:
	"""
	La fonction "start" prend en compte les paramètres du jeu actuellement sélectionné, les noms des
	joueurs et une liste originale, et affiche le menu et enregistre les différent inputs du joueurs.
	
	@param currentSelectedGame Le paramètre currentSelectedGame est un entier qui représente l'index du
	jeu actuellement sélectionné.
	@param player1 Le nom du premier joueur.
	@param player2 Le nom du deuxième joueur.
	@param original Le paramètre «original» est une liste d'entiers représentant l'état original du
	terminal.
	"""

	maxWidth : int

	maxWidth = get_terminal_size().columns - 2

	DisplayMenu()
	setTermCursor(10 + currentSelectedGame, (maxWidth - 8) // 2, DisplayGameSelected(currentSelectedGame))
	while True:
		currChar = sys.stdin.read(1)
		if currChar == '\x1b':
			currChar = sys.stdin.read(1)
			currChar = sys.stdin.read(1)
			if currChar == 'A' and currentSelectedGame != 1:
				currentSelectedGame -= 1
				setTermCursor(10 + currentSelectedGame, (maxWidth - 8) // 2, DisplayGameSelected(currentSelectedGame))
			if currChar == 'B' and currentSelectedGame != 4:
				currentSelectedGame += 1
				setTermCursor(10 + currentSelectedGame, (maxWidth - 8) // 2, DisplayGameSelected(currentSelectedGame))
		elif currChar == 'q' or currChar == 'Q':
			main.start(currentSelectedGame, player1, player2, original)
		elif currChar == '\n':
			system("clear")
			break
	if currentSelectedGame == 1:
		printRule("DEVINETTE", "Le joueur 1 rentre un chiffre et le joueur 2 doit le deviner en moins de temps possible !", 1, original, player1, player2)
	elif currentSelectedGame == 2:
		printRule("ALLUMETTES", "Chaque joueur retire 1 - 3 allumettes jusqu'a ce qui en ai plus ! Le perdant est celui qui prend la dernière.", 2, original, player1, player2)
	elif currentSelectedGame == 3:
		printRule("MORPION", "Chacun son tour les joueurs place un pion le premier à en aligner 3 a gagné !", 3, original, player1, player2)
	elif currentSelectedGame == 4:
		printRule("PUISSANCE 4", "Chacun son tour les joueurs place un pion le premier à en aligner 4 a gagné !", 4, original, player1, player2)