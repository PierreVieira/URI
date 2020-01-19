/*
* Autor: Pierre Vieira
* Data de submissão: 11/10/2018 19:33:15
*/
#include <stdio.h>
int main(){
    int i, N, A, soma;
    scanf("%d %d", &A, &N);
    if(N<= 0){
        do{
            scanf("%d", &N);
        }while(N<=0);
    }
    for(i = 0, soma =0; i<=N-1; i++){
        soma+=(A + i);
    }
    printf("%d\n", soma);
}