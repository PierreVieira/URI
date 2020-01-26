/*
 * Autor: Pierre Vieira
 * Data de submissão: 26/01/2020 15:01:03
 */

#include <stdio.h>

int main(){
    long long x, y;
    while (scanf("%lld %lld", &x, &y) != EOF){
        printf("%lld\n", x^y);
    }
    return 0;
}