/*
* Autor: Pierre Vieira
* Data de submissão: 19/01/2020 18:17:31
*/
#include<stdio.h>

int duplo_n(int n) {
    // Eq de recorrência
    // D(0) = 1
    // D(n) = D(n - 1) + (n + 1)
    return (n * n + 3 * n) / 2 + 1;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", (int) duplo_n(n));
    return 0;
}

