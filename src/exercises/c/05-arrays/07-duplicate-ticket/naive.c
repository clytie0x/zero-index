#include <stdio.h>

int ticket[200000];

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &ticket[i]);
    }
    for (int j = 1; j < n; j++) {
        for (int i = 0; i < j; i++) {
            if (ticket[i] == ticket[j]) {
                printf("%d %d\n", j + 1, ticket[j]);
                return 0;
            }
        }
    }
    printf("-1\n");
    return 0;
}
