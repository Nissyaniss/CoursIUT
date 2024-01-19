from os import get_terminal_size
import random
from time import sleep

from ANSIcolors import inverseColor
from players import addPoint
from termUtils import setCursorPosition, displayEmptySquare, printAt, centerTextAtLine, centerText, getKey

def displayMenuMaster(guess : str) -> None:
	"""
	Affiche le menu du maître du jeu
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

	if currentSelectedOption == 1:
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
		if player1[0] == '\t' and player2[0] == '\t':
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
	if master[0] != '\t':
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
	else:
		solution = str(random.randint(1, 999))
	while True:
		displayEmptySquare()
		if guesser[0] == '\t':
			if guesser[1] == "1":
				if isFirstPlay:
					result = random.randint(minPrev, maxPrev)
				if currentSelectedOption == 1 and minPrev != maxPrev and not isFirstPlay:
					minPrev = result + 1
				elif currentSelectedOption == 2 and maxPrev != minPrev and not isFirstPlay:
					maxPrev = result - 1
				if minPrev != maxPrev and not isFirstPlay:
					result = random.randint(minPrev, maxPrev)
				if currentSelectedOption != 3:
					tries += 1
					isFirstPlay = False
					if maxPrev == minPrev:
						result = maxPrev
					centerText("Devinez : " + str(result)) # Demande le nombre à deviner
					sleep(1)
					displayEmptySquare()
					print("\x1b[?25l", end='', flush=True)
					displayMenuMaster(f"{str(result)}")
				if master[0] == '\t':
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
				else:
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
			elif guesser[1] == "2":
				if random.randint(0, 1):
					result = (start + end) // 2
					isFirstPlay = False
					if result == int(solution):
						tries += 1
						centerText("Devinez : " + str(result)) # Demande le nombre à deviner
						sleep(1)
						displayEmptySquare()
						print("\x1b[?25l", end='', flush=True)
						displayMenuMaster(f"{str(result)}")
					elif result < int(solution):
						start = result + 1
						tries += 1
						centerText("Devinez : " + str(result)) # Demande le nombre à deviner
						sleep(1)
						displayEmptySquare()
						print("\x1b[?25l", end='', flush=True)
						displayMenuMaster(f"{str(result)}")
					else:
						end = result - 1
						tries += 1
						centerText("Devinez : " + str(result)) # Demande le nombre à deviner
						sleep(1)
						displayEmptySquare()
						print("\x1b[?25l", end='', flush=True)
						displayMenuMaster(f"{str(result)}")
				else:
					if isFirstPlay:
						result = random.randint(start, end)
					elif currentSelectedOption == 1 and start != end:
						start = result + 1
						result = random.randint(start, end)
					elif currentSelectedOption == 2 and start != end:
						end = result - 1
						result = random.randint(start, end)
					if currentSelectedOption != 3:
						tries += 1
						isFirstPlay = False
						if start == end:
							result = end
						centerText("Devinez : " + str(result)) # Demande le nombre à deviner
						sleep(1)
						displayEmptySquare()
						print("\x1b[?25l", end='', flush=True)
						displayMenuMaster(f"{str(result)}")
				if master[0] == '\t':
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
				else:
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
			if guesser[1] == "3":
				while start <= end:
					displayEmptySquare()
					result = (start + end) // 2
					if result == int(solution):
						centerText("Devinez : " + str(result)) # Demande le nombre à deviner
						sleep(1)
						displayEmptySquare()
						print("\x1b[?25l", end='', flush=True)
						if master[0] == '\t':
							displayMenuMaster(str(result))
							centerTextAtLine(13, displaySelectedOption(3))
							sleep(1)
							print("\x1b[?25h", end='', flush=True)
							break
					elif result < int(solution):
						start = result + 1
						tries += 1
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
					else:
						end = result - 1
						tries += 1
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
					if master[0] == '\t':
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
					else:
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
		else:
			centerText("Devinez : ") # Demande le nombre à deviner
			while True:
				setCursorPosition(maxHeight // 2, (maxWidth // 2 + 4) + 1 + len(guess))
				currChar = getKey()
				if currChar.isdigit() and len(guess) < 3:
					printAt(maxHeight // 2, (maxWidth // 2 + 5) + len(guess), currChar)
					guess += currChar
				elif currChar == "ENTER" and len(guess) > 0:
					break
				elif currChar == "TAB":
					return
				elif currChar == "BACKSPACE":
					if len(guess) != 0:
						printAt(maxHeight // 2, (maxWidth // 2 + 4) + len(guess), " ")
						guess = guess[:-1]
			displayMenuMaster(guess)
			print("\x1b[?25l", end='', flush=True)
			if master[0] == '\t':
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
			else:
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
			tries = tries + 1
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