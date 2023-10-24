# Exercice 1

```
fonction VerifierDate(jours : entier, mois : entier, annee : entier) retourne bool
debut
	avec anneeBis : booleen
		 moisOk : booleen

	moisOk <- Vrai

	si annee / 4 >= 1 et annee % 100 != 0 ou annee % 44 = 0 alors
		anneeBis <- Vrai
	fin si
	selon mois faire
		cas 1 : si jours > 31 alors moisOk <- Faux fin si
		cas 2 : si anneeBis et jours > 29 ou non anneeBis et jour > 28 alors moisOk <- Faux fin si
		cas 3 : si jours > 31 alors moisOk <- Faux fin si
		cas 4 : si jours > 30 alors moisOk <- Faux fin si
		cas 5 : si jours > 31 alors moisOk <- Faux fin si
		cas 6 : si jours > 30 alors moisOk <- Faux fin si
		cas 7 : si jours > 31 alors moisOk <- Faux fin si
		cas 8 : si jours > 31 alors moisOk <- Faux fin si
		cas 9 : si jours > 30 alors moisOk <- Faux fin si
		cas 10 : si jours > 31 alors moisOk <- Faux fin si
		cas 11 : si jours > 30 alors moisOk <- Faux fin si
		cas 12 : si jours > 31 alors moisOk <- Faux fin si
	fin faire
	
	retourne moisOk
fin VerifierDate

fonction diffAn(jour : entier, mois : entier, an : entier, jour1 : entier, mois1 : entier, an1 : entier) retourne entier
debut

	avec diff : entier

	diff <- an1 - an
	si (mois1 < mois ou (jour1 < jour et mois1 = mois))
		alors diff <- diff - 1
	fin si
 
	si diff < 0
		alors diff <- -1
	fin si

	retourne diff
fin diffAn

fonction qualiter(val : entier) retourne chaine
debut
	avec lib : chaine

	si (val < 18) alors
		lib <- "Mineure"
	sinon
		lib <- "Majeur"
		si (val >= 20 et val < 30) alors
			lib <- lib + "vingtenaire"
		sinon
			si (val >= 30 et val < 40) alors
				lib <- lib + "trentenaire"
			sinon
				si (val >= 40 et val val < 50) alors
					lib <- lib + "quadragénaire"
				sinon
					si (val >= 50 et < 60) alors
						lib <- lib + "quinquagénaire"
					sinon
						si (val >= 60 et val < 70) alors
							lib <- lib + "sexagénaire"
							si (val >= 65) alors
								lib <- lib + "retraité"
							fin si
						fin si
					fin si
				fin si
			fin si
		fin si
	fin si

programme principale
debut
	avec jj, mm, aa, jj1, mm1, aa1, difference : entier

	repeter
		SaisirCtrlEntierBorne("Entrer le jour :", 1, 31, "Erreur"; jj)
		SaisirCtrlEntierBorne("Entrer le mois :", 1, 12, "Erreur"; jj)
		SaisirCtrlEntierBorne("Entrer l'annee :", 1583, 9999, "Erreur"; jj)
	tant que VerifierDate(jj,mm,aa) = Faux
	repeter
		SaisirCtrlEntierBorne("Entrer le jour :", 1, 31, "Erreur"; jj)
		SaisirCtrlEntierBorne("Entrer le mois :", 1, 12, "Erreur"; jj)
		SaisirCtrlEntierBorne("Entrer l'annee :", 1583, 9999, "Erreur"; jj)
	tant que VerifierDate(jj1,mm1,aa1) = Faux

	difference <- diffAn(jj,mm,aa,jj1,mm1,aa1)

	si difference = -1
		alors afficher "Erreur différence"
		sinon afficher "Personne:", qualiter(différence)
fin principale
```

# Exercice 2

```
fonction sommeRIterative(n : entier) retourne entier
debut

	avec res : entier

	res <- 0

	tant que n != 1 alors
		res <- res + n
		n <- n + 1
	retourne res
```

>Les deux sont bon mais la recursive est plus rapide mais aussi plus méchante niveau mémoire. Mais elle peut être plus courte voir obligatoire pour certain problème