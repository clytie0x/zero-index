#include <stdio.h>

int when[100000];

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &when[i]);
    }
    long long best = -1;
    long long pairs = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            long long gap = (long long)when[i] - when[j];
            if (gap < 0) {
                gap = -gap;
            }
            if (best == -1 || gap < best) {
                best = gap;
                pairs = 1;
            } else if (gap == best) {
                pairs++;
            }
        }
    }
    printf("%lld %lld\n", best, pairs);
    return 0;
}
