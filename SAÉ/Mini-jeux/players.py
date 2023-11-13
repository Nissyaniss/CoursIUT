import json
from termUtils import printAt

def isPlayerExisting(player: str) -> bool:
	data: dict[str, tuple[int, int, int, int]]

	with open("players.json", "r") as jsonFile:
		data = json.load(jsonFile)

	if player in data:
		return True
	else:
		return False

def addPlayer(player: str) -> None:
	data: dict[str, tuple[int, int, int, int]]

	with open("players.json", "r") as jsonFile:
		data = json.load(jsonFile)

	data.update({player : (0, 0, 0, 0)})

	with open("players.json", "w") as outputFile:
		json.dump(data, outputFile, sort_keys=True, indent='\t', separators=(',', ': '))

def addPoint(player: str, game: int) -> None:
	data: dict[str, tuple[int, int, int, int]]

	with open("players.json", "r") as jsonFile:
		data = json.load(jsonFile)

	playerData = data[player]
	if game == 1:
		playerData = (playerData[0] + 1, playerData[1],
					  playerData[2], playerData[3])
	elif game == 2:
		playerData = (playerData[0], playerData[1] +
					  1, playerData[2], playerData[3])
	elif game == 3:
		playerData = (playerData[0], playerData[1],
					  playerData[2] + 1, playerData[3])
	else:
		playerData = (playerData[0], playerData[1],
					  playerData[2], playerData[3] + 1)

	data[player] = playerData
	with open("players.json", "w") as outputFile:
		json.dump(data, outputFile, sort_keys=True, indent='\t', separators=(',', ': '))

def printScoreboard(player1: str, player2: str) -> None:
	data: dict[str, tuple[int, int, int, int]]
	playerFormat : str

	with open("players.json", "r") as jsonFile:
		data = json.load(jsonFile)

	if len(player1) > 10:
		playerFormat = player1[:10] + "..."
	else:
		playerFormat = player1
	printAt(6, 5, f"{playerFormat} :")
	printAt(7, 6, f"Devinette   = {data[player1][0]}")
	printAt(8, 6, f"Allumette   = {data[player1][1]}")
	printAt(9, 6, f"Morpion     = {data[player1][2]}")
	printAt(10, 6, f"Puissance 4 = {data[player1][3]}")

	if len(player2) > 10:
		playerFormat = player2[:10] + "..."
	else:
		playerFormat = player2
	printAt(12, 5, f"{playerFormat} :")
	printAt(13, 6, f"Devinette   = {data[player2][0]}")
	printAt(14, 6, f"Allumette   = {data[player2][1]}")
	printAt(15, 6, f"Morpion     = {data[player2][2]}")
	printAt(16, 6, f"Puissance 4 = {data[player2][3]}")