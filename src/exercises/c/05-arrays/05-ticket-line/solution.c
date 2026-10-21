#include <stdio.h>

int line[1000];

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &line[i]);
    }
    int p, q, x;
    scanf("%d %d %d", &p, &q, &x);
    for (int i = p - 1; i < n - 1; i++) {
        line[i] = line[i + 1];
    }
    n--;
    for (int i = n; i > q - 1; i--) {
        line[i] = line[i - 1];
    }
    line[q - 1] = x;
    n++;
    for (int i = 0; i < n; i++) {
        printf("%d", line[i]);
        if (i < n - 1) {
            printf(" ");
        }
    }
    printf("\n");
    return 0;
}
