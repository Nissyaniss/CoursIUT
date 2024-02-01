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
