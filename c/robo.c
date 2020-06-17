#include <stdio.h>
int robo;
int main()
{scanf("%d", &robo);
if (robo < 800)
    printf("1");
else if (robo < 2000)
    printf("2");
else
    printf("3");
return 0;
}