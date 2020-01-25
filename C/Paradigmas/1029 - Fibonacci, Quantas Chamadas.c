/*
 * Autor: Pierre Vieira
 * Data de submissão: 25/01/2020 17:20:59
 */
#include <stdio.h>

int calcula_qtde_chamadas(int n){
    if (n == 1){
        return 0;
    } else if (n == 2){
        return 2;
    }
    return calcula_qtde_chamadas(n - 1) + calcula_qtde_chamadas(n - 2) + 2;
}


int fib(int n){
    if (n == 0){
        return 0;
    } else if (n == 1){
        return 1;
    }
    return fib(n - 1) + fib(n - 2);
}


int main() {
    int qtde_casos_teste, n;
    scanf("%d", &qtde_casos_teste);
    for (int i = 0; i < qtde_casos_teste; ++i) {
        scanf("%d", &n);
        printf("fib(%d) = %d calls = %d\n", n, calcula_qtde_chamadas(n),  fib(n));
    }
    return 0;
}