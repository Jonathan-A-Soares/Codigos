#include <stdio.h>

int main(){

	int valor;
	printf("\n sabado= 1\n domindo= 2\n segunda= 3\n terca= 4\n quarta= 5\n quinta= 6\n sexta= 7\n\n\n");

	printf("digite o dia da semana \n");
	
	scanf("%d", &valor);

	switch(valor){

	  case 1:
	  printf("dia selecionado = sabado\n");
	  break;

	  case 2:
	  printf("dia selecionado = domingo\n");
	  break;

	  case 3:
	  printf("dia selecionado = segunda\n");
	  break;

	  case 4:
	  printf("dia selecionado = terca\n");
	  break;

	  case 5:
	  printf("dia selecionado = quarta\n");
	  break;

	  case 6:
	  printf("dia selecionado = quinta\n");
	  break;

	  case 7:
	  printf("dia selecionado = sexta\n");
	  break;

	}

	if(valor>7){
		printf("numero invalido\n");

	}else if(valor<7){
		return 0;
	}
	
}