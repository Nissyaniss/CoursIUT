// Exo 1
#include <stdio.h>


int exo1(void){
	int n;
	n = 10;
	printf("L'entier n vaut: %d\n", n);
	return 0;
}

// Exo 2

int exo2(void){
	char chaine[] = "Bonjour à tous\n";
	int i;
	for (i = 0; i < 5; i++){
		printf("%s", chaine);
	}
	return 0;
}

// Exo 3

int exo3(void){
	int *p;
	int n;

	n = 10;
	p = &n;

	printf("L'entier n vaut : %d, il est stocké a l'adresse: %x\n", *p, p);
	printf("L'adresse de p est %x\n'", &p);
	return 0;
}

// Exo 4

void permut(int *a, int *b){
	int c;
	c = *a;
	*a = *b;
	*b = c;
}

int exo4(void){
	int n1 = 5;
	int n2 = 8;

	printf("Avant permutation: n1 = %d, n2 = %d\n", n1, n2);
	permut(&n1, &n2);

	printf("Après permutation: n1 = %d, n2 = %d\n", n1, n2);
	return 0;
}

// Exo 5

#include <stdlib.h>

int nbelnts = 10;

void mafct(void) {
	static int c = 0;
	int a = 0;
	a++;
	c++;
	printf("a = %d, c = %d\n", a, c);
}

int exo5(void){
	int *tab;
	int i;

	printf("Adresse de i = %x\n", &i);
	for (i = 0; i < 5; i++)
		mafct();
	/***********Allocation dynamique***********/
	printf("Adresse de nbelnts = %x", &nbelnts);
	tab = malloc(nbelnts * sizeof(int));
	*tab = 5;
	*(tab + 1) = 8;

	printf("1er elent tab = %d 2eme elent tab = %d \n", *tab, *(tab + 1));
	printf("adresse elent tab = %x adresse elent tab = %x \n", tab, tab + 1);
	free(tab);
	return 0;
}

int main(void)
{
	printf("Ex1\n");
	exo1();
	printf("\nExo2\n");
	exo2();
	printf("\nExo3\n");
	exo3();
	printf("\nExo4\n");
	exo4();
	printf("\nExo5\n");
	exo5();
	return 0;
}
