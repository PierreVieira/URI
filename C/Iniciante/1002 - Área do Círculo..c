/*
* Autor: Pierre Vieira
* Data de submissão: 13/09/2018 22:10:52
*/
#include <stdio.h>
#include <math.h>
int main()
{
    double area, raio;
    scanf("%lf",&raio);
    area=3.14159*pow(raio,2);
    printf("A=%.4lf\n",area);
}