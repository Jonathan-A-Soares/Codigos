#include <stdio.h>
int i,q;
int v[1000];
int main()
{
    scanf("%d", &q);

    if (q <= 1)
    {
        scanf("%d",&v[0]);
        printf("1");
     
    }else
    {
        q = q - 1;
        while (i < q)
        {
            i++;
            scanf("%d\n", &v[i]);
    }
    q = q+2;
    i = i=0;
        for (i = 1; i < q; i++)
        { 
            printf(" %d",v[i]);
        }
        printf(" %d", q);
        return 0;
}}