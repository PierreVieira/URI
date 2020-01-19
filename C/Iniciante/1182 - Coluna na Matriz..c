/*
* Autor: Pierre Vieira
* Data de submissão: 04/10/2018 09:36:32
*/
#include<stdio.h>
#define linha 12
#define coluna 12
int main(){
    int num, i, j;
    float soma = 0;
    float media, matriz[linha][coluna];
    char resp;
    do{
        scanf("%d", &num);
    }while(num < 0 || num > 11);
    do{
        scanf(" %c", &resp);
    }while(resp != 'S' && resp != 'M');
    for(i = 0; i<linha; i++){
        for(j = 0; j<coluna; j++){
            scanf("%f",&matriz[i][j]);
        }
    }
    //Algoritmo para a soma
    for(i = 0; i< linha; i++){
           soma += matriz[i][num];
    }
    if(resp == 'S'){
        printf("%.1f\n", soma);
    }
    else{
        media = soma/12;
        printf("%.1f\n", media);
