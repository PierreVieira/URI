/*
  Autor: Pierre Vieira
  Data: 28/03/2019 22:57:02
*/
#include <stdio.h>
#include <math.h>

int qtde_algarismos(int soma){
    int cont = 0;
    while(soma > 0){
        cont++;
        soma /= 10;
    }
    return cont;
}

void no_zero(int soma, int qtde_alg){
    int divisor, num, subtrador, aux, qtde_alg2;
    aux = qtde_alg;
    while(1){
        aux--;
        if(aux == 0){
            if(subtrador != 0){
                printf("%d", subtrador);
            }
            break;
        }
        divisor = pow(10, aux);
        subtrador = soma%((int) divisor);
        num = soma - subtrador;
        num /= divisor;
        if(num != 0){
            printf("%d", num);
        }
        soma %= divisor;
    }
    printf("\n");
}

int main(){
    int qtde_alg, soma, n1, n2;
    while(1){
        scanf("%d %d", &n1, &n2);
        if(n1 == 0 && n2 == 0){
            return 0;
        }
        soma = n1 + n2;
        qtde_alg = qtde_algarismos(soma);
        no_zero(soma, qtde_alg);
    }
}
