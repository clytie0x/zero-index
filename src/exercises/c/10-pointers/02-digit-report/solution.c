#include <stdio.h>

void digit_report(long long x, int *count, int *sum, int *low, int *high)
{
    *count = 0;
    *sum = 0;
    *low = 9;
    *high = 0;
    do {
        int digit = x % 10;
        *count += 1;
        *sum += digit;
        if (digit < *low) {
            *low = digit;
        }
        if (digit > *high) {
            *high = digit;
        }
        x /= 10;
    } while (x > 0);
}

int main()
{
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        long long x;
        scanf("%lld", &x);
        int count, sum, low, high;
        digit_report(x, &count, &sum, &low, &high);
        printf("%d %d %d %d\n", count, sum, low, high);
    }
    return 0;
}
