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
