/*
* Autor: Pierre Vieira
* Data de submissão: 23/09/2018 15:21:39
*/
#include <stdio.h>
#define tamanho 10
int main(){
    int v[tamanho], x, numero;
    scanf("%d", &numero);
    for(x = 0; x <= tamanho; x++){
        if(x == 0){
            v[x] = numero;
        }
        else{
            v[x] = 2*v[x-1];
        }
    }
    for(x = 0; x <= tamanho-1; x++){
        printf("N[%d] = %d\n", x, v[x]);
    }
}