/*
* Autor: Pierre Vieira
* Data de submissão: 14/01/2020 22:05:05
*/
#include <stdio.h>

int qtde_trocas(const int *v, int tam_vetor) {
    int q = 0;
    for (int i = 0; i < tam_vetor; ++i) {
        for (int j = i+1; j < tam_vetor; ++j) {
            if(v[i] > v[j]){
                q++;
            }
        }
    }
    return q;
}

int main() {
    int qtde_casos_teste, tam_vetor, v[50];
    scanf("%d", &qtde_casos_teste);
    for(int i = 0; i < qtde_casos_teste; ++i){
        scanf("%d", &tam_vetor);
        for(int j = 0; j < tam_vetor; j++){
            scanf("%d", &v[j]);
        }
        printf("Optimal train swapping takes %d swaps.\n", qtde_trocas(v, tam_vetor));
    }
    return 0;
}