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
