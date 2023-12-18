from os import get_terminal_size

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
		playerStr = player1
		printAt(12, maxWidth // 2 - len(player1) + 2, "  " + player2)
	elif currentSelectedPlayer == 2:
		printAt(11, maxWidth // 2 - len(player1) + 2, "  " + player1)
		playerStr = player2
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
	maxTries = 15
	tries = 0

	displayEmptySquare()
	displayMenuPlayer()
	while True:
		printAt(10 + currentSelectedPlayer, maxWidth // 2 - len(player1) + 3, DisplaySelectedPlayer(currentSelectedPlayer, player1, player2))
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
	while True:
		displayEmptySquare()
		centerText("Devinez : " + len(solution) * " ") # Demande le nombre à deviner
		while True:
			setCursorPosition(maxHeight // 2, (maxWidth // 2 + 4) + len(guess))
			currChar = getKey()
			if currChar.isdigit() and len(guess) < 3:
				printAt(maxHeight // 2, (maxWidth // 2 + 5) - 1 + len(guess), currChar)
				guess += currChar
			elif currChar == "ENTER" and len(guess) > 0:
				break
			elif currChar == "TAB":
				return
			elif currChar == "BACKSPACE":
				if len(guess) != 0:
					printAt(maxHeight // 2, (maxWidth // 2 + 4) - 1 + len(guess), " ")
					guess = guess[:-1]
		displayMenuMaster(guess)
		print("\x1b[?25l", end='', flush=True)
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
			centerText(f"{master} a gagné car {guesser} n'a pas trouvé en {maxTries} essais. La réponse était {solution}.")
			addPoint(master, 1)
			while True:
				currChar = getKey()
				if currChar == "TAB":
					return
		elif currentSelectedOption == 3: # Vérifie si le joueur a trouvé
			print("\x1b[?25l", end='', flush=True)
			displayEmptySquare()
			centerText(f"{guesser} a gagné car il a trouvé en {tries}/{maxTries} essais")
			addPoint(guesser, 1)
			while True:
				currChar = getKey()
				if currChar == "TAB":
					return