# Exercices 1:

>Le problème posé par le programme est le fait que b n'est pas initialisé et on le corrigerai de plusieurs manière mais la plus logique serait d'ajouter:
```
...
saisir a
saisir b
afficher "a = ", a, " et b = ", b
...
```

# Exercices 2:

```c
programme ex02
debut
	avec a : entier
		 b : entier

	afficher "Entrer a:"
	saisir a
	afficher "Entrer b:"
	saisir b
	si <a > b>
		afficher a, ">", b
	sinon si <a < b>
		afficher a, "<", b
	sinon si <a = b>
		afficher a, "=", b
	sinon
		afficher "Erreur"
	finsi
fin
```

# Exercices 3

>Le nombre de carreaux N pour recouvrir S est 2 si L>l+2*e, H>h+2\*e et que L-e n'est pas multiple l+e, ni H-e de h+e est vrai

# Exercices 4

```
programme ex04
debut
	avec a: entier
		 b: entier
		 x: entier
		 c: entier
		 d: entier
	
	afficher "Rentrer a"
	saisir a
	afficher "Rentrer b"
	saisir b
	afficher "Rentrer c"
	saisir c
	afficher "Rentrer x"
	saisir x
	si a n'est pas numérique ou b n'est pas numérique ou c n'est pas numérique ou x n'est pas numérique alors
		afficher "Erreur: L'une de vos saisies n'est pas un chiffre"
	finsi
	si a = 0 alors
		afficher "Erreur: a ne peux pas être égal a 0"
	sinon alors
		d <- pow(b, 2)-4*a*c
		si d = 0 alors
			afficher "x = ", -b, "/", "2a"
		finsi
		sinon alors
			si d > 0 alors
				afficher "x1 = ", -b, "-", "sqrt(d)/2*", a
				a la ligne
				afficher "x2 = ", -b, "+", "sqrt(d)/2*", a
			sinon alors
				si d < 0 alors
					afficher "Erreur"
				finsi
			finsi
	finsi
		
```