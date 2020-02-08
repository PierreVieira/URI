/*
 * Autor: Pierre Vieira
 * Data de submissão: 05/02/2020 20:16:34
 */
# include <stdio.h>
int main(){
    int e, d, dif;
    scanf("%d %d", &e, &d);
    dif = d - e;
    if (dif < 0){
        printf("Eu odeio a professora!\n");
    } else if (dif >= 3){
        printf("Muito bem! Apresenta antes do Natal!\n");
    }
    else{
        printf("Parece o trabalho do meu filho!\n");
        e += 2;
        if (e > 23){
            printf("Fail! Entao eh nataaaaal!\n");
        }
        else{
            printf("TCC Apresentado!\n");
        }
    }
}