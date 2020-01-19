/*
* Autor: Pierre Vieira
* Data de submissão: 23/09/2018 15:44:23
*/
#include <stdio.h>
int main(){
   int x[10], y, valor_digitado;
   for(y = 0; y<=9; y++){
        scanf("%d", &valor_digitado);
        x[y] = valor_digitado;
        if(x[y] <= 0){
            x[y] = 1;
        }
   }
   for (y = 0; y<=9; y++){
        printf("X[%d] = %d\n", y, x[y]);
   }
}