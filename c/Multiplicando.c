#include <stdio.h>
int contador, v, a, b, c;// declarando as variaveis 
int main(){   
    scanf("%d", &v); // quantas veses vai multiplicar 
    scanf("%d", &a);//numero 
    scanf("%d", &b);//expoente
    while (contador <=v ) // enquanto contador for igual veses nao para de elevar 
{   a = a*b;//elevando
    printf("\n%d ", a);//imprimindo o resultado
    contador++; // adicionando 1 em contador ate que seje igual v
}return 0;//matando main
}