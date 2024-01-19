from os import get_terminal_size
import random
from time import sleep

from ANSIcolors import inverseColor
from players import addPoint
from termUtils import setCursorPosition, displayEmptySquare, printAt, centerTextAtLine, centerText, getKey

def displayMenuMaster(guess : str) -> None:
	"""
	Affiche le menu du maître du jeu

	Entrée : guess : str
	guess symbolise le nombre à deviner
	"""
	displayEmptySquare()
	centerTextAtLine(6, "┌───"+ "─" * len(guess) + "───┐")
	centerTextAtLine(7, f"│   {guess}   │")
	centerTextAtLine(8, "└───"+ "─" * len(guess) + "───┘")

def displaySelectedOption(currentSelectedOption : int) -> str:
	"""
	Affiche l'option sélectionnée

	Entrée : currentSelectedOption : int
	currentSelectedOption symbolise l'option sélectionnée

	Sortie : str
	Symbolise l'option sélectionnée formaté
	"""
	optionStr: str

	if currentSelectedOption == 1: # Affiche l'option sélectionnée
		optionStr = "Plus Grand"
		centerTextAtLine(12, "  Plus Petit ")
		centerTextAtLine(13, "  C'est Bon !")
	elif currentSelectedOption == 2:
		centerTextAtLine(11, "  Plus Grand ")
		optionStr = "Plus Petit"
		centerTextAtLine(13, "  C'est Bon !")
	elif currentSelectedOption == 3:
		centerTextAtLine(11, "  Plus Grand ")
		centerTextAtLine(12, "  Plus Petit ")
		optionStr = "C'est Bon!"
	else :
		optionStr = "ERROR"

	return ">" + inverseColor(optionStr) + "  "

def displayMenuPlayer() -> None:
	"""
	Affiche le menu du joueur
	"""
	displayEmptySquare()
	centerTextAtLine(6, "┌─────────────────────────────────┐")
	centerTextAtLine(7, "│   Qui fera deviner à l'autre    │")
	centerTextAtLine(8, "└─────────────────────────────────┘")

def DisplaySelectedPlayer(currentSelectedPlayer : int, player1 : str, player2 : str) -> str:
	"""
	Affiche le joueur sélectionné

	Entrée : currentSelectedPlayer : int
	currentSelectedPlayer symbolise le joueur sélectionné

	Entrée : player1 : str
	player1 symbolise le nom du joueur 1

	Entrée : player2 : str
	player2 symbolise le nom du joueur 2
	
	Sortie : str
	Symbolise le joueur sélectionné formaté
	"""
	playerStr: str
	maxWidth : int

	maxWidth = get_terminal_size().columns - 3 # Récupère la taille du terminal
	
	if currentSelectedPlayer == 1: # Affiche le joueur sélectionné
		if player1 == '\t' and player2 == '\t':
			playerStr = "Bot"
			printAt(12, maxWidth // 2 - len("Bot") + 2, "  " + "Bot")
		elif player1 == '\t':
			playerStr = "Bot"
			printAt(12, maxWidth // 2 - len("Bot") + 2, "  " + player2)
		else:
			playerStr = player1
			printAt(12, maxWidth // 2 - len(player1) + 2, "  " + player2)
	elif currentSelectedPlayer == 2:
		if player1 == '\t' and player2 == '\t':
			playerStr = "Bot"
			printAt(11, maxWidth // 2 - len("Bot") + 2, "  " + "Bot")
		elif player2 == '\t':
			playerStr = "Bot"
			printAt(12, maxWidth // 2 - len(player1) + 2, "  " + player2)
		else:
			playerStr = player2
			printAt(11, maxWidth // 2 - len(player1) + 2, "  " + player1)
	else :
		playerStr = "ERROR"

	return str(">" + inverseColor(playerStr) + "  ")

def start(player1 : str, player2 : str) -> None:
	"""
	Démarre le jeu

	Entrée : player1 : str
	player1 symbolise le nom du joueur 1

	Entrée : player2 : str
	player2 symbolise le nom du joueur 2
	"""
	solution : str
	guess : str
	currChar : str
	currentSelectedOption : int
	maxWidth : int
	maxHeight : int
	strikes : int
	currentSelectedPlayer : int
	master : str
	maxTries : int
	tries : int
	start : int
	end : int
	result : int
	maxPrev : int
	minPrev : int
	isFirstPlay : bool

	maxWidth = get_terminal_size().columns - 3 # Récupère la taille du terminal
	maxHeight = get_terminal_size().lines - 3
	currentSelectedOption = 1
	currentSelectedPlayer = 1
	master = ''
	guesser = ''
	solution = ''
	guess = ''
	currChar = ""
	strikes = 0
	maxTries = 25
	tries = 0
	start = 1
	end = 999
	result = 0
	maxPrev = 999
	minPrev = 1
	isFirstPlay = True

	displayEmptySquare()
	displayMenuPlayer()
	while True:
		if player1[0] == '\t' and player2[0] == '\t': # Affiche le joueur sélectionné
			break
		elif player1[0] == '\t':
			printAt(10 + currentSelectedPlayer, maxWidth // 2 - len("Bot") + 2, DisplaySelectedPlayer(currentSelectedPlayer, "Bot", player2))
		elif player2[0] == '\t':
			printAt(10 + currentSelectedPlayer, maxWidth // 2 - len("Bot") + 2, DisplaySelectedPlayer(currentSelectedPlayer, player1, "Bot"))
		else:
			printAt(10 + currentSelectedPlayer, maxWidth // 2 - len("Bot") + 2, DisplaySelectedPlayer(currentSelectedPlayer, player1, player2))
		currChar = getKey()
		if currChar == "UP" and currentSelectedPlayer != 1: # Déplace le curseur
			currentSelectedPlayer -= 1
		elif currChar == "DOWN" and currentSelectedPlayer != 2:
			currentSelectedPlayer += 1
		if currChar == "ENTER":
			break
		elif currChar == "TAB":
			return
	if currentSelectedPlayer == 1:
		master = player1
		guesser = player2
	else:
		master = player2
		guesser = player1
	print("\x1b[?25h", end='')
	displayEmptySquare()
	if master[0] != '\t': # Demande le nombre à faire deviner
		centerText("Nombre : ") # Demande le nombre à faire deviner
		while True:
			currChar = getKey()
			if currChar.isdigit() and len(solution) < 3:
				solution += currChar
			elif currChar == "ENTER" and len(solution) > 0:
				break
			elif currChar == "TAB":
				return
			elif currChar == "BACKSPACE":
				if len(solution) != 0:
					solution = solution[:-1]
	else: # Génère un nombre aléatoire
		solution = str(random.randint(1, 999))
	while True:
		displayEmptySquare()
		if guesser[0] == '\t': # Si le joueur est un bot
			if guesser[1] == "1": # Si le bot est un bot de difficulté 1
				if isFirstPlay: # Si c'est le premier tour
					result = random.randint(minPrev, maxPrev) # Génère un nombre aléatoire
				if currentSelectedOption == 1 and minPrev != maxPrev and not isFirstPlay:
					minPrev = result + 1 # Si le bot a déjà joué et que le nombre est plus petit que le précédent
				elif currentSelectedOption == 2 and maxPrev != minPrev and not isFirstPlay:
					maxPrev = result - 1 # Si le bot a déjà joué et que le nombre est plus grand que le précédent
				if minPrev != maxPrev and not isFirstPlay:
					result = random.randint(minPrev, maxPrev) # Génère un nombre aléatoire
				if currentSelectedOption != 3:
					tries += 1 # Incrémente le nombre d'essais
					isFirstPlay = False # Ce n'est plus le premier tour
					if maxPrev == minPrev: # Si le nombre est le même que le précédent
						result = maxPrev
					centerText("Devinez : " + str(result)) # Demande le nombre à deviner
					sleep(1)
					displayEmptySquare()
					print("\x1b[?25l", end='', flush=True)
					displayMenuMaster(f"{str(result)}") # Affiche le menu du maître du jeu
				if master[0] == '\t': # Si le maître est un bot, il affiche la réponse du master
					if result < int(solution):
						centerTextAtLine(11, displaySelectedOption(1))
						currentSelectedOption = 1
					elif result > int(solution):
						centerTextAtLine(12, displaySelectedOption(2))
						currentSelectedOption = 2
					elif result == int(solution):
						centerTextAtLine(13, displaySelectedOption(3))
						currentSelectedOption = 3
					sleep(1)
					print("\x1b[?25h", end='', flush=True)
				else: # Si le maître est un joueur, il affiche le menu du maître du jeu
					while True:
						centerTextAtLine(10 + currentSelectedOption, displaySelectedOption(currentSelectedOption))
						currChar = getKey()
						if currChar == "UP" and currentSelectedOption != 1: # Déplace le curseur
							currentSelectedOption -= 1
						elif currChar == "DOWN" and currentSelectedOption != 3:
							currentSelectedOption += 1
						elif currChar == "TAB":
							return
						elif currChar == "ENTER":
							print("\x1b[?25h", end='', flush=True)
							break
			elif guesser[1] == "2": # Si le bot est un bot de difficulté 2
				if random.randint(0, 1): # Génère un nombre aléatoire entre 0 et 1
					result = (start + end) // 2 # Calcule la moyenne entre le max et le min
					isFirstPlay = False # Ce n'est plus le premier tour
					if result == int(solution): # Si le nombre est le même que la solution
						tries += 1 # Incrémente le nombre d'essais
					elif result < int(solution):
						start = result + 1 # Change le min
						tries += 1
					else:
						end = result - 1 # Change le max
						tries += 1
					centerText("Devinez : " + str(result)) # Demande le nombre à deviner
					sleep(1)
					displayEmptySquare()
					print("\x1b[?25l", end='', flush=True)
					displayMenuMaster(f"{str(result)}")
				else:
					if isFirstPlay: # Si c'est le premier tour
						result = random.randint(start, end) # Génère un nombre aléatoire
					if currentSelectedOption == 1 and start != end and not isFirstPlay:
						start = result + 1 # Si le bot a déjà joué et que le nombre est plus petit que le précédent
					elif currentSelectedOption == 2 and end != start and not isFirstPlay:
						end = result - 1 # Si le bot a déjà joué et que le nombre est plus grand que le précédent
					if start != end and not isFirstPlay:
						result = random.randint(start, end) # Génère un nombre aléatoire
					if currentSelectedOption != 3:
						tries += 1 # Incrémente le nombre d'essais
						isFirstPlay = False # Ce n'est plus le premier tour
						if start == end:
							result = end
						centerText("Devinez : " + str(result)) # Demande le nombre à deviner
						sleep(1)
						displayEmptySquare()
						print("\x1b[?25l", end='', flush=True)
						displayMenuMaster(f"{str(result)}")
				if master[0] == '\t': # Si le maître est un bot, il affiche la réponse du master
					if result < int(solution):
						centerTextAtLine(11, displaySelectedOption(1))
						currentSelectedOption = 1
					elif result > int(solution):
						centerTextAtLine(12, displaySelectedOption(2))
						currentSelectedOption = 2
					elif result == int(solution):
						centerTextAtLine(13, displaySelectedOption(3))
						currentSelectedOption = 3
					sleep(1)
					print("\x1b[?25h", end='', flush=True)
				else: # Si le maître est un joueur, il affiche le menu du maître du jeu
					while True:
						centerTextAtLine(10 + currentSelectedOption, displaySelectedOption(currentSelectedOption))
						currChar = getKey()
						if currChar == "UP" and currentSelectedOption != 1: # Déplace le curseur
							currentSelectedOption -= 1
						elif currChar == "DOWN" and currentSelectedOption != 3:
							currentSelectedOption += 1
						elif currChar == "TAB":
							return
						elif currChar == "ENTER":
							print("\x1b[?25h", end='', flush=True)
							break
			if guesser[1] == "3": # Si le bot est un bot de difficulté 3
				while start <= end: # Tant que le min est plus petit que le max
					displayEmptySquare()
					result = (start + end) // 2 # Calcule la moyenne entre le max et le min
					if result == int(solution): # Si le nombre est le même que la solution
						centerText("Devinez : " + str(result)) # Demande le nombre à deviner
						sleep(1)
						displayEmptySquare()
						print("\x1b[?25l", end='', flush=True)
						if master[0] == '\t': # Si le maître est un bot, il affiche la réponse du master
							displayMenuMaster(str(result))
							centerTextAtLine(13, displaySelectedOption(3))
							sleep(1)
							print("\x1b[?25h", end='', flush=True)
					elif result < int(solution): # Si le nombre est plus petit que la solution
						start = result + 1 # Change le min
						tries += 1 # Incrémente le nombre d'essais
						centerText("Devinez : " + str(result)) # Demande le nombre à deviner
						sleep(1)
						displayEmptySquare()
						print("\x1b[?25l", end='', flush=True)
						if master[0] == '\t':
							displayMenuMaster(str(result))
							centerTextAtLine(11, displaySelectedOption(1))
							sleep(1)
							print("\x1b[?25h", end='', flush=True)
						displayEmptySquare()
					else: # Si le nombre est plus grand que la solution
						end = result - 1 # Change le max
						tries += 1 # Incrémente le nombre d'essais
						centerText("Devinez : " + str(result)) # Demande le nombre à deviner
						sleep(1)
						displayEmptySquare()
						print("\x1b[?25l", end='', flush=True)
						if master[0] == '\t':
							displayMenuMaster(str(result))
							centerTextAtLine(12, displaySelectedOption(2))
							sleep(1)
							print("\x1b[?25h", end='', flush=True)
						displayEmptySquare()
					displayMenuMaster(str(result))
					if master[0] == '\t': # Si le maître est un bot, il affiche la réponse du master
						if result < int(solution):
							centerTextAtLine(11, displaySelectedOption(1))
							currentSelectedOption = 1
						elif result > int(solution):
							centerTextAtLine(12, displaySelectedOption(2))
							currentSelectedOption = 2
						elif result == int(solution):
							centerTextAtLine(13, displaySelectedOption(3))
							currentSelectedOption = 3
						sleep(1)
						print("\x1b[?25h", end='', flush=True)
					else: # Si le maître est un joueur, il affiche le menu du maître du jeu
						while True:
							centerTextAtLine(10 + currentSelectedOption, displaySelectedOption(currentSelectedOption))
							currChar = getKey()
							if currChar == "UP" and currentSelectedOption != 1: # Déplace le curseur
								currentSelectedOption -= 1
							elif currChar == "DOWN" and currentSelectedOption != 3:
								currentSelectedOption += 1
							elif currChar == "TAB":
								return
							elif currChar == "ENTER":
								print("\x1b[?25h", end='', flush=True)
								break
						if currentSelectedOption == 3:
							break
		else: # Si le joueur est un joueur
			centerText("Devinez : ") # Demande le nombre à deviner
			while True:
				setCursorPosition(maxHeight // 2, (maxWidth // 2 + 4) + 1 + len(guess))
				currChar = getKey()
				if currChar.isdigit() and len(guess) < 3: # Si le caractère est un chiffre et que le nombre n'est pas trop grand
					printAt(maxHeight // 2, (maxWidth // 2 + 5) + len(guess), currChar)
					guess += currChar
				elif currChar == "ENTER" and len(guess) > 0:
					break
				elif currChar == "TAB":
					return
				elif currChar == "BACKSPACE": # Si le caractère est un backspace et que le nombre n'est pas vide
					if len(guess) != 0:
						printAt(maxHeight // 2, (maxWidth // 2 + 4) + len(guess), " ")
						guess = guess[:-1]
			displayMenuMaster(guess)
			print("\x1b[?25l", end='', flush=True)
			if master[0] == '\t': # Si le maître est un bot, il affiche la réponse du master
				displayEmptySquare()
				print("\x1b[?25l", end='', flush=True)
				displayMenuMaster(guess)
				if int(guess) < int(solution):
					currentSelectedOption = 1
					centerTextAtLine(11, displaySelectedOption(currentSelectedOption))
				elif int(guess) > int(solution):
					currentSelectedOption = 2
					centerTextAtLine(12, displaySelectedOption(currentSelectedOption))
				else:
					currentSelectedOption = 3
					centerTextAtLine(13, displaySelectedOption(currentSelectedOption))
					sleep(1)
					print("\x1b[?25h", end='', flush=True)
					displayEmptySquare()
				sleep(1)
				print("\x1b[?25h", end='', flush=True)
				displayEmptySquare()
			else: # Si le maître est un joueur, il affiche le menu du maître du jeu
				while True:
					centerTextAtLine(10 + currentSelectedOption, displaySelectedOption(currentSelectedOption))
					currChar = getKey()
					if currChar == "UP" and currentSelectedOption != 1: # Déplace le curseur
						currentSelectedOption -= 1
					elif currChar == "DOWN" and currentSelectedOption != 3:
						currentSelectedOption += 1
					elif currChar == "TAB":
						return
					elif currChar == "ENTER":
						print("\x1b[?25h", end='', flush=True)
						break
			tries = tries + 1 # Incrémente le nombre d'essais
			if master[0] != '\t':
				if currentSelectedOption == 1 and int(guess) < int(solution): # Vérifie si la réponse est bonne
					strikes += 1
				elif currentSelectedOption == 2 and int(guess) > int(solution):
					strikes =+ 1
				elif (currentSelectedOption == 1 or currentSelectedOption == 2) and guess == solution: # Vérifie si le master a pas triché
					strikes = 3
			guess = ""
		if strikes == 3: # Vérifie si le master a pas triché
			print("\x1b[?25l", end='', flush=True)
			displayEmptySquare()
			centerText(f"{guesser} a gagné car {master} a triché. La réponse était {solution}.")
			addPoint(guesser, 1)
			while True:
				currChar = getKey()
				if currChar == "TAB":
					return
		elif tries == maxTries: # Vérifie si le joueur a pas dépassé le nombre d'essais
			print("\x1b[?25l", end='', flush=True)
			displayEmptySquare()
			if master[0] != '\t':
				centerText(f"{master} a gagné car {guesser} n'a pas trouvé en {maxTries} essais. La réponse était {solution}.")
				addPoint(master, 1)
			elif guesser[0] != '\t':
				centerText(f"Le bot a gagné car {guesser} n'a pas trouvé en {maxTries} essais. La réponse était {solution}.")
			else:
				centerText(f"Le bot a gagné car l'autre bot n'a pas trouvé en {maxTries} essais. La réponse était {solution}.")
			while True:
				currChar = getKey()
				if currChar == "TAB":
					return
		elif currentSelectedOption == 3 or result == int(solution): # Vérifie si le joueur a trouvé
			print("\x1b[?25l", end='', flush=True)
			displayEmptySquare()
			if not guesser[0] == "\t":
				centerText(f"{guesser} a gagné car il a trouvé en {tries}/{maxTries} essais")
				addPoint(guesser, 1)
			else:
				centerText(f"Le bot a gagné en {tries} essais")
			while True:
				currChar = getKey()
				if currChar == "TAB":
					return