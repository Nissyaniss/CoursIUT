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
