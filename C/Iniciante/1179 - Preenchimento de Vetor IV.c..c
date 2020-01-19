/*
* Autor: Pierre Vieira
* Data de submissão: 12/10/2018 14:20:38
*/
int main(){
    int v[15], vpar[5], vimpar[5], posicao, posicao_impar, posicao_par, posicao_impar_final, posicao_par_final;
    for(posicao = 0; posicao < 15; posicao ++){
        scanf("%d", &v[posicao]);
    }
    for(posicao = 0, posicao_par = 0, posicao_impar = 0; posicao < 15; posicao++){
        if(v[posicao]%2 == 0){
            vpar[posicao_par] = v[posicao];
            posicao_par++;
            if(posicao_par == 5){
                for(posicao_par = 0; posicao_par < 5; posicao_par++){
                    printf("par[%d] = %d\n", posicao_par, vpar[posicao_par]);
                }
                posicao_par = 0;
            }
        }
        else /*if(v[posicao]%2 != 0)*/{
            vimpar[posicao_impar] = v[posicao];
            posicao_impar++;
            if(posicao_impar == 5){
                for(posicao_impar = 0; posicao_impar < 5; posicao_impar++){
                    printf("impar[%d] = %d\n", posicao_impar, vimpar[posicao_impar]);
                }
                posicao_impar = 0;
            }
        }
    }
    for(posicao_impar_final = 0; posicao_impar_final < posicao_impar; posicao_impar_final++){
        printf("impar[%d] = %d\n", posicao_impar_final,vimpar[posicao_impar_final]);
    }
    for(posicao_par_final = 0; posicao_par_final < posicao_par; posicao_par_final++){
        printf("par[%d] = %d\n", posicao_par_final,vpar[posicao_par_final]);
    }
}