/*
* Autor: Pierre Vieira
* Data de submissão: 11/02/2019 00:14:07
*/
#include<stdio.h>
int main(){
    int n, p1, p2, x;
    int termo = 1;
    scanf("%d",&n);
    for (x = 0; x < n; x++){
        p1 = termo*termo;
        p2 = termo*termo*termo;
        printf("%d %d %d\n", termo, p1, p2);
        printf("%d %d %d\n", termo, p1+1, p2+1);
        termo++;
    }
}