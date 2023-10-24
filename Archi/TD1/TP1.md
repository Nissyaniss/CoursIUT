# Exercice 1

## Code

<!-- markdownlint-disable MD010 -->
<!-- markdownlint-disable MD024 -->
<!-- markdownlint-disable MD025 -->
<!-- markdownlint-disable MD040 -->

```c
#include <stdio.h>

int main(void)
{
	char car;

	printf("Entrer un caractère : ");
	scanf("%c", &car);

	printf("Affichage mode caractère: %c\n", car);
	printf("Affichage caractère en décimal: %d\n", car);
	printf("Affichage caractère en octal: %o\n", car);
	printf("Affichage caractère en Hexa: %x\n", car);

	printf("Affichage car+2 en mode caractère pui décimal: %c, %d\n", car+2, car+2);
	printf("Affichage car+10 en mode caractère pui décimal: %c, %d\n", car+10, car+10);
	return 0;
}
```

## Résultats

```
Entrer un caractère : A
Affichage mode caractère: A
Affichage caractère en décimal: 65
Affichage caractère en octal: 101
Affichage caractère en Hexa: 41
Affichage car+2 en mode caractère pui décimal: C, 67
Affichage car+10 en mode caractère pui décimal: K, 75
```

```
Entrer un caractère : 9
Affichage mode caractère: 9
Affichage caractère en décimal: 57
Affichage caractère en octal: 71
Affichage caractère en Hexa: 39
Affichage car+2 en mode caractère pui décimal: ;, 59
Affichage car+10 en mode caractère pui décimal: C, 6
```

>On peut remarquer que le code décimal de 9 n'est pas 9 et que le code Hexa de A n'est pas A

# Exercice 2

## Code

```c
#include <stdio.h>

int main(void)
{
	unsigned short int n;

	printf("Entrer un entier : ");
	scanf("%hu", &n);

	printf("Affichage entier en décimal et Hexa : %hu, %hx\n", n, n);
	printf("Affichage n+1000 en décimal et Hexa : %hu, %hx\n", n+1000, n+1000);
	return 0;
}
```

## Résultats

```
Entrer un entier : 50
Affichage entier en décimal et Hexa : 50, 32
Affichage n+1000 en décimal et Hexa : 1050, 4
```

```
Entrer un entier : -10
Affichage entier en décimal et Hexa : 65526, fff6
Affichage n+1000 en décimal et Hexa : 990, 3de
```

```
Entrer un entier : 65000
Affichage entier en décimal et Hexa : 65000, fde8
Affichage n+1000 en décimal et Hexa : 464, 1d0
```

>On peut voir que `-10` donne en décimal `65526` ce qui signifie que on prend le max de `unsigned short` et on lui retire `10`.

# Exercice 3

## Code

```c
#include <stdio.h>

int main(void)
{
	short int n;

	printf("Entrer un entier : ");
	scanf("%hd", &n);

	printf("Affichage entier en décimal et Hexa : %hd, %hx\n", n, n);
	printf("Affichage n + 1000 en décimal et Hexa : %hd, %hx\n", n + 1000, n + 1000);
	printf("Affichage n - 1000 en décimal et Hexa : %hd, %hx\n", n - 1000, n - 1000);
	return 0;
}
```

## Résultats

```
Entrer un entier : 50
Affichage entier en décimal et Hexa : 50, 32
Affichage n + 1000 en décimal et Hexa : 1050, 41a
Affichage n - 1000 en décimal et Hexa : -950, fc4a
```

```
Entrer un entier : -10
Affichage entier en décimal et Hexa : -10, fff6
Affichage n + 1000 en décimal et Hexa : 990, 3de
Affichage n - 1000 en décimal et Hexa : -1010, fc0e
```

```
Entrer un entier : 32000
Affichage entier en décimal et Hexa : 32000, 7d00
Affichage n + 1000 en décimal et Hexa : -32536, 80e8
Affichage n - 1000 en décimal et Hexa : 31000, 7918
```

>On peut remarquer la même erreur que l'exercise précédent avec `32000 + 1000` qui donne `-23536`

# Exercice 4

## Code

```c
#include <stdio.h>

int main(void)
{
	short int n;
	short int n1;

	printf("Entrer le nombre n : ");
	scanf("%hd", &n);
	printf("Entrer le nombre n1 : ");
	scanf("%hd", &n1);

	printf("Affichage entier n en décimal et Hexa : %hd, %hx\n", n, n);
	printf("Affichage entier n1 en décimal et Hexa : %hd, %hx\n", n1, n1);
	printf("Affichage n + n1 en décimal et Hexa : %hd, %hx\n", n + n1, n + n1);
	printf("Affichage n - n1 en décimal et Hexa : %hd, %hx\n", n - n1, n - n1);
	return 0;
}
```

## Résultats

```
Entrer le nombre n : 50
Entrer le nombre n1 : -10
Affichage entier n en décimal et Hexa : 50, 32
Affichage entier n1 en décimal et Hexa : -10, fff6
Affichage n + n1 en décimal et Hexa : 40, 28
Affichage n - n1 en décimal et Hexa : 60, 3c
```

```
Entrer le nombre n : 32000
Entrer le nombre n1 : 2000
Affichage entier n en décimal et Hexa : 32000, 7d00
Affichage entier n1 en décimal et Hexa : 2000, 7d0
Affichage n + n1 en décimal et Hexa : -31536, 84d0
Affichage n - n1 en décimal et Hexa : 30000, 7530
```

```
Entrer le nombre n : 25000
Entrer le nombre n1 : 8000
Affichage entier n en décimal et Hexa : 25000, 61a8
Affichage entier n1 en décimal et Hexa : 8000, 1f40
Affichage n + n1 en décimal et Hexa : -32536, 80e8
Affichage n - n1 en décimal et Hexa : 17000, 4268
```

```
Entrer le nombre n : 25000
Entrer le nombre n1 : -12000
Affichage entier n en décimal et Hexa : 25000, 61a8
Affichage entier n1 en décimal et Hexa : -12000, d120
Affichage n + n1 en décimal et Hexa : 13000, 32c8
Affichage n - n1 en décimal et Hexa : -28536, 9088
```

>On remarque les même problèmes que dans les exercices précédent

# Exercice 5

## Code

```c
#include <stdio.h>

int main(void)
{
	float n;
	float n1;

	printf("Entrer le réel n : ");
	scanf("%f", &n);
	printf("Entrer le réel n1 : ");
	scanf("%f", &n1);

	printf("Affichage n en décimal: %e\n", n);
	printf("Affichage n1 en décimal: %e\n", n1);

	printf("Affichage n + n1 en décimal: %e\n", n + n1);
	return 0;
}
```

## Résultats

```
Entrer le réel n : 50
Entrer le réel n1 : 1e40
Affichage n en décimal: 5.000000e+01
Affichage n1 en décimal: inf
Affichage n + n1 en décimal: inf
```

```
Entrer le réel n : 32000
Entrer le réel n1 : 4e-48
Affichage n en décimal: 3.200000e+04
Affichage n1 en décimal: 0.000000e+00
Affichage n + n1 en décimal: 3.200000e+04
```

```
Entrer le réel n : 3e28
Entrer le réel n1 : 2e38 
Affichage n en décimal: 3.000000e+28
Affichage n1 en décimal: 2.000000e+38
Affichage n + n1 en décimal: 2.000000e+38
```

>On peut remarquer que si il y a un Overflow le programme renvoie `inf`
