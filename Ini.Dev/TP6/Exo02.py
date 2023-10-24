def sommeRRecursive(n : int) -> int:
	if n == 1:
		return 1
	else:
		return n + sommeRRecursive(n - 1)
	
def sommeRIterative(n : int) -> int:
	res : int
	
	res = 0

	while n > 1:
		res += n
		n -= 1
	return res + 1

if __name__ == "__main__":
	print(sommeRIterative(5))
	print(sommeRRecursive(5))
