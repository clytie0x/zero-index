#include <stdio.h>

int main()
{
    int q;
    scanf("%d", &q);
    for (int k = 0; k < q; k++) {
        long long n;
        scanf("%lld", &n);
        printf("%lld =", n);
        int printed = 0;
        for (long long p = 2; p * p <= n; p++) {
            if (n % p == 0) {
                int power = 0;
                while (n % p == 0) {
                    n /= p;
                    power++;
                }
                if (printed) {
                    printf(" *");
                }
                printf(" %lld", p);
                if (power > 1) {
                    printf("^%d", power);
                }
                printed = 1;
            }
        }
        if (n > 1) {
            if (printed) {
                printf(" *");
            }
            printf(" %lld", n);
        }
        printf("\n");
    }
    return 0;
}
