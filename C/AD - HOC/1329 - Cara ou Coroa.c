/*
 * Autor: Pierre Vieira
 * Data de submissão: 26/01/2020 14:50:48
 */

#include <stdio.h>

int main(){
    int n, numero, qtde_mary, qtde_john;
    while (1){
        qtde_john = qtde_mary = 0;
        scanf("%d", &n);
        if (n == 0){
            break;
        }
        for (int i = 0; i < n; ++i) {
            scanf("%d", &numero);
            if(numero == 0){
                qtde_mary++;
            } else{
                qtde_john++;
            }
        }
        printf("Mary won %d times and John won %d times\n", qtde_mary, qtde_john);
    }
    return 0;
}