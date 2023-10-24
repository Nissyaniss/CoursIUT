import math

def factorielle(n : int) -> int:
	i : int
	res : int

	res = 1
	for i in range(1, n+1) :
		res = res * i
	return res

if __name__ == "__main__": #idk
	temp		: str
	rayon		: float
	aire		: float
	
	temp = ""
	rayon = 0.0
	aire = 0.0
	temp = input("Saisir le rayon (ou pas) : ") #read stdout
	#NO {} AAAAAAAAAAAAAAAAH
	if temp.isnumeric():
		rayon = float(temp)
		aire = 3.14 * math.pow(rayon, 2)
		if rayon <= 10.0:
			print("Votre petite aire est", aire)
		else:
			print("Votre grande aire est", aire)
		print("Racine carrée de", aire, "est", math.sqrt(aire))

	print("\n print(\"value1\", 5, \"value2\", 10) -->")
	print("value1", 5, "value2", 10)

	print("\nnot True :", not True)
	print("not False :", not False)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	print("\n5 // 2 =", 5 // 2)
	print("5.2 // 2.2 =", 5.2 // 2.2)
	print("5.2 % 2.2 =", 5.2 % 2.2)
	print("5 / 2 =", 5 / 2)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

	print("\n\"str\" + \" str\"")
	print("str" + " str")
	print("\"str\" * 2 = \n")
	print("str" * 2)
	print("\"str\" <= \"stre\"")
	print("str" <= "stre")