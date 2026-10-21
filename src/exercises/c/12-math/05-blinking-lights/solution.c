#include <stdio.h>

long long gcd(long long a, long long b)
{
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

int main()
{
    int n;
    scanf("%d", &n);
    long long answer = 1;
    for (int i = 0; i < n; i++) {
        long long period;
        scanf("%lld", &period);
        answer = answer / gcd(answer, period) * period;
    }
    printf("%lld\n", answer);
    return 0;
}
