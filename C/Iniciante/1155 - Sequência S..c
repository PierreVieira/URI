/*
* Autor: Pierre Vieira
* Data de submissão: 16/02/2019 21:24:09
*/
#include <stdio.h>
int main(){
    float soma = 0;
    float den = 1;
    while (den <= 100){
        soma += (1/den);
        den++;
    }
    printf("%.2f\n", soma);
}