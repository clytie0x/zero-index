#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    for (int row = 1; row <= 2 * n - 1; row++) {
        int i = row;
        if (row > n) {
            i = 2 * n - row;
        }
        for (int j = 1; j <= n - i; j++) {
            printf(" ");
        }
        printf("*");
        if (i > 1) {
            for (int j = 1; j <= 2 * i - 3; j++) {
                printf(" ");
            }
            printf("*");
        }
        printf("\n");
    }
    return 0;
}
