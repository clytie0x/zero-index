#include <stdio.h>
#include <stdlib.h>

int when[100000];

int compare_int(const void *p, const void *q)
{
    int x = *(const int *)p;
    int y = *(const int *)q;
    if (x < y) {
        return -1;
    }
    if (x > y) {
        return 1;
    }
    return 0;
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &when[i]);
    }
    qsort(when, n, sizeof(int), compare_int);
    long long best = (long long)when[1] - when[0];
    for (int i = 2; i < n; i++) {
        long long gap = (long long)when[i] - when[i - 1];
        if (gap < best) {
            best = gap;
        }
    }
    long long pairs = 0;
    if (best > 0) {
        for (int i = 1; i < n; i++) {
            if ((long long)when[i] - when[i - 1] == best) {
                pairs++;
            }
        }
    } else {
        int start = 0;
        for (int i = 1; i <= n; i++) {
            if (i == n || when[i] != when[i - 1]) {
                long long size = i - start;
                pairs += size * (size - 1) / 2;
                start = i;
            }
        }
    }
    printf("%lld %lld\n", best, pairs);
    return 0;
}
