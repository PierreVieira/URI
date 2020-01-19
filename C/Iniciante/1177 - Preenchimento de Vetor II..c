/*
* Autor: Pierre Vieira
* Data de submissão: 03/10/2018 20:38:33
*/
#include <stdio.h>
#define tam 999
int main(){
    int N[tam], T;
    int i = 0; int x = 0;
    scanf("%d",&T);
    if(T < 2 || T > 50){
        while (T < 2 || T > 50){
            scanf("%d",&T);
        }
    }
        do{
            if(x == T){
                x = 0;
            }
            printf("N[%d] = %d\n", i, x);
            i++, x++;
        }while(i!=1000);
}