#include <stdio.h>
int caixa, janela, v[5];
int main()
{
    for (int i = 0; i < 5; i++)
    {
        scanf("%d", &v[i]);
    }
    if (v[0] > v[4] && v[1] > v[5] && v[2] > v[4])
        printf("N1");
    else if (v[0] > v[5] && v[1] > v[4] && v[2] > v[5])
        printf("N2");
    else if (v[0] > v[4] && v[1] > v[5] && v[2] > v[4])
        printf("N3");
    else if (v[0] > v[5] && v[1] > v[4] && v[2] > v[5])
        printf("N4");
    else if (v[0] > v[5 && v[1] > v[5] && v[2] > v[4]])
        printf("N5");
    else if (v[0] > v[5] && v[1] > v[4] && v[2] > v[5])
        printf("N6");
    else if (v[0] > v[4] && v[1] > v[5] && v[2] > v[4])
        printf("N1n");
    else if (v[0] > v[5] && v[1] > v[4] && v[2] > v[5])
        printf("N2n");
        

    else
        printf("s");

    return 0;
}