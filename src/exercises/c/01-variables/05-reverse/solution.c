#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int hundreds = n / 100;
    int tens = n / 10 % 10;
    int ones = n % 10;
    printf("%d\n", ones * 100 + tens * 10 + hundreds);
    return 0;
}
