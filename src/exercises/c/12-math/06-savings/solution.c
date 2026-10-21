#include <stdio.h>

int main()
{
    int q;
    scanf("%d", &q);
    for (int k = 0; k < q; k++) {
        long long first, step, days;
        scanf("%lld %lld %lld", &first, &step, &days);
        long long total = days * first + step * (days * (days - 1) / 2);
        printf("%lld\n", total);
    }
    return 0;
}
