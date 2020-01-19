/*
* Autor: Pierre Vieira
* Data de submissão: 12/10/2018 12:42:21
*/
#include <stdio.h>
int qtde(char n[]){
    int i = 0;
    while (n[i] != '\0'){
        i++;
    }
    return i;
}

int verifica_ultimos_digitos(char A[], char B[], int q1, int q2){
    int i, i2;
    for (i = q1 - q2, i2 = 0; A[i] != '\0'; i++, i2++){
        if (A[i] != B[i2]){
            return 0;
        }
    }
    return 1;
}

int main(){
    int N, q1, q2, verifica;
    char A[1000], B[1000];
    scanf("%d",&N);
    do{
        scanf("%s %s", A, B);
        q1 = qtde(A);
        q2 = qtde(B);
        if(q1 < q2){
            printf("nao encaixa\n");
        }
        else if(verifica_ultimos_digitos(A, B, q1, q2) == 0){
            printf("nao encaixa\n");
        }
        else{
            printf("encaixa\n");
        }
        N--;
    }while(N!= 0);
}
