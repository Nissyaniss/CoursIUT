#include <stdio.h>
#include <stdlib.h>

void exo1(void)
{
	char *couleur[] = { "rouge", "vert", "bleu", "blanc", "noir", "orange", NULL };
	char **c = couleur;

	while (*c != NULL)
	{
		printf("%s\n", *c);
		c++;
	}
	
	printf("\n");
	c = couleur;
	while (*c != NULL)
	{
		printf("%s\n", *c + 1);
		c++;
	}

	printf("\n");
	c = couleur;
	char *ntm = *c;
	while (*c != NULL)
	{
		ntm = *c;
		while (*ntm != '\0')
			printf("%c", *ntm++ - 32);
		printf("\n");
		c++;
	}

	printf("\n");
	c = couleur;
	ntm = *c;
	while (*c != NULL)
	{
		ntm = *c;
		while (*ntm != '\0')
			printf("%c", *ntm++);
		printf("\n");
		c++;
	}
}

int tabLen(char **str)
{
	int i;

	i = 0;
	
	while (str[i])
		i++;
	return i;
}

void reverseTab(char **str)
{
	char *tmp;
	int len;
	char **strEnd;

	tmp = 0;
	len = tabLen(str) - 1;
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

void exo2(void)
{
	char *p[6] = {"ABC", "DEFGH", "IJKLM", "NOPQRS", "TUV", NULL};

	reverseTab(p);

	for (int i = 0; p[i] != NULL; i++)
	{
		printf("%s\n", p[i]);
	}
}

void exo3(void)
{
	char *jour[8] = { "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche", NULL };

	char **j = jour;
	while (*j != NULL)
		printf("%s\n",*j++);

	
	printf("\n");
	j = jour;
	char *jo = *j;
	while (*j != NULL)
	{
		jo = *j;
		while (*jo != '\0')
			printf("%c", *jo++);
		printf("\n");
		j++;
	}

	printf("\n");
	j = jour + 6;
	while (j + 1 != jour)
		printf("%s\n", *j--);

	reverseTab(jour);

	printf("\n");
	j = jour;
	jo = *j;
	while (*j != NULL)
	{
		jo = *j;
		while (*jo != '\0')
			printf("%c", *jo++ - 32);
		printf("\n");
		j++;
	}
}

void exo4(int argc, char *argv[])
{
	char **a = argv + argc - 1;

	printf("nb arguments : %d\n", argc);
	while (a - 1 != argv)
		printf("%s ", *a--);
	printf("%s\n", *a);
}

int ft_strcmp(char *str1, char *str2)
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

void exo5(int argc, char *argv[])
{
	int rescmp;

	rescmp = 0;
	if (argc != 3)
	{
		printf("Pas assez d'arguments");
		exit(1);
	}
	rescmp = ft_strcmp(*(argv + 1), *(argv + 2));
	if (rescmp == 1)
		printf("Il n'y a pas de différence entre les deux arguments\n");
	else
		printf("Il y a une différence entre les deux arguments\n");
}

char ft_to_upper(char c)
{
	if (c >= 97 && c <= 122)
		return c - 32;
	else
		return c;
}

void string_to_upper(char* str)
{
	int i;

	i = 0;

	while (str[i])
	{
		str[i] = ft_to_upper(str[i]);
		i++;
	}
}

void exo6(int argc, char *argv[])
{
	char **a = argv;
	char **ar = a;
	int isToBeReversed;

	isToBeReversed = 0;
	while (*a != NULL)
	{
		if ((*a)[0] == '-')
		{
			if ((*a)[1] == '\0' || (*a)[2] != '\0')
			{
				printf("Invalid Option : %s\n", *a);
				exit(1);
			}
			else
			{
				switch ((*a)[1])
				{
					case 'r':
						isToBeReversed = 1;
						break;
					case 'M':
						ar = argv + 1;
						while (*ar != NULL)
						{
							if (*ar[0] != '-')
								string_to_upper(*ar);
							ar++;
						}
						break;
					case 'm':
						ar = argv + 1;
						while (*ar != NULL)
						{
							(*ar)[0] = ft_to_upper((*ar)[0]);
							ar++;
						}
						break;
					default:
						printf("Invalid Option : %s\n", *a);
						exit(1);
				}
			}
		}
		a++;
	}
	a = argv + 1;
	if (isToBeReversed)
		reverseTab(a);
	while (*a != NULL)
	{
		if (*a[0] != '-')
			printf("%s\n", *a);
		a++;
	}
}

int main(int argc, char *argv[])
{
	//exo1();
	//exo2();
	//exo3();
	//exo4(argc, argv);
	//exo5(argc, argv);
	//exo6(argc, argv);
}
