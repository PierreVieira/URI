/*
* Autor: Pierre Vieira
* Data de submissão: 03/10/2018 19:45:44
*/
#include <stdio.h>
int main(){
    char string1[30], string2[30], string3[30];
    scanf(" %[^\n]s", string1);
    if (string1[0] == 'v'){
       scanf(" %[^\n]s", string2);
       if(string2[0] == 'a'){
         scanf(" %[^\n]s", string3);
         if(string3[0] == 'c'){
            printf("aguia\n");
            }
          else if(string3[0] == 'o'){
                  printf("pomba\n");
         }
       }
       else if(string2[0] == 'm'){
            scanf(" %[^\n]s", string3);
            if(string3[0] == 'o'){
                printf("homem\n");
            }
            else if(string3[0] == 'h'){
                printf("vaca\n");
            }
       }
    }
    else if(string1[0] == 'i'){
        scanf(" %[^\n]s", string2);
        if(string2[0] == 'i'){
            scanf(" %[^\n]s", string3);
            if(string3[2] == 'm'){
                printf("pulga\n");
            }
            else if(string3[2] == 'r'){
                printf("lagarta\n");
            }
        }
        else if(string2[0] == 'a'){
            scanf(" %[^\n]s", string3);
            if(string3[0] == 'h'){
                printf("sanguessuga\n");
            }
            else if(string3[0] == 'o'){
                printf("minhoca\n");
            }
        }
    }
}