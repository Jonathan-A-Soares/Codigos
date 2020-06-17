#include <stdio.h>

int main(void)
{
    int termos,
        razao,
        inicial,
        count;

    printf("Numero de termos da P.A: ");
    scanf("%d", &termos);

    printf("Razao da P.A: ");
    scanf("%d", &razao);

    printf("Elemento inicial da P.A: ");
    scanf("%d", &inicial);

    for (count = 1; count <= termos; count++)
        printf("Termo %d: %d\n", count, (inicial + (count - 1) * razao));
}
