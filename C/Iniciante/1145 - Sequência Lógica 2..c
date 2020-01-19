/*
* Autor: Pierre Vieira
* Data de submissão: 11/02/2019 00:25:19
*/
#include<stdio.h>
int main(){
    int x, y, c, c2;
    scanf("%d", &x);
    scanf("%d", &y);
    c2 = x-1;
    for (c = 1; c <= y; c++){
        if(c2 == 0){
            printf("%d\n",c);
            c2 = x;
        }
        else{
            printf("%d ",c);
        }
        c2--;
    }
}