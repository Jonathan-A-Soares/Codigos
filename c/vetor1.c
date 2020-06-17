#include <stdio.h>
int main(){
   int teste[4];
   for (int i = 1; i < 4; i++)
   {
    scanf("%d",&teste[i]);
   }
   printf("\n%d", teste[1]+teste[2]+teste[3]);
   return 0 ;
}
