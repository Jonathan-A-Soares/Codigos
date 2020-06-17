#include <stdio.h>
int main()
{
    int A, a, B, b, a1, A1, B1, b1, H;
    H = 70;
    A = 0;
    A1 = 0;
    scanf("%d", &B);
    scanf("%d", &b);
    b1 = 160 - b;
    B1 = 160 - B;
    A = ((B + b) / 2) * H;
    A1 = ((B1 + b1) / 2) * H;
    if (A < A1)
    printf("2");
    else if (A>A1)
    printf("1");
    else 
    printf("0");
    return 0;
}