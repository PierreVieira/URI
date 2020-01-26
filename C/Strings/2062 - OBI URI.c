/*
 * Autor: Pierre Vieira
 * Data de submissão: 26/01/2020 10:55:02
 */

#include <stdio.h>
#include <string.h>

void faz_verificacao(char *palavra){
    int tamanho_palavra;
    tamanho_palavra = strlen(palavra);
    if (tamanho_palavra != 3){
        printf("%s", palavra);
    }
    else if(palavra[0] == 'O' && palavra[1] == 'B' && palavra[2] != 'I'){
        printf("OBI");
    }
    else if(palavra[0] == 'U' && palavra[1] == 'R' && palavra[2] != 'I'){
        printf("URI");
    }
    else{
        printf("%s", palavra);
    }
}

int main(){
    int n;
    char palavra[20];
    scanf("%d", &n);
    while (n > 1){
        scanf("%s", palavra);
        faz_verificacao(palavra);
        printf(" ");
        n--;
    }
    scanf("%s", palavra);
    faz_verificacao(palavra);
    printf("\n");
    return 0;
}