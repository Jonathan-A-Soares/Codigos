#include <iostream>
using namespace std;

int numeros[5], resultado;

int main()
{

    for (int i = 1; i < 4; i++)
    {
        cin >> numeros[i];
    }

    resultado = numeros[1] + numeros[2] + numeros[3];

    cout << resultado;
    return 0 ;
}