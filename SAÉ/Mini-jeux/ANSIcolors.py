def inverseColor(string : str) -> str:
	return '\x1b[38:5:0m' + '\x1b[48:5:15m' + string + '\x1b[m'

def stringRed(string : str) -> str:
	return '\x1b[38:5:9m' + string + '\x1b[m'

def stringYellow(string : str) -> str:
	return '\x1b[38:5:11m' + string + '\x1b[m'