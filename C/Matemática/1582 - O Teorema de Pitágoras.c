/*
 * Autor: Pierre Vieira
 * Data de submissão: 16/02/2020 20:31:41
 */
#include <stdio.h>
#include <math.h>
int forma_triangulo(a, b, c){
    if ((a < b + c) && (b < a + c) && (c < a + b)){
        return 1; //true
    }
    return 0; //false
}

int mdc(int a, int b){
    int resto_divisao;
    while (b > 0){
        resto_divisao = a % b;
        a = b;
        b = resto_divisao;
    }
    return a;
}

int main(){
    int a, b, c, aux;
    while (scanf("%d %d %d", &a, &b, &c) != EOF){
        if (c > b){
            aux = c;
            c = b;
            b = aux;
        }
        if (b > a){
            aux = b;
            b = a;
            a = aux;
        }
        if (!forma_triangulo(a, b, c)){
            printf("tripla\n");
        }
        else if(a == sqrt(c*c + b*b)){
            if(mdc(a, b) == 1 && mdc(a, c) == 1 && mdc(b, c) == 1){
                printf("tripla pitagorica primitiva\n");
            }
            else{
                printf("tripla pitagorica\n");
            }
        }
        else{
            printf("tripla\n");
        }
    }
    return 0;
}