/*
* Autor: Pierre Vieira
* Data de submissão: 11/02/2019 12:33:24
*/
#include <stdio.h>
int primo(int x){
    int c, div;
    for (c = 2, div = 0; c <= x/2; c++){
        if (x%c == 0){
            div++;
        }
    }
    if (div == 0){
        return 1;
    }
    return 0;
}

int main(){
    int n, x;
    scanf("%d", &n);
    do{
        scanf("%d", &x);
        if(primo(x) == 1){
            printf("%d eh primo\n", x);
        }
        else{
            printf("%d nao eh primo\n", x);
        }
        n--;
    }while(n > 0);
}