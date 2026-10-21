#include <stdio.h>
#define MOD 1000000007

long long choose(int n, int r)
{
    if (r < 0 || r > n) {
        return 0;
    }
    if (r == 0 || r == n) {
        return 1;
    }
    return (choose(n - 1, r - 1) + choose(n - 1, r)) % MOD;
}

int main()
{
    int q;
    scanf("%d", &q);
    for (int k = 0; k < q; k++) {
        int boys, girls, size;
        scanf("%d %d %d", &boys, &girls, &size);
        long long all = choose(boys + girls, size);
        long long boys_only = choose(boys, size);
        printf("%lld\n", (all - boys_only + MOD) % MOD);
    }
    return 0;
}
