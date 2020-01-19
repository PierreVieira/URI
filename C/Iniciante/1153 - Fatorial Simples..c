/*
* Autor: Pierre Vieira
* Data de submissão: 16/02/2019 21:12:53
*/
#include <stdio.h>
void fatorial(int n){
    int resultado = 1;
    if (n == 0){
        printf("1\n");
    }
    while(n > 0){
        resultado *= n;
        n--;
    }
    printf("%d\n", resultado);
}
int main(){
    int n;
    scanf("%d", &n);
    fatorial(n);
    return 0;
}