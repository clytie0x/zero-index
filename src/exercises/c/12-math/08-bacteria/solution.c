#include <stdio.h>
#define MOD 1000000007

long long power(long long base, long long exp)
{
    if (exp == 0) {
        return 1;
    }
    long long half = power(base, exp / 2);
    long long result = half * half % MOD;
    if (exp % 2 == 1) {
        result = result * base % MOD;
    }
    return result;
}

int main()
{
    int q;
    scanf("%d", &q);
    for (int k = 0; k < q; k++) {
        long long split, hours;
        scanf("%lld %lld", &split, &hours);
        printf("%lld\n", power(split % MOD, hours));
    }
    return 0;
}
