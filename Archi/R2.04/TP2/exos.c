#include <string.h>
char	*strcpy_tab(char *dest, char *src)
{
	int	i;

	i = 0;
	while (src[i]) // Tant que src n'a pas atteint le '\0'
	{
		dest[i] = src[i]; ///Fait en sorte que dest est égal a src
		i++;
	}
	dest[i] = '\0'; //Termine la chaine
	return (dest); //Retourne la valeur
}

char	*strcpy_pointer(char *dest, char *src)
{
	char *dest_cpy = dest;

	while (*src) // Tant que src n'a pas atteint le '\0'
		*dest_cpy++ = *src++;//Fait en sorte que dest est égal a src
	*dest_cpy = '\0'; //Termine le chaine
	return (dest); //Retourne la valeur
}

#include <stdio.h>

void	exo2(void)
{
	char str1[100];
	char str2[100];
	char str3[100];

	printf("Entrez str1 :\n");
	fgets(str1, 100, stdin);
	*(str1 + (strlen(str1) - 1)) = '\0';
	printf("\nEntrez str2 :\n");
	fgets(str2, 100, stdin);
	*(str2 + (strlen(str2) - 1)) = '\0';
	strcpy_tab(str3, str1);
	printf("\nCopie de str1 dans str3 :\n\tstr1 = %s\n\tstr3 = %s\n", str1, str3);
	int len = strlen(str3);
	int i = 0;
	while (str2[i])
	{
		str3[len + i] = str2[i];
		i++;
	}
	printf("\nstr2 concaténer a str3 = %s\n", str3);
}

void exo3(void)
{
	char str[100];
	char *str_cpy = str;

	printf("Entrez str :\n");
	fgets(str, 100, stdin);
	*(str + (strlen(str) - 1)) = '\0';
	while (*str_cpy && *str_cpy >= 97 && *str_cpy <= 122)
		*str_cpy++ = *str_cpy - 32;
	printf("\nRésultat = %s\n", str);
}

char exo4part1(char c)
{
	if (c >= 97 && c <= 122)
		return c - 32;
	else
		return c;
}

void exo4part2(char* str)
{
	int i;

	i = 0;

	while (str[i])
	{
		str[i] = exo4part1(str[i]);
		i++;
	}
}

int exo4part3(char* str)
{
	int i;

	i = 0;
	
	while (str[i])
		i++;
	return i;
}

void exo4part4(char *str)
{
	char tmp;
	int len;
	char *strEnd;

	tmp = 0;
	len = exo4part3(str) - 1;
	strEnd = str + len;

	while (str < strEnd)
	{
		tmp = *str;
		*str = *strEnd;
		*strEnd = tmp;
		str++;
		strEnd--;
	}
}

void exo4part5(char *str)
{
	fgets(str, 10000, stdin);
	str[exo4part3(str) - 1] = '\0';
}

void exo4part6(char *str)
{
	printf("%s\n", str);
}

int exo4part7(char *str1, char *str2)
{
	while (*str1 || *str2)
	{
		if (*str1 != *str2)
			return 0;
		str1++;
		str2++;
	}
	if (*str1 != *str2)
		return 0;
	return 1;
}

void exo4part8(void)
{
	char str1[81];
	char str2[81];

	exo4part6("Veuillez saisir str1 :");
	exo4part5(str1);
	exo4part6("Veuillez saisir str2 :");
	exo4part5(str2);
	int len1 = exo4part3(str1);
	printf("Taille de str1 = %d\n", len1);
	exo4part2(str1);
	printf("str1 mis en majuscules = %s\n", str1);
	exo4part2(str2);
	printf("str2 mis en majuscules = %s\n", str2);
	if (exo4part7(str1, str2))
		exo4part6("Les chaines str1 et str2 sont égales");
	else
		exo4part6("Les chaines str1 et str2 ne sont pas égales");
	exo4part4(str2);
	printf("str2 inversé = %s\n", str2);
}

int	main(void)
{
	char src[100] = "Bonjour !\0";
	char dest[100] = "Au revoir !\0";

	printf("Exo 1 Partie 1\t\nString 1 = %s\t\nString 2 = %s", src, strcpy_tab(dest, src));
	memset(dest, 'A', 15);
	dest[15] = '\0';
	printf("\nExo 1 Partie 2\t\nString 1 = %s\t\nString 2 = %s", src, strcpy_pointer(dest, src));
	printf("\nExo 2 :\n");
	exo2();
	printf("\nExo 3 : \n");
	exo3();
	exo4part8();
}
