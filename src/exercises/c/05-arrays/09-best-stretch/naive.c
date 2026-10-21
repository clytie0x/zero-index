#include <stdio.h>

int profit[200000];

int main()
{
    int n, k;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++) {
        scanf("%d", &profit[i]);
    }
    long long best = 0;
    int best_start = 0;
    for (int start = 1; start <= n - k + 1; start++) {
        long long total = 0;
        for (int day = start; day <= start + k - 1; day++) {
            total += profit[day - 1];
        }
        if (best_start == 0 || total > best) {
            best = total;
            best_start = start;
        }
    }
    printf("%lld %d\n", best, best_start);
    return 0;
}
