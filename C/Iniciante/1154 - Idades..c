/*
* Autor: Pierre Vieira
* Data de submissão: 16/02/2019 21:18:24
*/
#include<stdio.h>
int main(){
    int soma = 0, n = 0;
    float cont = 0;
    while (n>=0){
        scanf("%d", &n);
        if (n >= 0){
            soma += n;
            cont ++;
        }
    }
    printf("%.2f\n", soma/(cont));
}