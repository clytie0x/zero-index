#include <stdio.h>

int a[100][100];

int main()
{
    int n;
    scanf("%d", &n);
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < n; c++) {
            scanf("%d", &a[r][c]);
        }
    }
    long long main_sum = 0, anti_sum = 0;
    for (int i = 0; i < n; i++) {
        main_sum += a[i][i];
        anti_sum += a[i][n - 1 - i];
    }
    long long cross = main_sum + anti_sum;
    if (n % 2 == 1) {
        cross -= a[n / 2][n / 2];
    }
    printf("%lld\n%lld\n%lld\n", main_sum, anti_sum, cross);
    return 0;
}
