#include <stdio.h>

void exo1(void) {
	int i;

	i = 0;

	printf("Entrez un entier : ");
	scanf("%d", &i);
	printf("Décimal = %d\n", i);
	printf("Octal = 0o%o\n", i);
	printf("Hexadecimal = 0x%x\n", i);
}

void exo2(void) {
	int i;
	int y;

	i = 0;
	y = 0;
	printf("Entrez deux entiers (format :<i> <y>) : ");
	scanf("%d %d", &i, &y);
	if (i > y) {
		printf("%d\n", i);
	} else{
		printf("%d\n", y);
	}
}

void exo3(void) {
	short tab[10];
	int i;

	i = 0;

	while (i < 10) {
		printf("Entrez un entier : ");
		scanf("%hd", &tab[i]);
		i++;
	}
	i = 0;
	while (i < 10) {
		printf("Valeur %hd a l'adresse %p\n", tab[i], &tab[i]);
		i++;
	}
}

void exo4(void) {
	char str[81] = "ABCDEF";
	char *p;

	p = str;

	*p = 'X';
	p++;
	*p = 'Y';
	*(p + 2) = 'Z';
	printf("%s\n", str);
	printf("%s\n", &str[1]);

	printf("%s\n", p);
	printf("%s\n", p + 1);
	printf("%s\n", p - 1);
	printf("%ld\n", p - str);
}

void exo5part1(void) {
	int i;
	char str[1000];

	fgets(str, 1000, stdin);
	i = 0;

	while (str[i] != '\0')
		i++;
	printf("Len = %d\n", i - 1);
}

void exo5part2(void) {
	char str[1000];
	char *p;
	
	p = str;
	fgets(str, 1000, stdin);
	while (*p++);
	printf("Len = %ld\n", p - str);
}

int main(void) {
	printf("Exo 1\n");
	exo1();
	printf("Exo 2\n");
	exo2();
	printf("Exo 3\n");
	exo3();
	printf("Exo 4\n");
	exo4();
	printf("Exo 5 Partie 1\n");
	exo5part1();
	printf("Exo 5 Partie 2\n");
	exo5part2();
	return 0;
}
