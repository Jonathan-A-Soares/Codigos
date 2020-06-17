#include <stdio.h>

int main(){
	
	int numero1;
	int numero2;
	
	printf("digite um numero\n");
	fflush(stdout);
	scanf("%d", &numero1);
	fflush(stdout);
	printf("digite outro numero\n");
	fflush(stdout);
	scanf("%d", &numero2);

	if(numero2>numero1){
		printf("O Maior e %d", numero2 );
		
	}else if (numero1>numero2){
		printf("O Maior e %d", numero1 );
	}

 	return 0;
}	