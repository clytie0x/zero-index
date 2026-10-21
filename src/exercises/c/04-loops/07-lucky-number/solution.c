#include <stdio.h>

int main()
{
    long long n;
    scanf("%lld", &n);
    printf("%lld", n);
    while (n >= 10) {
        long long digit_sum = 0;
        while (n > 0) {
            digit_sum += n % 10;
            n /= 10;
        }
        n = digit_sum;
        printf(" %lld", n);
    }
    printf("\n");
    return 0;
}
