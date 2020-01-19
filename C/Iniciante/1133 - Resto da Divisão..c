/*
* Autor: Pierre Vieira
* Data de submissão: 10/02/2019 23:20:40
*/
#include<stdio.h>
void main(){
    int x, y;
    scanf("%d", &x);
    scanf("%d", &y);
    if (x > y){
        int aux;
        aux = x;
        x = y;
        y = aux;
    }
    for (x = x+1; x < y; x++){
        if(x%5 == 2 || x%5 == 3){
            printf("%d\n",x);
        }
    }
}