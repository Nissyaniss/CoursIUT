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
