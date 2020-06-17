#include <stdio.h>

int main(){
	//declarando variavel
	int idade;
	//entrada
	printf("qual sau idade?\n");
	fflush(stdout);
	scanf("%d", &idade);
	//processament
	if(idade<18){
		printf("voce e menor de idade\n");
	}else if(idade >18 && idade <60){
		printf("voce e adulto\n");
	}else{
		printf("vc e idoso\n");
	}
	//saida
	printf("sua idade e : %d", idade);
 	return 0;
}	