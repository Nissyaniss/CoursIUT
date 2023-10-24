def powerRecursive(a : int, n : int) -> int:
	if (n < 0):
		return (0)
	if (n == 0):
		return (1)
	if (n == 1):
		return (a)
	else:
		return (a * powerRecursive(a, n - 1))

if __name__ == "__main__":
	print(powerRecursive(10, 1000))

