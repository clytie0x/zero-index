#include <stdio.h>

int a[100][100], b[100][100];

int main()
{
    int n, m, p;
    scanf("%d %d %d", &n, &m, &p);
    for (int i = 0; i < n; i++) {
        for (int k = 0; k < m; k++) {
            scanf("%d", &a[i][k]);
        }
    }
    for (int k = 0; k < m; k++) {
        for (int j = 0; j < p; j++) {
            scanf("%d", &b[k][j]);
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            long long sum = 0;
            for (int k = 0; k < m; k++) {
                sum += (long long)a[i][k] * b[k][j];
            }
            printf("%lld", sum);
            if (j < p - 1) {
                printf(" ");
            }
        }
        printf("\n");
    }
    return 0;
}
