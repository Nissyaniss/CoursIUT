# Exercice 1

```sql
CREATE TABLE FACTURE(
	idFacture INT PRIMARY KEY NOT NULL,
	dateFacture DATE NOT NULL,
	idClient INT FOREIGN KEY REFERENCES CLIENT(idClient) NOT NULL
);
```

```sql
CREATE TABLE VENTE(
	idFacture INT FOREIGN KEY REFERENCES FACTURE(idFacture) NOT NULL,
	idProduit CHAR(1) FOREIGN KEY REFERENCES PRODUIT(idProduit) NOT NULL,
	quantite INT NOT NULL,

	PRIMARY KEY (idFacture, idProduit)
);
```

# Exercice 2

```sql
R1 = SELECT idClient FROM CLIENT;
R2 = SELECT DISTINCT idProduit FROM VENTE;
R3 = SELECT * FROM CLIENT 
	 WHERE ville = 'Limoges';

R4 = SELECT * FROM CLIENT JOIN FACTURE ON idClient=idClient;
R4bis = SELECT * FROM CLIENT, FACTURE 
		WHERE CLIENT.idClient = FACTURE.idClient;

R5 = SELECT idProduit FROM PRODUIT EXCEPT SELECT idProduit FROM VENTE;
R5bis = SELECT idProduit FROM PRODUIT 
		WHERE NOT EXISTS (
			SELECT * FROM VENTE
			WHERE PRODUIT.idProduit = VENTE.idProduit
		)
	
R5bisBis = SELECT idProduit FROM PRODUIT 
		   WHERE idProduit 
		   NOT IN(
			SELECT idProduit FROM VENTE
		   )

R6 = SELECT idClient FROM R4
R7 = SELECT idClient FROM R1 EXCEPT
	 SELECT idClient FROM R6
R7bis = SELECT idClient FROM R1 
		WHERE NOT EXISTS (
			SELECT idClient FROM R6
			WHERE R1.idClient = R6.idClient
		)
```

# Exercice 3

1)
```sql
SELECT quantite, prix as TOTAL FROM PRODUIT, VENTE, FACTURE
	WHERE VENTE.idFacture = FACTURE.idFacture
	AND VENTE.idProduit = PRODUIT.idProduit
	AND CLIENT.idClient = FACTURE.idFacture
	AND CLIENT.ville = 'Paris'
```

2)
```sql
SELECT SUM(quantite * prix) as TOTAL FROM PRODUIT, VENTE, FACTURE
	WHERE VENTE.idFacture = FACTURE.idFacture
	AND VENTE.idProduit = PRODUIT.idProduit
	AND CLIENT.idClient = FACTURE.idFacture
	AND CLIENT.ville = 'Paris'
```

3)
```sql
SELECT ville, SUM(quantite * prix) AS TOTAL FROM CLIENT, PRODUIT, FACTURE, VENTE
	WHERE CLIENT.idClient = FACTURE.idClient
	AND FACTURE.idFacture = VENTE.idFacture
	AND VENTE.idProduit = PRODUIT.idProduit
GROUP BY ville
```

4)
```sql
SELECT designation, SUM(quantite) AS TOTAL FROM CLIENT, PRODUIT, FACTURE, VENTE
	WHERE CLIENT.idClient = FACTURE.idClient
	AND FACTURE.idFacture = VENTE.idFacture
	AND VENTE.idProduit = PRODUIT.idProduit
	AND dateFacture >='01/01/2020'
	AND dateFacture < '01/01/2021'
GROUP BY designation
```

5)
```sql
SELECT designation, SUM(quantite * prix) AS TOTAL FROM CLIENT, PRODUIT, FACTURE, VENTE
	WHERE CLIENT.idClient = FACTURE.idClient
	AND FACTURE.idFacture = VENTE.idFacture
	AND VENTE.idProduit = PRODUIT.idProduit
	AND dateFacture >='01/01/2020'
	AND dateFacture < '01/01/2021'
ORDER BY TOTAL DESC, designation ASC
GROUP BY designation
```
