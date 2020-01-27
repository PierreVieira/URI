/*
 * Autor: Pierre Vieira
 * Data de submissão: 27/01/2020 14:05:25
 */

#include <stdio.h>
#include <stdlib.h>

void solve_this_problem(const char *entrada){
    char caminho[] = {'N', 'L', 'S', 'O'};
    int cont = 0;
    for (int i = 0; entrada[i] != '\0' ; ++i) {
        if (entrada[i] == 'D'){
            cont++;
            if (cont == 4){
                cont = 0;
            }
        }
        else{
            cont--;
            if (cont == -1){
                cont = 3;
            }
        }
    }
    printf("%c\n", caminho[cont]);
}

int main(){
    int n;
    char *entrada;
    while (1){
        scanf("%d", &n);
        if (n == 0){
            break;
        }
        entrada = malloc(sizeof(char)*n);
        scanf("%s", entrada);
        solve_this_problem(entrada);
        free(entrada);
    }
    return 0;
}