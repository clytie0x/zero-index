#include <stdio.h>

int profit[200000];
long long prefix[200001];

int main()
{
    int n, k;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++) {
        scanf("%d", &profit[i]);
    }
    prefix[0] = 0;
    for (int i = 1; i <= n; i++) {
        prefix[i] = prefix[i - 1] + profit[i - 1];
    }
    long long best = prefix[k] - prefix[0];
    int best_start = 1;
    for (int start = 2; start <= n - k + 1; start++) {
        long long total = prefix[start + k - 1] - prefix[start - 1];
        if (total > best) {
            best = total;
            best_start = start;
        }
    }
    printf("%lld %d\n", best, best_start);
    return 0;
}
