/*
* Autor: Pierre Vieira
* Data de submissão: 30/08/2018 16:26:37
*/
#include <stdio.h>
#include <math.h>
int main(){
    float A, B, C, delta, R1, R2;
    scanf("%f %f %f", &A, &B, &C);
    delta = (B*B) -4*A*C;
    R1 = (-B + pow(delta, 0.5))/(2*A);
    R2 = (-B - pow(delta, 0.5))/(2*A);
    if(delta < 0 || A == 0){
        printf("Impossivel calcular\n");
    }
    else{
        printf("R1 = %.5f\nR2 = %.5f\n", R1, R2);
    }
}