/*
* Autor: Pierre Vieira
* Data de submissão: 16/02/2019 21:08:21
*/
#include <stdio.h>
int main(){
    int x, z, cont = 1, soma;
    scanf("%d", &x);
    scanf("%d", &z);
    while (x >= z){
        scanf("%d", &z);
    }
    soma = x;
    while(soma < z){
        cont++;
        soma += x;
        x++;
    }
    printf("%d\n",cont);
    return 0;
}
