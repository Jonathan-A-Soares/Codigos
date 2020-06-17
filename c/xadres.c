#include <stdio.h>
int main()
{
    int A = 0, B = 0;
    scanf("%d", &A);
    scanf("%d", &B);
    if (A % 2 == B % 2)
        printf("1");
    else
        printf("0");
    return 0;
}