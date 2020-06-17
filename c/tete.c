#include <stdio.h>
int main(){
    char nom, pes, ida, aio;
printf("\nOla Bem vindo\n ");
printf("Qual seu nome:");
    scanf("%s", &nom);

printf(" sua idade? ");
    scanf(" %d", &ida);
    if(ida <18){
        printf("\nVoce nao cumpre os requisitos minimos \n");
        return 0;
    }

printf("\nqual seu peso\n");
    scanf("%d", &pes);
    if (pes <60) {
        printf("\nVoce nao cumpre os requisitos minimos\n");
        return 0;
        }

printf("\nQual sua altura\n ");
    scanf("%d", &aio);
    if (aio <=160){
        printf("sua altura e %d", aio);
        printf("\nVoce nao cumpre os requisitos retardo minimos\n");
        return 0;
    }else{
        printf(" \nVoce cumpre os requisitos minimos\n");
        return 0;
    }

  
}