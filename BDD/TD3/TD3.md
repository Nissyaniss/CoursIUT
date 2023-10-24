# Exercice 1

>CLIENT(<u>idClient</u>, nom, ville)<br>
PRODUIT(<u>idProduit</u>, désignation, prix)<br>
FACTURE(<u>idFacture</u>, dateFacture, #<u>idClient</u>)<br>
VENTE(#<u>idClient</u>, #<u>idProduit</u>, quantité)

>Chaque client peut faire un achat d'une certaine quantité d'un produit et ensuite reçois une facture. La facture a besoin de l'idClient car sinon la facture ne serait pas adressé au client. Et la vente a besoin de l'idClient et de l'idProduit car sinon elle ne ferait pas payer le client et le client ne recevrais pas le produit demandé

# Exercice 2

## R1

>R1 = πCLIENT(idClient)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;R1

| idClient |
|:--------:|
|    1     |
|    2     |
|    3     |

## R2

>R2 = πVENTE(idProduit)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;R2

| idProduit |
|:---------:|
|     B     |
|     A     |
|     F     |
|     C     |
|     D     |

## R3

>R3 = σClient(ville="Limoges")

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;R3

| idClient | nom  | ville   |
|:--------:|:-----|:--------|
|    1     | Mike | Limoges |
|    3     | Bill | Limoges |

## R4

>R4 = CLIENT x FACTURE(CLIENT.idClient = FACTURE.idClient)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;R4

| idClient | nom  | ville   | idFacture | dateFacture | idClient |
|:--------:|:-----|:--------|:---------:|:-----------:|:--------:|
|    2     | Joe  | Paris   |    10     | 17/12/2020  |    2     |
|    2     | Joe  | Paris   |    30     | 05/11/2020  |    2     |
|    3     | Bill | Limoges |    20     | 07/11/2021  |    3     |

## R5

>R5 = πPRODUIT(idProduit)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;R5

| idProduit |
|:---------:|
|     B     |
|     A     |
|     F     |
|     C     |
|     D     |
|     E     |

## R6

>R6 = R5 - R2

| idProduit |
|:---------:|
|     E     |

## R7

>R7 = πR4(idClient)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;R7

| idClient |
|:--------:|
|    2     |
|    3     |

## R8

>R8 = R1 - R7

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;R8

| idClient |
|:--------:|
|    1     |

# Exercice 3

>R1 = <br>
((CLIENTx FACTURE(CLIENT.idClient = FACTURE.idClient)) x (VENTE x PRODUIT(VENTE.idProduit = PRODUIT.idProduit))) x ((CLIENT x FACTURE) x (VENTE x Produit)((CLIENT x FACTURE).idFacture = (VENTE x Produit).idFacture))
>1) R2 = πR1(dateFacture, idClient ,idProduit, ville, désignation)<br>
R3 = σR2(ville = Paris)
<br><br>
>2) R4 = πR1(idProduit, idFacture, idClient, nom, ville, prix)<br>R5 = σR3(dateFacture < 01/01/2021, désignation = Marteau)

## Correction

> 1) R9 = σClient(Ville = 'Paris')<br>R10 = R9 x FACTURE(R9.idClient = FACTURE.idClient)<br>R11 = R10 x VENTE(R10.idFacture = VENTE.idFacture)<br>R12 = R11 x PRODUIT(R11.idProduit = PRODUIT.idProduit)<br>R13 = πR12(quantité, prix)
>
>2) R15 = σProduit(désignation = 'Marteau')\
>R16 = πR15(idProduit)\
>R16 donne l'identifiant du marteau\
\
>R17 = σFACTURE(dateFacture < '01/01/2021')\
>R18 = πR17(idFacture)\
>R18 donne la liste des factures datant d'avant 2021\
\
>R19 = VENTE x R16(VENTE/idProduit = R16.idProduit)\
>R20 = R19 x R18(R19.idFacture = R18.idFacture)\
>R21 = πR20(idFacture, quantité)

| idFacture | quantité |
|:---------:|:--------:|
|    10     |    2     |
|    30     |    3     |