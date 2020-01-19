/*
* Autor: Pierre Vieira
* Data de submissão: 16/02/2019 21:30:56
*/
#include <stdio.h>
int main(){
    int n, c;
    scanf("%d", &n);
    for(c = 1; c <= n/2; c++){
        if (n%c == 0){
            printf("%d\n", c);
        }
    }
    printf("%d\n", n);
}