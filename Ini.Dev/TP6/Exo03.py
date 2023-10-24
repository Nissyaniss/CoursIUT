def powerRecursive(a : int, n : int) -> int:
	x : int

	x = 0

	if n == 1:
		return a
	elif n % 2 == 0:
		x = powerRecursive(a, n // 2)
		return x * x
	elif n % 2 == 1:
		x = powerRecursive(a, (n - 1) // 2)
		return a * x * x
	return a

if __name__ == "__main__":
	print(powerRecursive(10, 10))

