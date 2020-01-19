/*
* Autor: Pierre Vieira
* Data de submissão: 10/02/2019 23:47:04
*/
#include<stdio.h>
int main(){
    int alcool, gasolina, diesel, opcao;
    alcool = gasolina =  diesel = opcao = 0;
    do{
        do{
            scanf("%d", &opcao);
        }while((opcao < 1) || (opcao > 4));
        if (opcao == 4){
            printf("MUITO OBRIGADO\n");
            printf("Alcool: %d\n",alcool);
            printf("Gasolina: %d\n",gasolina);
            printf("Diesel: %d\n",diesel);
        }
        else{
            if (opcao == 1){
                alcool++;
            }
            else if(opcao == 2){
                gasolina++;
            }
            else{
                diesel++;
            }
        }
    }while(opcao != 4);
}
