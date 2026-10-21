#include <stdio.h>
#define MOD 1000000007

int main()
{
    int q;
    scanf("%d", &q);
    for (int k = 0; k < q; k++) {
        long long split, hours;
        scanf("%lld %lld", &split, &hours);
        split %= MOD;
        long long count = 1;
        for (long long h = 0; h < hours; h++) {
            count = count * split % MOD;
        }
        printf("%lld\n", count);
    }
    return 0;
}
