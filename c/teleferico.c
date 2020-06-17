#include<stdio.h>
 int c, a, r;
int main()
{   scanf("%d", &c);
    scanf("%d", &a);
    c = c -1;
    r = a / c;
    if (a % c > 0)
    {r = r + 1;
    printf("%d", r);}
    else
    {printf("%d", r);}
    return 0;
}