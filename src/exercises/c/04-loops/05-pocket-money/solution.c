#include <stdio.h>

int main()
{
    int received = 0, spent = 0;
    while (1) {
        int amount;
        scanf("%d", &amount);
        if (amount == 0) {
            break;
        }
        if (amount > 0) {
            received += amount;
        } else {
            spent -= amount;
        }
    }
    printf("%d\n", received);
    printf("%d\n", spent);
    printf("%d\n", received - spent);
    return 0;
}
