from colorama import Fore, Back
import sys
from os import system, get_terminal_size
import main
from typing import Tuple

from termUtils import setTermCursor, displayEmptySquare

def DisplayMenu():
	i : int
	maxSize : Tuple[int, int]

	i = 1
	maxSize = displayEmptySquare()

	# ═══════════════╦═══════════════╦═══════════════
	for i in range(1, 45):
		setTermCursor(maxSize[1] // 2 - 10, maxSize[0] // 2 - 24 + i, "═")
		if i == 15 or i == 30:
			setTermCursor(maxSize[1] // 2 - 10, maxSize[0] // 2 - 24 + i, "╦")

	# ═══════════════════════════════════════════════
	for i in range(1, 45):
		setTermCursor(maxSize[1] // 2 - 4, maxSize[0] // 2 - 24 + i, "═")

	# ═══════════════════════════════════════════════
	for i in range(1, 45):
		setTermCursor(maxSize[1] // 2 + 2, maxSize[0] // 2 - 24 + i, "═")

	# ═══════════════╩═══════════════╩═══════════════
	for i in range(1, 45):
		setTermCursor(maxSize[1] // 2 + 8, maxSize[0] // 2 - 24 + i, "═")
		if i == 15 or i == 30:
			setTermCursor(maxSize[1] // 2 + 8, maxSize[0] // 2 - 24 + i, "╩")

	# first bar
	setTermCursor(maxSize[1] // 2 - 10, maxSize[0] // 2 - 24, "╔")
	for i in range(1, 18):
		setTermCursor(maxSize[1] // 2 - 10 + i, maxSize[0] // 2 - 24, "║")
		if i == 6 or i == 12:
			setTermCursor(maxSize[1] // 2 - 10 + i, maxSize[0] // 2 - 24, "╠")
	setTermCursor(maxSize[1] // 2 - 9 + i, maxSize[0] // 2 - 24, "╚")

	# second column
	for i in range(1, 18):
		setTermCursor(maxSize[1] // 2 - 10 + i, maxSize[0] // 2 - 9, "║")
		if i == 6 or i == 12:
			setTermCursor(maxSize[1] // 2 - 10 + i, maxSize[0] // 2 - 9, "╬")

	# third column
	for i in range(1, 18):
		setTermCursor(maxSize[1] // 2 - 10 + i, maxSize[0] // 2 + 6, "║")
		if i == 6 or i == 12:
			setTermCursor(maxSize[1] // 2 - 10 + i, maxSize[0] // 2 + 6, "╬")

	# final bar
	setTermCursor(maxSize[1] // 2 - 10, maxSize[0] // 2 + 21, "╗")
	for i in range(1, 18):
		setTermCursor(maxSize[1] // 2 - 10 + i, maxSize[0] // 2 + 21, "║")
		if i == 6 or i == 12:
			setTermCursor(maxSize[1] // 2 - 10 + i, maxSize[0] // 2 + 21, "╣")
	setTermCursor(maxSize[1] // 2 - 9 + i, maxSize[0] // 2 + 21, "╝")

	print()
	DisplaySelectedCase(1, 1)

def DisplaySelectedCase(selectedCase: int, selectedCasePrevious : int):
	i : int
	maxWidth : int
	maxHeight : int

	i = 0
	maxWidth = get_terminal_size().columns - 3
	maxHeight = get_terminal_size().lines - 3

	if selectedCase == 1:
		while i <= 4:
			setTermCursor(maxHeight // 2 - 9 + i, maxWidth // 2 - 23, Fore.BLACK + Back.WHITE + " " * 14)
			i = i + 1
		if not (selectedCasePrevious == selectedCase):
			RestorePreviousCase(selectedCasePrevious)
	elif selectedCase == 2:
		while i <= 4:
			setTermCursor(maxHeight // 2 - 9 + i, maxWidth // 2 - 8, Fore.BLACK + Back.WHITE + " " * 14)
			i = i + 1
		if not (selectedCasePrevious == selectedCase):
			RestorePreviousCase(selectedCasePrevious)
	elif selectedCase == 3:
		while i <= 4:
			setTermCursor(maxHeight // 2 - 9 + i, maxWidth // 2 + 7, Fore.BLACK + Back.WHITE + " " * 14)
			i = i + 1
		if not (selectedCasePrevious == selectedCase):
			RestorePreviousCase(selectedCasePrevious)

	elif selectedCase == 4:
		while i <= 4:
			setTermCursor(maxHeight // 2 - 3 + i, maxWidth // 2 - 23, Fore.BLACK + Back.WHITE + " " * 14)
			i = i + 1
		if not (selectedCasePrevious == selectedCase):
			RestorePreviousCase(selectedCasePrevious)
	elif selectedCase == 5:
		while i <= 4:
			setTermCursor(maxHeight // 2 - 3 + i, maxWidth // 2 - 8, Fore.BLACK + Back.WHITE + " " * 14)
			i = i + 1
		if not (selectedCasePrevious == selectedCase):
			RestorePreviousCase(selectedCasePrevious)
	elif selectedCase == 6:
		while i <= 4:
			setTermCursor(maxHeight // 2 - 3 + i, maxWidth // 2 + 7, Fore.BLACK + Back.WHITE + " " * 14)
			i = i + 1
		if not (selectedCasePrevious == selectedCase):
			RestorePreviousCase(selectedCasePrevious)

	elif selectedCase == 7:
		while i <= 4:
			setTermCursor(maxHeight // 2 + 3 + i, maxWidth // 2 - 23, Fore.BLACK + Back.WHITE + " " * 14)
			i = i + 1
		if not (selectedCasePrevious == selectedCase):
			RestorePreviousCase(selectedCasePrevious)
	elif selectedCase == 8:
		while i <= 4:
			setTermCursor(maxHeight // 2 + 3 + i, maxWidth // 2 - 8, Fore.BLACK + Back.WHITE + " " * 14)
			i = i + 1
		if not (selectedCasePrevious == selectedCase):
			RestorePreviousCase(selectedCasePrevious)
	elif selectedCase == 9:
		while i <= 4:
			setTermCursor(maxHeight // 2 + 3 + i, maxWidth // 2 + 7, Fore.BLACK + Back.WHITE + " " * 14)
			i = i + 1
		if not (selectedCasePrevious == selectedCase):
			RestorePreviousCase(selectedCasePrevious)
	print()

def RestorePreviousCase(selectedCase: int):
	i : int
	maxWidth : int
	maxHeight : int

	i = 0
	maxWidth = get_terminal_size().columns - 3
	maxHeight = get_terminal_size().lines - 3

	if selectedCase == 1:
		while i <= 4:
			setTermCursor(maxHeight // 2 - 9 + i, maxWidth // 2 - 23, Fore.RESET + Back.RESET + " " * 14)
			i = i + 1
	elif selectedCase == 2:
		while i <= 4:
			setTermCursor(maxHeight // 2 - 9 + i,maxWidth // 2 - 8, Fore.RESET + Back.RESET + " " * 14)
			i = i + 1
	elif selectedCase == 3:
		while i <= 4:
			setTermCursor(maxHeight // 2 - 9 + i,maxWidth // 2 + 7, Fore.RESET + Back.RESET + " " * 14)
			i = i + 1

	elif selectedCase == 4:
		while i <= 4:
			setTermCursor(maxHeight // 2 - 3 + i, maxWidth // 2 - 23, Fore.RESET + Back.RESET + " " * 14)
			i = i + 1
	elif selectedCase == 5:
		while i <= 4:
			setTermCursor(maxHeight // 2 - 3 + i, maxWidth // 2 - 8, Fore.RESET + Back.RESET + " " * 14)
			i = i + 1
	elif selectedCase == 6:
		while i <= 4:
			setTermCursor(maxHeight // 2 - 3 + i, maxWidth // 2 + 7, Fore.RESET + Back.RESET + " " * 14)
			i = i + 1

	elif selectedCase == 7:
		while i <= 4:
			setTermCursor(maxHeight // 2 + 3 + i, maxWidth // 2 - 23, Fore.RESET + Back.RESET + " " * 14)
			i = i + 1
	elif selectedCase == 8:
		while i <= 4:
			setTermCursor(maxHeight // 2 + 3 + i, maxWidth // 2 - 8, Fore.RESET + Back.RESET + " " * 14)
			i = i + 1
	elif selectedCase == 9:
		while i <= 4:
			setTermCursor(maxHeight // 2 + 3 + i, maxWidth // 2 + 7, Fore.RESET + Back.RESET + " " * 14)
			i = i + 1
	print()

def start(player1 : str, player2 : str, original : list[int]):
	currChar : str
	selectedCase : int

	currChar = ""
	selectedCase = 1

	DisplayMenu()
	while True:
		while True:
			currChar = sys.stdin.read(1)
			if currChar == '\x1b':
				currChar = sys.stdin.read(1)
				currChar = sys.stdin.read(1)
				if currChar == 'A' and selectedCase > 3 :
					selectedCase = selectedCase - 3
					DisplaySelectedCase(selectedCase, selectedCase + 3)
				elif currChar == 'B' and selectedCase <= 6:
					selectedCase = selectedCase + 3
					DisplaySelectedCase(selectedCase, selectedCase - 3)
				elif currChar == 'C' and selectedCase != 9:
					selectedCase = selectedCase + 1
					DisplaySelectedCase(selectedCase, selectedCase - 1)
				elif currChar == 'D' and selectedCase != 1:
					selectedCase = selectedCase - 1
					DisplaySelectedCase(selectedCase, selectedCase + 1)
			elif currChar == '\n':
				system("clear")
				print(selectedCase)
				exit()
			elif currChar == 'q' or currChar == 'Q':
				print(Fore.RESET + Back.RESET)
				return