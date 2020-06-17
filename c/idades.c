#include <stdio.h>
int main(){

    int m, a, b, c;

    scanf("%d",&m);
    scanf("%d",&a);
    scanf("%d",&b);
    c = m - (a+b);
    if (a>b&&a>c)
    {
        printf("%d",a);
    }else if (b>c&&b>a)
    {
        printf("%d",b);
    }else
    {
        printf("%d",c);
    }
    
    return 0;
}