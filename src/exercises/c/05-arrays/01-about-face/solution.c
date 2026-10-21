#include <stdio.h>

int id[1000];

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &id[i]);
    }
    for (int i = n - 1; i >= 0; i--) {
        printf("%d", id[i]);
        if (i > 0) {
            printf(" ");
        }
    }
    printf("\n");
    return 0;
}
