#include <stdio.h>
#define MOD 1000000007

int choose[2001][2001];

int main()
{
    for (int i = 0; i <= 2000; i++) {
        choose[i][0] = 1;
        for (int j = 1; j <= i; j++) {
            choose[i][j] = (choose[i - 1][j - 1] + choose[i - 1][j]) % MOD;
        }
    }
    int q;
    scanf("%d", &q);
    for (int k = 0; k < q; k++) {
        int boys, girls, size;
        scanf("%d %d %d", &boys, &girls, &size);
        long long all = choose[boys + girls][size];
        long long boys_only = 0;
        if (size <= boys) {
            boys_only = choose[boys][size];
        }
        printf("%lld\n", (all - boys_only + MOD) % MOD);
    }
    return 0;
}
