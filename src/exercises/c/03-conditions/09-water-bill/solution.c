#include <stdio.h>

int main()
{
    int units;
    scanf("%d", &units);
    int bill;
    if (units <= 10) {
        bill = units * 8;
    } else if (units <= 30) {
        bill = 10 * 8 + (units - 10) * 12;
    } else {
        bill = 10 * 8 + 20 * 12 + (units - 30) * 20;
    }
    if (bill < 50) {
        bill = 50;
    }
    printf("%d\n", bill);
    return 0;
}
