/*
* Autor: Pierre Vieira
* Data de submissão: 22/08/2018 21:04:11
*/
#include <stdio.h>
int main(){
	int valor;
	int n100, n50, n20, n10, n5, n2, n1, resto;
	scanf("%d", &valor);
	resto = valor;
	n100 = resto/100;
	resto = resto - (n100*100);
	n50 = resto/50;
	resto = resto - (n50*50);
	n20 = resto/20;
	resto = resto - (n20*20);
	n10 = resto/10;
	resto = resto - (n10*10);
	n5 = resto/5;
	resto = resto - (n5*5);
	n2 = resto/2;
	resto = resto - (n2*2);
	n1 = resto/1;
	printf ("%d\n%d nota(s) de R$ 100,00\n%d nota(s) de R$ 50,00\n%d nota(s) de R$ 20,00\n", valor, n100, n50, n20);
	printf("%d nota(s) de R$ 10,00\n%d nota(s) de R$ 5,00\n%d nota(s) de R$ 2,00\n%d nota(s) de R$ 1,00\n", n10, n5, n2, n1);
}