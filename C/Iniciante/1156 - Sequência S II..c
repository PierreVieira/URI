/*
* Autor: Pierre Vieira
* Data de submissão: 16/02/2019 21:27:40
*/
#include <stdio.h>
int main(){
    float soma = 0, num = 1;
    float den = 1;
    while (num <= 39){
        soma += (num/den);
        den = den*2;
        num += 2;
    }
    printf("%.2f\n", soma);
}