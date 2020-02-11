/*
 * Autor: Pierre Vieira
 * Data de submissão: 11/02/2020 16:35:47
 */
#include <stdio.h>

void trocar(int *v, int p1, int p2){
    int aux;
    aux = v[p1];
    v[p1] = v[p2];
    v[p2] = aux;
}

int encontrar_copo_inicial(const int *copos, int copo_inicial){
    for (int i = 0; i < 3; ++i) {
        if (copos[i] == copo_inicial){
            return i;
        }
    }
    return -1; //Não achou nada
}

int main(){
    int copos[] = {65, 66, 67}, n, troca, pos_finded;
    char copo_inicial;
    scanf("%d", &n);
    scanf(" %c", &copo_inicial);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &troca);
        switch (troca){
            case 1:
                trocar(copos, 0, 1);
                break;
            case 2:
                trocar(copos, 1, 2);
                break;
            default:
                trocar(copos, 0, 2);
        }
    }
    pos_finded = encontrar_copo_inicial(copos, copo_inicial);
    if (pos_finded == 0){
        printf("A\n");
    } else if (pos_finded == 1){
        printf("B\n");
    } else{
        printf("C\n");
    }
    return 0;
}