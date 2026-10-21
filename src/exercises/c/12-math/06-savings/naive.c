#include <stdio.h>

int main()
{
    int q;
    scanf("%d", &q);
    for (int k = 0; k < q; k++) {
        long long first, step, days;
        scanf("%lld %lld %lld", &first, &step, &days);
        long long total = 0, amount = first;
        for (long long day = 0; day < days; day++) {
            total += amount;
            amount += step;
        }
        printf("%lld\n", total);
    }
    return 0;
}
