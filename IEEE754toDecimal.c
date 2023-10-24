#include <stdio.h>
#include <string.h>
#include <math.h>

int main(int argc, char **argv)
{
	int    sign;
	int    binary_e[8] = {0, 0, 0, 0, 0, 0, 0};
	int    binary_m[23] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	int    i;
	float  mantisse;
	int    exposant;
	double result;

	i        = 0;
	sign     = 0;
	mantisse = 0;
	exposant = 0;
	if (argc < 2 || argc > 3)
	{
		printf("Argument Error !");
		return (0);
	}
	if (strlen(argv[1]) != 32)
	{
		printf("Argument not 32 bits long !");
		return (0);
	}
	while (argv[1][i])
	{
		if (argv[1][i] != '0' && argv[1][i] != '1')
		{
			printf("Number at positon %d is [%c] not 1 nor 0.\n", i + 1, argv[1][i]);
			return (0);
		}
		if (i == 0)
			sign = argv[1][i] - 48;
		else if (i > 0 && i < 8)
			binary_e[i - 1] = argv[1][i] - 48;
		else if (i > 8 && i < 31)
			binary_m[i - 8] = argv[1][i] - 48;
		i++;
	}
	i = 0;
	while (++i < 23)
		mantisse += binary_m[i] * pow(2, -i);
	i = -1;
	while (++i < 8)
		exposant += binary_e[i] * pow(2, 7 - i);

	printf("exposant = %d\n", exposant);
	printf("mantisse = %f\n", mantisse);
	if (exposant == 0 && mantisse != 0)
		result = pow(-1, sign) * mantisse * pow(2, -126);
	else 
		result = pow(-1, sign) * (mantisse + 1) * pow(2, exposant - 127);
	printf("result = %.20f\n", result);
	return (0);
}
