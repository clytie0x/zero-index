#include <stdio.h>

int main()
{
    long long n;
    scanf("%lld", &n);
    long long count = 0, sum = 0;
    for (long long i = 1; i <= n; i++) {
        if (n % i == 0) {
            count++;
            sum += i;
        }
    }
    printf("%lld %lld\n", count, sum);
    return 0;
}
