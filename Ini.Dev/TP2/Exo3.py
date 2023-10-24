import math

if __name__ == "__main__":
	delta	: float
	x1		: float
	x2		: float
	a		: float
	b		: float
	c		: float
	end		: int

	a = 0
	b = 0
	c = 0
	end = 0

	print("With the form : ax^2 +bx + c.")
	while end == 0:
		try:
			a = float(input("Enter a : "))
			b = float(input("Enter b : "))
			c = float(input("Enter c : "))
			end = 1
		except ValueError:
			print("ERROR : Value incorrect")

	delta = pow(b, 2) - (4 * a * c)
	if delta == 0:
		x1 = -b / (2 * a)
		print(f"Your answer is x = {x1}")
	elif delta > 0:
		x1 = (-b - math.sqrt(delta)) / (2 * a)
		x2 = (-b + math.sqrt(delta)) / (2 * a)
		print(f"Your answer is x1 = {x1} and x2 = {x2}")
	elif delta < 0:
		print("ERROR : There is no solution")
