/*
* Autor: Pierre Vieira
* Data de submissão: 13/10/2018 13:03:12
*/
#include <stdio.h>
int verifica_se_tem_letra(char s[]){ //Essa função verifica se a string digitada pelo usuário tem letras
                                    //O programa só continua se tiver letras
    int i, teste;
    for (i = 0, teste = 0; s[i]!= '\0'; i++){
        if((s[i] >= 65 && s[i] <= 90)||(s[i] >= 97 && s[i] <= 122)){
            teste++;
        }
    }
    if(teste != 0){
        return 1;
    }
    else{
        return 0;
    }
}
char*transforma_em_minusculo(char s[]){ //Essa função transforma as letras maiusculas em minusculas
    int i;
    for (i = 0; s[i] != '\0'; i++){
        if(s[i] >= 65 && s[i] <= 90){
            s[i] = s[i] + 32;
        }
    }
    s[i] = '\0';
    return s;
}

char*apena_letras(char s[]){ //Essa função deixa a string digitada pelo usuário apenas com letras
    int i, j;
    char aux[200];
    for (i = 0, j =0; s[i]!= 0; i++){
        if(s[i] >= 97 && s[i] <= 122){
            aux[j] = s[i];
            j++;
        }
    }
    aux[j] = '\0';
    for(i = 0; aux[i] != '\0'; i++){
        s[i] = aux[i];
    }
    s[i] = '\0';
    return s;
}

char*ordem_alfabetica(char s[]){ //Organiza a string do usuário em ordem alfabética
    int i, j;
    char aux;
    for (i = 0; s[i]!= '\0'; i++){
        for(j = 0; s[j] != '\0'; j++){
            if((s[i] < s[j]) && (i != j)){
                aux = s[j];
                s[j] = s[i];
                s[i] = aux;
            }
        }
    }
    return s;
}
int verifica_se_tem_repetido(char s[]){ //Essa função é chamada pela main e verifica se há caracteres repetidos na string
                                        //digitada pelo usuário, se não há então o programa não chama a função letras_que_mais_ocorreram
    int i, cont, j;
    for (i = 0, cont = 0; s[i] != '\0'; i++){
        if(s[i] == s[i+1]){
            cont = 1;
        }
    }
    if(cont == 1){
        return 1;
    }
    return 0;
}

int verifica_se_tem_repetido2(char s[]){ // essa funçao nao é chamada pela main, mas sim pela letras_que_mais_ocorreram
    int i;
    for (i = 0; s[i] != '\0'; i++){
        if(s[i] == s[i+1]){
            return 1;
        }
    }
    return 0;
}

void letras_que_mais_ocorreram(char s[]){//Esse procedimento cria uma nova string apenas para as letras que mais ocorrem e imprime ela para o usuário
    int i, j, cont, repetido;
    char aux[200];
    do{
        cont = 0;
        //printf("Loop\n");
        for (i = 0, j = 0; s[i] != '\0'; i++){
            if(s[i] == s[i+1] && (s[i+1] != '\0')){
                //printf("Entrei no if porque s[%d] (%c) = s[%d] (%c)\n", i, s[i], i+1, s[i+1]);
                aux[j] = s[i];
                j++;
                cont = 1;
            }
        }
        aux[j] = '\0';
        for(i = 0, j = 0; aux[j]!= '\0' ;i++, j++){
            s[i] = aux[j];
            //printf("|%c|",s[i]);
        }
        //printf("\ne cont = %d\n", cont);
        s[j] = '\0';
        repetido = verifica_se_tem_repetido2(s);
        if(repetido == 0){
            cont = 0;
        }
    }while(cont == 1);
    printf("%s\n", s);
}

int main(){
    int N, teste, pega_retorno;
    char string[200];
    scanf("%d", &N);
    getchar();
    do{
        do{
            scanf(" %[^\n]s", string);
            teste = verifica_se_tem_letra(string);
        }while(teste == 0);
        transforma_em_minusculo(string);
        apena_letras(string);
        ordem_alfabetica(string);
        pega_retorno = verifica_se_tem_repetido(string);
        if(pega_retorno == 1){
            letras_que_mais_ocorreram(string);
        }
        else{
            printf("%s\n", string);
        }
        N--;
    }while(N != 0);
}