#include <stdio.h>

int main(){
	//declaraçao das variaveis

	int pontos = 0;

	
	char res = 'a';
	char ras =  'a';
	
	printf("\n");
	

	//inicio (entrada)
	printf("Bem vindo quis alfagames\n");
	
	scanf("aperte enter para continuar\n");
	
	printf("pergunta 1 ");
	
	printf("\n\nEm que continete se encontra o japao?\n\n");

	printf("(a)  America do Norte \n");
	printf("(b)  America do sul\n");
	printf("(c)  Asia\n");
	printf("(d)  Afica\n");
    printf("\ndigite uma letra\n");
	scanf("%c", &res);
	printf("sua reposta %c\n", res );
	// proseçamento
	
	if(res == 'c'){
		printf ("acertou\n");
		pontos += 5;
		
	


	}
	else {
		printf("Errou \nR:C\n");
		printf("Pontos Feitos: %d \n", pontos);
		return 0;
	}


	
	
	

	printf("\n\n\n\n\n\npergunta 2\n\n ");
	
	printf("Qual oceano banha a costa Brasileira?\n\n");

	printf("(a)  Pacifico \n");
	printf("(b)  Atlantico\n");
	printf("(c)  Indico\n");
	printf("(d)  Artico\n");
    printf("digite uma letra\n");
	scanf("%c", &ras);
	printf("sua reposta %c\n", ras );
	// proseçamento
	
	if(ras == 'b'){
		printf ("acertou\n");
		pontos += 5;

	}
	else {
		printf("Errou \nR:b\n");
		printf("Pontos Feitos: %d \n", pontos);
		return 0;
	}
	printf("pergunta 3 ");
	return 0;
}
